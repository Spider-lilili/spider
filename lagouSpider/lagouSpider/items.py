# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouspiderItem(scrapy.Item):
    company = scrapy.Field()  # 招聘公司名字
    job_name = scrapy.Field()  # 工作名字
    address = scrapy.Field()  # 工作地址
    job_Descriptions = scrapy.Field()  # 工作描述
    Position_temptation = scrapy.Field()  # 工作诱惑
    salary = scrapy.Field()  # 工资


