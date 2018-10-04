import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ['docs.python.org']
    start_urls = [
        'https://docs.python.org/3/',
        'https://docs.python.org/3/reference/index.html'
        ]
    def parse(self,response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//ul/li/ul/li/a/@href').extract()
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = "https://docs.python.org/3/reference/"+site
            items.append(item)

        return items
		
