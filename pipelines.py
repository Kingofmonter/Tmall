# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.exporters import JsonItemExporter
from Tmall.items import *

class TmallPipeline(object):
    def process_item(self, item, spider):
        return item


class TmallWithJsonPipeline(object):    #商品列表管道

    def __init__(self):
        self.file = open('uniqlo_list.json', 'ab')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        print(item)
        if isinstance(item,TmallItem):
            self.exporter.export_item(item)
            return item


class GoodsWithJsonPipeline(object):    #商品详情管道

    def __init__(self):

        self.file = open('goodsdetail.json', 'ab')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item