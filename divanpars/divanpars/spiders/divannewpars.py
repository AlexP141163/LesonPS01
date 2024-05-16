import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lihgts = response.css('div._Ud0k')
        for lihgt in lihgts:
            yield {
                'name' :  lihgt.css('div.lsooF span::text').get(),
                'price' :  lihgt.css('div.pY3d2 span::text').get(),
                'url' : lihgt.css('a').attrib['href']
            }
