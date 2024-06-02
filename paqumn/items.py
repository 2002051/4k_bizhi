# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaqumnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jpg_name = scrapy.Field()   # 图片名字
    jpg_url = scrapy.Field()    # 图片路径
