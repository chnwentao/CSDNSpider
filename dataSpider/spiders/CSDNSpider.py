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
        "http://blog.csdn.net/sjz4860402",
    ]

    #rules = (
    #    Rule(LinkExtractor(allow=('fengzheng/default.html\?page\=([\d]+)', ),),callback='parse_item',follow=True),
    #)  #制定规则


    #减慢爬取速度 为2s
    download_delay = 2


    rules = (

        # 提取匹配 '/article/details/' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('/article/details/', )), callback='parse_item',follow=True),
    )

    # 回调函数
    # 用来处理Response对象，返回爬取的数据，并且获得更多等待爬取的链接。
    # 默认的 request 得到 response 之后会调用这个回调函数，我们需要在这里对页面进行解析，返回两种结果（需要进一步 crawl 的链接和需要保存的数据）
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

        





