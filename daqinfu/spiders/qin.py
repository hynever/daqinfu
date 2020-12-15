# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import QinItem

class QinSpider(scrapy.Spider):
    name = 'qin'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/subject/26413293/comments?start=0&limit=20']
    domain = "https://movie.douban.com/subject/26413293/comments"

    def parse(self, response):
        comment_items = response.xpath("//div[@id='comments']/div[contains(@class,'comment-item')]")
        for comment_item in comment_items:
            pub_time = comment_item.xpath(".//span[contains(@class,'comment-time')]/@title").extract_first()
            rating_classes = comment_item.xpath(".//span[contains(@class,'rating')]/@class").extract_first()
            rating = re.search(r'allstar(\d)0 rating',rating_classes).group(1)
            content = comment_item.xpath(".//p[contains(@class,'comment-content')]/span/text()").extract_first()
            item = QinItem(pub_time=pub_time,rating=rating,content=content)
            yield item

        query = response.xpath("//div[@id='paginator']/a[@class='next']/@href").extract_first()
        if query:
            yield scrapy.Request(url=self.domain+query,callback=self.parse)
            print("="*40)
            print(response.url,query)
            print("=" * 40)