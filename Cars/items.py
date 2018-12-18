# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link_car = scrapy.Field()
    sub_title = scrapy.Field()
    location = scrapy.Field()
    phone = scrapy.Field()
    marque = scrapy.Field()
    modele = scrapy.Field()
    price = scrapy.Field()
    annee = scrapy.Field()
    km = scrapy.Field()
    capacite = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
