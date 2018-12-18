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
	    title = car.css('div.offer-item__title > h2.offer-title > a::attr(title)').extract_first()
	    link_car = car.css('div.offer-item__title > h2.offer-title > a::attr(href)').extract_first()
	    sub_tit = car.css('div.offer-item__title > h3.offer-item__subtitle::text').extract_first()
	    sub_title = sub_tit.strip()  if sub_tit is not None else sub_tit
	    price = car.css('span.offer-price__number::text').extract_first()
	    annee = car.css('li.offer-item__params-item > span::text').extract()[0]
	    km = car.css('li.offer-item__params-item > span::text').extract()[1]
            capacite = car.css('li.offer-item__params-item > span::text').extract()[2]
	    image = car.css('div.offer-item__photo > a > img::attr(data-src)').extract_first()
            yield Request(link_car, callback=self.parse_page, meta={'title':title, 'link_car':link_car, 'sub_title':sub_title, 'price':price, 'annee':annee, 'km':km, 'capacite':capacite, 'image':image})

	relative_next_url = response.css('li.next > a::attr(href)').extract_first()
        yield Request(relative_next_url, callback=self.parse)


    def parse_page(self, response):
	item = CarsItem()
	#title = response.meta.get('title')
        #link_car = response.meta.get('link_car')
	#sub_title = response.meta.get('sub_title')
	#price = response.meta.get('price')
	#annee = response.meta.get('annee')
	#km = response.meta.get('km')
	#capacite = response.meta.get('capacite')
	img_url = response.meta.get('image')
        #location = response.css('span.seller-box__seller-address__label::text').extract_first().strip()
	#phone = response.css('span.phone-number::text').extract_first()
        #marque = response.css('div.offer-params__value > a.offer-params__link::attr(title)').extract()[2].strip()
	#modele = response.css('div.offer-params__value > a.offer-params__link::text').extract()[3].strip()
        #img_url = response.css('div.photo-item > img.bigImage::attr(src)').extract_first()
        #yield {'title':title, 'link_car':link_car, 'sub_title':sub_title, 'price':price, 'annee':annee, 'km':km, 'capacite':capacite, 'location':location, 'phone':phone, 'marque':marque, 'modele':modele, 'image_urls': [img_url]}
	yield{'image_urls': [img_url]}
