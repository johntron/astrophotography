# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class OptCorpProducts(CrawlSpider):
    name = "optcorp_products"
    allowed_domains = ['optcorp.com']
    start_urls = ['https://optcorp.com/collections/telescope-cameras', ]
    rules = (
        Rule(LinkExtractor(restrict_css='.snize-product'), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Found %s', response.url)
