import {shortUrl, shortTitle} from "./page.mjs";

const pageNumber = (request) => (new URL(request.loadedUrl).searchParams.get('page') || 1)

const transformRequestFunction = request => {
    const url = new URL(request.url)

    if (url.searchParams.get('page') === '1') {
        url.searchParams.delete('page')
    }

    url.searchParams.sort()

    // Fix for leading hash - e.g. ?&page=1
    url.search = url.searchParams.toString()

    request.url = url.toString()
    return request;
}
const handler = async ({request, page, enqueueLinks, log}) => {
    log.info(`CATEGORY: "${await shortTitle(page)}" p${pageNumber(request)} - ${shortUrl(request.loadedUrl)}`);
    await page.waitForSelector('.snize-product')
    await enqueueLinks({
        label: 'category',
        strategy: 'same-domain',
        selector: '.snize-pagination a',
        transformRequestFunction,
    })
    await enqueueLinks({
        label: 'product',
        strategy: 'same-domain',
        selector: '.snize-search-results-main-content a',
    });
};

const url = name => `https://optcorp.com/collections/${name}`

export {handler, url}