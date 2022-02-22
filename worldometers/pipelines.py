# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os,re
from sys import platform
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from .items import NowCoronaItem
from datetime import datetime

class CoronavirusPipeline:
    def __init__(self):
        self.coronaDir = "csv_files/virus"
        self.coronaList = ["nowRank","nowCountry","nowTotalCases","nowNewCases","nowTotalDeaths","nowNewDeaths", \
            "nowTotalRecovered","nowNewRecovered","nowActiveCases","nowSeriousCritical","nowCasesPerMillion", \
            "nowDeathsPerMillion","nowTotalTests","nowTestsPerMillion","nowPopulation"]

        self.coronaWriter = ""
        self.coronaFileName = ""
        self.coronaExporter = ""

    @classmethod
    def from_crawler(cls,crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened,signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed,signals.spider_closed)
        return pipeline

    def spider_opened(self,spider):
        # check system; change if on windows
        if (platform != "linux"):
            self.coronaDir = "csv_files\\virus"

        today = datetime.today()
        dt = datetime(today.year,today.month,today.day)

        self.coronaFileName = "now_corona_" + self.checkMonthDay(dt.month) + "_" + self.checkMonthDay(dt.day) + "_" \
            + str(dt.year) + ".csv"

        absolutePathCorona = os.path.join(os.getcwd(),self.coronaDir)

        self.coronaWriter = open(os.path.join(absolutePathCorona,self.coronaFileName),"wb+")
        self.coronaExporter = CsvItemExporter(self.coronaWriter)
        self.coronaExporter.fields_to_export = self.coronaList
        self.coronaExporter.start_exporting()

    def spider_closed(self,spider):
        self.coronaExporter.finish_exporting()
        self.coronaWriter.close()

    def process_item(self,item,spider):
        if (isinstance(item,NowCoronaItem)):
            if (len(item) == 0):
                return item
            else:
                self.coronaExporter.export_item(item)
                return item

    def checkMonthDay(self,dayOrMonth):
        if (int(dayOrMonth) <= 9):
            concatStr = "0" + str(dayOrMonth)
            return concatStr
        else:
            return str(dayOrMonth)