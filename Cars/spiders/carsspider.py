# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from Cars.items import CarsItem

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
	    sub_tit = car.css('div.offer-item__title > h3.offer-item__subtitle::text').extract_first()
	    sub_title = sub_tit.strip()  if sub_tit is not None else sub_tit
	    yield Request(link_car, callback=self.parse_page, meta={'link_car':link_car,'sub_title':sub_title})

	#relative_next_url = response.css('ul.om-pager > li  > a::attr(href)').extract()
        #absolute_next_url = response.urljoin(relative_next_url)
        #for url in response.css('ul.om-pager > li'):
	#    absolute_next_url = url.css('a::attr(href)').extract_first()
	    #print(absolute_next_url)
	#    yield Request(absolute_next_url, callback=self.parse)


    def parse_page(self, response):
	item = CarsItem()
        item['link_car'] = response.meta.get('link_car')
	item['sub_title'] = response.meta.get('sub_title')
        item['location'] = response.css('span.seller-box__seller-address__label::text').extract_first().strip()
	yield item

