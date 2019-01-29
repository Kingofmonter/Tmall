# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmallItem(scrapy.Item):   #商品列表Item
    # define the fields for your item here like:
    # name = scrapy.Field()
    item_id = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    sold = scrapy.Field()
    quantity = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()

class GoodsDetail(scrapy.Item): #商品详情Item

    name = scrapy.Field()
    brand = scrapy.Field()
    size = scrapy.Field()
    color = scrapy.Field()
    num = scrapy.Field()
    style = scrapy.Field()
    season = scrapy.Field()
    listing_year = scrapy.Field()
    scenario =scrapy.Field()
    type = scrapy.Field()
    composition = scrapy.Field()