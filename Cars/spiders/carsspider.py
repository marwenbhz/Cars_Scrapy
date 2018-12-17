# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess


class CarsspiderSpider(scrapy.Spider):
    name = 'carsspider'
    allowed_domains = ['otomoto.pl']
    start_urls = ['https://www.otomoto.pl/osobowe/']
    custom_settings = {
    'LOG_FILE': 'logs/cars.log',
    'LOG_LEVEL':'ERROR'
     }


    def parse(self, response):
        print('Processing...' + response.url)
	for car in response.css('article.adListingItem'):
	    #title = car.css('h2.offer-title::text').extract_first()
	    link_car = car.css('div.offer-item__title > h2.offer-title > a::attr(href)').extract_first()
	    sub_title = car.css('div.offer-item__title > h3.offer-item__subtitle::text').extract_first()
	    print(sub_title)

	#relative_next_url = response.css('ul.om-pager > li  > a::attr(href)').extract()
        #absolute_next_url = response.urljoin(relative_next_url)
        #for url in response.css('ul.om-pager > li'):
	#    absolute_next_url = url.css('a::attr(href)').extract_first()
	    #print(absolute_next_url)
	#    yield Request(absolute_next_url, callback=self.parse)


    def parse_page(self, response):
	pass
