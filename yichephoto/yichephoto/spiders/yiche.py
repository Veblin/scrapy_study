# -*- coding: utf-8 -*-
import scrapy

def transStr (text):
    if type(text) == bytes:
        return text.decode('unicode_escape')
    else:
        return text.encode('latin-1').decode('unicode_escape')

class YicheSpider(scrapy.Spider):
    name = 'yiche'
    allowed_domains = ['photo.yiche.com','bitautoimg.com']
    start_urls = [
        'http://photo.bitauto.com/master/7/',
        # 'http://photo.bitauto.com/master/8/',
        # 'http://photo.bitauto.com/master/9/'
        ]
        # //*[@id="carContent"]/div[1]/div/h2
    rules = []
    # def parse_item(self, response):
    #     self.logger.info('Hi, this is an item page! %s', response.url)
    #     item = scrapy.Item()
    #     # item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
    #     item['brand'] = response.xpath('//*[@id="carContent"]/div[1]/div/h2/text()').extract()
    #     # item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
    #     return item
    #     # vendor : //*[@id="carContent"]/h5/a 
    #     # car //*[@id="carContent"]/div[2]/div[1]/div/div/a


    def parse(self, response):
        # do something with response
        for h2 in response.xpath('//*[@id="carContent"]/div[1]/div/h2/text()').extract():
            yield {"title": h2}

        for url in response.xpath('//*[@id="carContent"]/div[2]//a/@href').extract():
            yield {"links": url}
            yield scrapy.Request(url, callback=self.parse)

            
        self.logger.info('A response from %s just arrived!', response.url)
        # pass
