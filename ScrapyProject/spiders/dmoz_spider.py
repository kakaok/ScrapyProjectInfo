#coding=utf-8
'''
Created on 2015年9月14日

@author: kaka
'''

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from ..items import DmoItem

class DmoSpider(BaseSpider):
    name = "dmoz"
    allowed_domains=["dmoz.org"]
    start_urls = [
                "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
                "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
                ]
    def parse(self,response):
        hxs=HtmlXPathSelector(response)
        sites=hxs.xpath('//fieldset/ul/li')
        items=[]
        for site in sites:
            item=DmoItem()
            item['title']=site.xpath('a/text()').extract()
            item['link']=site.xpath('a/@href').extract()
            item['desc']=site.xpath('text()').extract()
            items.append(item)
        return items
#             print title,link,desc
#         filename=response.url.split("/")[-2]
#         open(filename,"wb").write(response.body)
    
