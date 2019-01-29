# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class TmallPipeline(object):
    def process_item(self, item, spider):
        return item


class TmallWithJsonPipeline(object):

    def __init__(self):
        print(True)
        self.file = codecs.open('unqilo_list.json','a+',encoding='utf8')

    def process_item(self,item,spider):

        line = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(line)

        return item

    def spider_closed(self,item,spider):

        self.file.close()

class GoodsWithJsonPipeline(object):

    def __init__(self):
        print(True)
        self.file = codecs.open('goods_detail.json','a+',encoding='utf8')

    def process_item(self,item,spider):

        line = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(line)

        return item

    def spider_closed(self,item,spider):

        self.file.close()