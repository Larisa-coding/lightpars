import scrapy


class LightnewparsSpider(scrapy.Spider):
    name = "lightnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru"]

    def parse(self, response):
        pass
