# -*- coding: utf-8 -*-
import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
import hashlib
import re,os
import requests

class CeshiSpider(RedisCrawlSpider):
    name = 'meizitu'
    allowed_domains = ['mzitu.com']
    redis_key = 'meizitu:start_urls'
    a = 1
    header = {

        "Connection":"keep-alive",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Accept":"image/webp,image/apng,image/*,*/*;q=0.8",
        "Referer":"http://www.mzitu.com/xinggan/robot/",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.8",
    }

    rules = (
        Rule(LinkExtractor(allow=r'mzitu.com/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'mzitu.com/\d+/\d+'), callback='parse_item', follow=True),

    )

    def parse_item(self, response):
        img_url = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract()[0]
        fname = response.xpath('//div[@class="main-image"]/p/a/img/@alt').extract()[0]
        img = img_url.split('/')[-1]
        print img_url
        print fname
        print img
        if not os.path.exists('./meizi1/'+fname):
            os.makedirs('./meizi1/'+fname)
            print '创建成功'
        html = requests.get(img_url,headers = self.header)
        html = html.content
        with open('./meizi1/'+fname+'/'+img,'wb') as f:
            f.write(html)
        print '爬取第%d张图片' % self.a
        self.a += 1
