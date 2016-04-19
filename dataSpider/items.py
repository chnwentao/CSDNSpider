# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 定义在抓取网页内容中抽象出来的数据结构的定义，由于这里需要博客名称、发布日期、阅读量和评论量这四个字段，定义的Item结构如下：
class DataspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title = scrapy.Field()
	link = scrapy.Field()
	publishDate = scrapy.Field()  #发布日期
	readCount = scrapy.Field()  #阅读量
	commentCount = scrapy.Field() #评论数<br><br>
	article = scrapy.Field() #正文
	desc = scrapy.Field()
