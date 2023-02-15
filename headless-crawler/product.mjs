import {PlaywrightCrawler, Dataset} from 'crawlee';
import {shortTitle, shortUrl} from "./page.mjs";

const title = async (page) => await page.title();
const breadcrumbs = async (page) => {
    const collection = await page.$$eval('.breadcrumb-collection .breadcrumb_text', els => {
        return Array.from(els).map(el => {
            return Array.from(el.querySelectorAll('a')).map(el => el.textContent.trim()).filter(el => el.length)
        })
    })
    return collection
}
const vendor = async (page) => await page.$eval('.vendor .vendor', el => el.textContent)
const price = async (page) => cleanPrice(await page.$eval('.current_price', s => s.textContent));
const specs = async (page) => {
    const entries = await page.$$eval('.specifications tr', trs => trs.map(tr => [tr.querySelector('.left').textContent.trim(), tr.querySelector('.right').textContent.trim(),]));
    return Object.fromEntries(entries)
}

function cleanPrice(price) {
    return price.match(/[\d.,]+/)[0].replace(",", '');
}

const html = async (page) => page.$eval('body .product', el => el.outerHTML)

const handler = async ({request, page, enqueueLinks, log}) => {
    const title = await shortTitle(page);
    const url = request.loadedUrl
    log.info(`PRODUCT: "${title}" - ${shortUrl(request.loadedUrl)}`);
    const data = {
        title,
        url,
        breadcrumbs: await breadcrumbs(page),
        vendor: await vendor(page),
        price: await price(page),
        specs: await specs(page),
        html: await html(page),
    }
    await Dataset.pushData(data);
}

export {handler}