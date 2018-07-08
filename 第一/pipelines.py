# -*- coding: utf-8 -*-
import sqlite3
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstPipeline(object):
    def open_spider(self,spider):
        self.conn=sqlite3.connect('gd.db')
        self.c=self.conn.cursor()
        try:
            self.c.execute('''create table gp
    (id text ,
    历史次数 int ,
    本次股东户数 text ,
    上次股东户数 text ,
    增减股东户数 text ,
    增减比例百分比 text ,
    区间涨跌幅百分比 text ,
    统计截止日 text ,
    户均持股值 text ,
    户均持股数 text ,
    总市值 text ,
    总股本 text,
    公告日期 text,
    股本变动 text,
    变动原因 text,
    收盘价格 text);''')
        except:
            pass
    
        
    def process_item(self, item, spider):
        data=item['data']
        dm=item['dm']
        urll=(dm,)
        xx=''
        try:
            a=self.c.execute('select id from gp where id=?',urll)
            for i in a:
                xx=i[0]
                break
        except:
            pass
        if xx==dm:
            print('已经保存过了\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        else:
            for x in range(len(data)):
                list=(dm,x,data[x]['HolderNum'],data[x]['PreviousHolderNum'],data[x]['HolderNumChange'],data[x]['HolderNumChangeRate'],data[x]['RangeChangeRate'],data[x]['EndDate'],data[x]['HolderAvgCapitalisation'],data[x]['HolderAvgStockQuantity'],data[x]['TotalCapitalisation'],data[x]['CapitalStock'],data[x]['NoticeDate'],data[x]['CapitalStockChange'],data[x]['CapitalStockChangeEvent'],data[x]['ClosePrice'])
                self.c.execute('insert into gp values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',list)
                self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()

