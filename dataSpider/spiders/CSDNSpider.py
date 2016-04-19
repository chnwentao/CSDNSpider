# _#_ coding:utf-8 _*_
__author__ = 'wente'
import scrapy
from dataSpider.items import DataspiderItem
import re

from goose import Goose
from goose.text import StopWordsChinese

from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule


class CSDNSpider(CrawlSpider):
    # 爬虫的名字
    name = "csdn"

    # 爬取范围（可选）
    allowed_domains = ["blog.csdn.net"]  #设置允许的域名

    #设置开始爬取页面
    start_urls = [
        "http://blog.csdn.net/",
    ]

    #减慢爬取速度 为2s
    download_delay = 2

    #制定规则
    rules = (

        # 提取匹配 '/article/details/' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('/article/details/', )), callback='parse_item',follow=True),
    )

    # 回调函数
    # 接受一个response作为其第一个参数， 并返回一个包含 Item 以及(或) Request 对象(或者这两者的子类)的列表(list)。
    def parse_item (self, response):

        #获得文章url和标题
        item = DataspiderItem()
        sel = scrapy.Selector(response)

        title = sel.xpath('//*[@class="link_title"]/a/text()').extract()[0]
        link = str(response.url)
        publishDate = sel.xpath('//*[@class="link_postdate"]/text()').extract()[0]  #发布日期
        readCount =  sel.xpath('//*[@class="link_view"]/text()').re(r'\d+')[0]  #阅读量

        g = Goose({'stopwords_class': StopWordsChinese})
        article = g.extract(url=response.url)
        articleText = article.cleaned_text

        item['title'] =title.encode('utf-8')
        item['link'] = link.encode('utf-8')
        item['publishDate'] = publishDate.encode('utf-8')
        item['readCount'] = readCount.encode('utf-8')
        item['article'] = articleText.encode('utf-8')

        return item # 是一个类似 return 的关键字，只是这个函数返回的是个生成器。

        





