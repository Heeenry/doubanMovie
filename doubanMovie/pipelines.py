# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook


class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        return item


class doubanPipeline(object):  # 设置工序一
    wb = Workbook()
    ws = wb.active
    ws.append(['排名', '片名', '评分', '评论数', '类型','可播放？', '链接', 'quote'])  # 设置表头
    #ws.append(['rank'], ['title'])

    def process_item(self, item, spider):  # 工序具体内容
        line = [item['rank'], item['title'], item['rate'],item['pl'],
                item['type'], item['playable'], item['link'], item['quote']]  # 把数据中每一项整理出来
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('/home/henry/spiders/doubanMovie/movieList.xlsx')  # 保存xlsx文件
        return item

