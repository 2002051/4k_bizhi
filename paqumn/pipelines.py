# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request
import os
# os.mkdir()


# 写入excel的管道
class PaqumnPipeline:
    sum1 = 0  #记录每一页的图片数  #"E:\86178\tp"
    page = 1 #记录第几页即第几个文件夹
    fn = f"第1页图片\\"
    def process_item(self, item, spider):  # 每次传过来一个对象，此方法就之执行一次,每个对象其实就对应一个图片
        name = str(item.get('jpg_name'))
        url = item.get("jpg_url")

        if self.sum1==0:   # 检测到图片满20了就新建一个文件夹
            self.fn = f"第{self.page}页图片\\"
            os.mkdir(f"E:\86178\图片\{self.fn}")
        urllib.request.urlretrieve(url=url, filename="E:\86178\图片\\"+ self.fn + name + ".jpg")
        self.sum1 += 1
        if self.sum1 == 20:  # 检测到图片满20，然后就归零。
            self.sum1 = 0
            self.page += 1

        return item


