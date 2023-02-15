import {createPlaywrightRouter} from 'crawlee';
import {handler as productHandler} from "./product.mjs";
import {handler as categoryHandler} from "./category.mjs";

const router = createPlaywrightRouter();

router.addDefaultHandler(categoryHandler)
router.addHandler('category', categoryHandler)
router.addHandler('product', productHandler)

export {router}