# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    star = scrapy.Field()
    rate = scrapy.Field()
    pl = scrapy.Field()
    link = scrapy.Field()
    quote = scrapy.Field()
    playable = scrapy.Field()
    type = scrapy.Field()
    #pass
