import {Dataset, KeyValueStore, log} from '@crawlee/playwright';
import {shortTitle, shortUrl} from "./page.mjs";
import {htmlToText} from "@crawlee/utils";
import {key} from "./store.mjs";

const accessors = {
    html: async (page) => page.$eval('body .product', el => el.outerHTML),
    title: async (page) => await shortTitle(page),
    breadcrumbs: async (page) =>
        await page.$$eval('.breadcrumb-collection .breadcrumb_text', els =>
            Array.from(els).map(el => Array.from(el.querySelectorAll('a')).map(el => el.textContent.trim()).filter(el => el.length))),
    vendor: async (page) => await page.$eval('.vendor .vendor', el => el.textContent),
    price: async (page) => cleanPrice(await page.$eval('.current_price', s => s.textContent)),
    specs: async (page) => {
        const entries = await page.$$eval('.specifications tr', trs => trs.map(tr => [tr.querySelector('.left').textContent.trim(), tr.querySelector('.right').textContent.trim(),]));
        return Object.fromEntries(entries)
    }
}

function cleanPrice(price) {
    return price.match(/[\d.,]+/)[0].replace(",", '');
}

class Crawler {
    key;
    context;

    constructor(key, context) {
        this.key = key
        this.context = context
    }

    async all() {
        return await Promise.all([
            this.html(),
            this.productText(),
            this.structured(),
        ])
    }

    async html() {
        const { page } = this.context;
        const content = await page.content();
        await KeyValueStore.open()
        await KeyValueStore.setValue(this.key, content, {contentType: 'text/html'});
    }

    async productText() {
        const { page } = this.context;
        const content = await page.$eval('body .product', el => el.innerHTML)
        const text = htmlToText(content)
        await KeyValueStore.setValue(this.key, text, {contentType: 'text/plain'});
    }

    async structured() {
        const { page, request } = this.context;
        const {
            title, breadcrumbs, vendor, price, specs, html
        } = accessors
        const data = {
            title: await title(page),
            url: request.loadedUrl,
            breadcrumbs: await breadcrumbs(page),
            vendor: await vendor(page),
            price: await price(page),
            specs: await specs(page),
            html: await html(page),
        }
        await Dataset.pushData(data);
    }
}

const handler = async (context) => {
    const {request, page, log} = context;
    await page.waitForSelector('body .product')
    const title = await shortTitle(page);
    log.info(`PRODUCT: "${title}" - ${shortUrl(request.loadedUrl)}`);
    const storageKey = key(title)
    log.debug(`storageKey: ${storageKey}`)
    const crawler = new Crawler(storageKey, context);
    await crawler.all()
}

const url = (category, name) => `https://optcorp.com/collections/${category}/products/${name}`

export {handler, url}