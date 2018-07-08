import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from first.items import FirstItem
import json


class Myspider(scrapy.Spider):
    name ='first'
    
    def start_requests(self):
        url1='http://quote.eastmoney.com/stocklist.html'
        yield Request(url1,callback=self.get_code)

    def get_code(self,response):
        a=BeautifulSoup(response.text)
        for a in a.find_all('a'):
            gpdm=a.get_text()[len(a.get_text())-7:len(a.get_text())-1]
            url='http://data.eastmoney.com/DataCenter_V3/gdhs/GetDetial.ashx?code='+gpdm
            yield Request(url,self.parse)       
    
    def parse(self,response):
        item=FirstItem()
        if json.loads(response.text)['pages']==0:
            pass
        else:
            item['dm']=response.url[len(response.url)-6:]
            item['data']=json.loads(response.text)['data']
        return item
        
