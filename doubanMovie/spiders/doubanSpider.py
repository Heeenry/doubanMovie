# -*- coding: utf-8 -*-
import scrapy
from doubanMovie.items import DoubanmovieItem


class doubanSpider(scrapy.Spider):
    name = 'doubanMovie1'
    allowed_domains = ["douban.com"]
    start_urls = [
        'https://movie.douban.com/top250',
    ]

    def parse(self, response):
        for movie in response.xpath('//div[@class="item"]'):
            item = DoubanmovieItem()
            item['rank'] = movie.xpath('./div[@class="pic"]/em/text()').extract_first()
            item['title'] = movie.xpath('./div[@class="pic"]/a/img/@alt').extract_first()
            item['playable'] = movie.xpath('.//span[@class="playable"]/text()').extract_first()
            item['link'] = movie.xpath('./div[@class="pic"]/a/@href').extract_first()
            item['star'] = movie.xpath('.//div[@class="star"]/span[1]/@class').extract_first()
            item['rate'] = movie.xpath('.//span[@class="rating_num"]/text()').extract_first()
            item['pl'] = movie.xpath('.//div[@class="star"]/span[4]/text()').extract_first()[:-3]
            item['quote'] = movie.xpath('.//p[@class="quote"]/span/text()').extract_first()
            item['type'] = movie.xpath('.//div[@class="bd"]/p/text()').extract()[1].lstrip().rstrip()
            yield item

        next_page = response.xpath('//span[@class="next"]/a/@href')
        if next_page:
            url = response.urljoin(next_page.extract_first())
            yield scrapy.Request(url, self.parse)
