# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class DataspiderPipeline(object):

    # 将item写入JSON文件
    def __init__(self):
        self.file = open('./data/items.json', 'wb')


    # 每个item pipeline组件都需要调用该方法，这个方法必须返回一个具有数据的dict，或是 Item (或任何继承类)对象， 或是抛出 DropItem 异常，被丢弃的item将不会被之后的pipeline组件所处理。
    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + "\n" #此处如果有中文的话，要加上ensure_ascii=False参数，否则可能出现乱码
        self.file.write(line)
        return item

    # 当spider被开启时，这个方法被调用。
    # spider (Spider 对象) – 被开启的spider
    def open_spider(self, spider):
        pass


    # spider被关闭时，这个方法被调用
    def close_spider(self, spider):
        self.file.close()
