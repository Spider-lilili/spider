# -*- coding: utf-8 -*-
# Created : 2018/8/26 18:33
# author ：GuoLi

from lxml import etree,html
import scrapy
from lagouSpider.items import LagouspiderItem

class lagouSpider(scrapy.Spider):
    #爬虫名
    name = 'lagou'
    #允许爬虫作用域
    allowd_domains = ['https://www.lagou.com/']
    current_num = 1
    page = 0
    url = 'https://www.lagou.com/zhaopin/Python/'
    start_urls = [url+str(current_num)]

    def parse(self, response):
        total_page = response.xpath("//div[@class='page-number']/span[@class='span totalNum']/text()").extract()[0]
        # for current_num in range(int(total_page)):
        if self.page < int(total_page) + 1:
            self.page += 1
        yield scrapy.Request(url=self.url + str(self.page), callback=self.parse)
    # def parse_url(self,response):
        links = response.xpath("//div[@class='list_item_top']/div[@class='position']/div[@class='p_top']/a/@href").extract()
        for link in links:
            try:
                yield scrapy.Request(url=link, callback=self.parse_info)
            except Exception as e:
                yield scrapy.Request(url=link, callback=self.parse_info)

    def parse_info(self,response):
        item = LagouspiderItem()
        #公司名称
        item['company'] = response.xpath("//div[@class='job-name']/div[@class='company']/text()").extract()[0]
        # print(company)
        #职位名称
        item['job_name'] = response.xpath("//div[@class='job-name']/span[@class='name']/text()").extract()
        #工作地址
        address_1 = response.xpath("//div[@class='work_addr']/a/text()").extract()[0]
        # address_2 = response.xpath("//div[@class='work_addr']/a[2]/text()").extract()[0]
        # address_3 = response.xpath("//div[@class='work_addr']/a[3]/text()").extract()[0]
        address_4 = response.xpath("//dl[@class='job_detail']/dd[@class='job-address clearfix']/input[3]/@value").extract()[0]
        # print(address_1,address_2,address_3,address_4)
        item['address'] = address_1 + address_4
        #工作描述
        # job_Descriptions = response.xpath("//").extract()[0]
        #职位诱惑
        # Position_temptation = response.xpath("//").extract()[0]
        #工资
        item['salary'] = response.xpath("//dd[@class='job_request']/p/span[@class='salary']/text()").extract()[0]
        yield item
