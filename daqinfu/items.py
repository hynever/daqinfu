# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QinItem(scrapy.Item):
    pub_time = scrapy.Field()
    rating = scrapy.Field()
    content = scrapy.Field()
