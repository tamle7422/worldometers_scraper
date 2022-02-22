# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os,re
from sys import platform
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from .items import NowCoronaItem,YesterdayCoronaItem
from datetime import datetime

class CoronavirusPipeline:
    def __init__(self):
        self.nowCoronaDir = "csv_files/virus/now"
        self.yesterdayCoronaDir = "csv_files/virus/yesterday"
        self.nowCoronaList = ["nowRank","nowCountry","nowTotalCases","nowNewCases","nowTotalDeaths","nowNewDeaths", \
            "nowTotalRecovered","nowNewRecovered","nowActiveCases","nowSeriousCritical","nowCasesPerMillion", \
            "nowDeathsPerMillion","nowTotalTests","nowTestsPerMillion","nowPopulation"]
        self.yesterdayCoronaList = ["yesterdayRank","yesterdayCountry","yesterdayTotalCases","yesterdayNewCases", \
            "yesterdayTotalDeaths","yesterdayNewDeaths","yesterdayTotalRecovered","yesterdayNewRecovered", \
            "yesterdayActiveCases","yesterdaySeriousCritical","yesterdayCasesPerMillion","yesterdayDeathsPerMillion", \
            "yesterdayTotalTests","yesterdayTestsPerMillion","yesterdayPopulation"]

        self.nowCoronaWriter = ""
        self.yesterdayCoronaWriter = ""

        self.nowCoronaFileName = ""
        self.yesterdayCoronaFileName = ""

        self.nowCoronaExporter = ""
        self.yesterdayCoronaExporter = ""

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

        self.nowCoronaFileName = "now_corona_" + self.checkMonthDay(dt.month) + "_" + self.checkMonthDay(dt.day) + "_" \
            + str(dt.year) + ".csv"
        self.yesterdayCoronaFileName = "yesterday_corona_" + self.checkMonthDay(dt.month) + "_" + self.checkMonthDay(dt.day) + "_" \
            + str(dt.year) + ".csv"

        absolutePathNowCorona = os.path.join(os.getcwd(),self.nowCoronaDir)
        absolutePathYesterdayCorona = os.path.join(os.getcwd(),self.yesterdayCoronaDir)

        self.nowCoronaWriter = open(os.path.join(absolutePathNowCorona,self.nowCoronaFileName),"wb+")
        self.yesterdayCoronaWriter = open(os.path.join(absolutePathYesterdayCorona,self.yesterdayCoronaFileName),"wb+")

        self.nowCoronaExporter = CsvItemExporter(self.nowCoronaWriter)
        self.yesterdayCoronaExporter = CsvItemExporter(self.yesterdayCoronaWriter)

        self.nowCoronaExporter.fields_to_export = self.nowCoronaList
        self.yesterdayCoronaExporter.fields_to_export = self.yesterdayCoronaList

        self.nowCoronaExporter.start_exporting()
        self.yesterdayCoronaExporter.start_exporting()

    def spider_closed(self,spider):
        self.nowCoronaExporter.finish_exporting()
        self.yesterdayCoronaExporter.finish_exporting()

        self.nowCoronaWriter.close()
        self.yesterdayCoronaWriter.close()

    def process_item(self,item,spider):
        if (isinstance(item,NowCoronaItem)):
            if (len(item) == 0):
                return item
            else:
                self.nowCoronaExporter.export_item(item)
                return item
        elif (isinstance(item,YesterdayCoronaItem)):
            if (len(item) == 0):
                return item
            else:
                self.yesterdayCoronaExporter.export_item(item)
                return item

    def checkMonthDay(self,dayOrMonth):
        if (int(dayOrMonth) <= 9):
            concatStr = "0" + str(dayOrMonth)
            return concatStr
        else:
            return str(dayOrMonth)