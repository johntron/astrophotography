import {PlaywrightCrawler, Configuration } from '@crawlee/playwright';
import {router} from "./router.mjs";
import {url as categoryUrl} from './category.mjs'
import {url as productUrl} from './product.mjs'

const now = new Date()
const config = new Configuration({
    purgeOnStart: false,
    defaultDatasetId: now,
    defaultKeyValueStoreId: now,
    defaultRequestQueueId: now,
})


await new PlaywrightCrawler({
    // headless: false,
    // maxRequestsPerMinute: 5,
    requestHandler: router,
}, config).run([
    // categoryUrl('telescope-cameras'),
    categoryUrl('telescope-mounts'),
    // {label: 'product', url: productUrl('telescope-mounts', 'sky-watcher-az-gti-computerized-altitude-azimuth-mount')},
]);
