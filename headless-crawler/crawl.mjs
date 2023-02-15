import {PlaywrightCrawler} from 'crawlee';
import {router} from "./router.mjs";
import {url as categoryUrl} from './category.mjs'


const crawler = new PlaywrightCrawler({
    // headless: false,
    // maxRequestsPerMinute: 2,
    requestHandler: router,
});

await crawler.run([
    // categoryUrl('telescope-cameras'),
    categoryUrl('telescope-mounts'),
]);
