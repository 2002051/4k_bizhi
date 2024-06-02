import scrapy
from paqumn.items import PaqumnItem  # 此处报错不是语法问题不影响框架的运行

# /uploads/allimg/230723/002300-16900429808745.jpg
class MnSpider(scrapy.Spider):
    name = "mn"
    allowed_domains = ["pic.netbian.com"]
    start_urls = ["https://pic.netbian.com/4kmeinv/"]
    page = 1


    def parse(self, response,**kwargs):
        basic_url = response.xpath('//div[@class = "slist"]/ul/li')  # 基础url，对其再次使用xpath即可索引到想要的内容

        for li in basic_url:
            name = li.xpath('.//@alt').extract_first()
            src = li.xpath('.//@src').extract_first()
            url = 'https://pic.netbian.com' + src
            meinv = PaqumnItem(jpg_name=name, jpg_url=url)  # 一个对象代表的是一张图片，分别具有其名字和下载链接

            yield meinv  # 将对象传给管道下载和保存
        # https://pic.netbian.com/4kmeinv/index_2.html
        # https://pic.netbian.com/4kmeinv/index_3.html
        # https://pic.netbian.com/4kmeinv/index_4.html
        if self.page < 5:  # 页面随便设置
            self.page += 1
            url = f'https://pic.netbian.com/4kmeinv/index_{self.page}.html'  # 新页面的网址
            #             怎么去调用parse方法
            #             scrapy.Request就是scrpay的get请求
            #             url就是请求地址
            #             callback是你要执行的那个函数  注意不需要加（）
            yield scrapy.Request(url=url, callback=self.parse)  # 返回请的请求对象，和下一页url作为url闯入parse方法，再执行一次parse方法
