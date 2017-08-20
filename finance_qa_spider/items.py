# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinanceQaSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QAItem(scrapy.Item):
    user_name = scrapy.Field() #用户名
    company_name = scrapy.Field() #提问的公司名
    company_id = scrapy.Field() #公司ID
    question_time = scrapy.Field() #提问时间
    question_content = scrapy.Field() #提问内容
    answer_time = scrapy.Field() #回答时间
    answer_content = scrapy.Field() #回答内容
    
    