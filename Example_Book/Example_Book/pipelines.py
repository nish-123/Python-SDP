# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import Workbook

class ExampleBookPipeline:
    def open_spider(self,spider):
        self.workbook=Workbook()
        self.sheet=self.workbook.active
        self.sheet.title='Example_Book'
        self.sheet.append(spider.cols)
        
    def process_item(self,item, spider):
        self.sheet.append([item['title'], item['price']])
        return item
    def close_spider(self,spider):
        self.workbook.save('Example_Book.xlsx')