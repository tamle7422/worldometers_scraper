# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os,re
from sys import platform
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from .items import CoronavirusCurrItem,CoronavirusYestItem,Coronavirus2DaysItem,PopulationItem
from datetime import datetime

class CoronavirusPipeline:
    def __init__(self):
        self.currentDir = "csv_files/coronavirus/current"
        self.yesterdayDir = "csv_files/coronavirus/yesterday"
        self.twoDaysDir = "csv_files/coronavirus/two_days"

        self.currentList = ["rankCurr","countryCurr","totalCasesCurr","newCasesCurr","totalDeathsCurr","newDeathsCurr", \
            "totalRecoveredCurr","newRecoveredCurr","activeCasesCurr","seriousCriticalCurr","casesPerMillionCurr", \
            "deathsPerMillionCurr","totalTestsCurr","testsPerMillionCurr","populationCurr"]
        self.yesterdayList = ["rankYest","countryYest","totalCasesYest","newCasesYest","totalDeathsYest","newDeathsYest", \
            "totalRecoveredYest","newRecoveredYest","activeCasesYest","seriousCriticalYest","casesPerMillionYest", \
            "deathsPerMillionYest","totalTestsYest","testsPerMillionYest","populationYest"]
        self.twoDaysList = ["rank2Days","country2Days","totalCases2Days","newCases2Days","totalDeaths2Days","newDeaths2Days", \
            "totalRecovered2Days","newRecovered2Days","activeCases2Days","seriousCritical2Days","casesPerMillion2Days", \
            "deathsPerMillion2Days","totalTests2Days","testsPerMillion2Days","population2Days"]

        self.currentWriter = ""
        self.yesterdayWriter = ""
        self.twoDaysWriter = ""

        self.currentFileName = ""
        self.yesterdayFileName = ""
        self.twoDaysFileName = ""

        self.currentExporter = ""
        self.yesterdayExporter = ""
        self.twoDaysExporter = ""

    @classmethod
    def from_crawler(cls,crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened,signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed,signals.spider_closed)
        return pipeline

    def spider_opened(self,spider):
        # check system; change if on windows
        if (platform != "linux"):
            self.coronaDir = "csv_files\\coronavirus"

        today = datetime.today()
        dt = datetime(today.year,today.month,today.day)

        self.currentFileName = "coronavirus_current_" + self.checkMonthDay(dt.month) + "_" + self.checkMonthDay(dt.day) + "_" \
            + str(dt.year) + ".csv"
        self.yesterdayFileName = "coronavirus_yesterday_" + self.checkMonthDay(dt.month) + "_" \
            + self.checkMonthDay(dt.day) + "_" + str(dt.year) + ".csv"
        self.twoDaysFileName = "coronavirus_2_days_" + self.checkMonthDay(dt.month) + "_" + self.checkMonthDay(dt.day) \
            + "_" + str(dt.year) + ".csv"

        absolutePathCurrent = os.path.join(os.getcwd(),self.currentDir)
        absolutePathYesterday = os.path.join(os.getcwd(),self.yesterdayDir)
        absolutePathTwoDays = os.path.join(os.getcwd(),self.twoDaysDir)

        self.currentWriter = open(os.path.join(absolutePathCurrent,self.currentFileName),"wb+")
        self.yesterdayWriter = open(os.path.join(absolutePathYesterday,self.yesterdayFileName),"wb+")
        self.twoDaysWriter = open(os.path.join(absolutePathTwoDays,self.twoDaysFileName),"wb+")

        self.currentExporter = CsvItemExporter(self.currentWriter)
        self.yesterdayExporter = CsvItemExporter(self.yesterdayWriter)
        self.twoDaysExporter = CsvItemExporter(self.twoDaysWriter)

        self.currentExporter.fields_to_export = self.currentList
        self.yesterdayExporter.fields_to_export = self.yesterdayList
        self.twoDaysExporter.fields_to_export = self.twoDaysList

        self.currentExporter.start_exporting()
        self.yesterdayExporter.start_exporting()
        self.twoDaysExporter.start_exporting()

    def spider_closed(self,spider):
        self.currentExporter.finish_exporting()
        self.yesterdayExporter.finish_exporting()
        self.twoDaysExporter.finish_exporting()

        self.currentWriter.close()
        self.yesterdayWriter.close()
        self.twoDaysWriter.close()

    def process_item(self,item,spider):
        if (isinstance(item,CoronavirusCurrItem)):
            if (len(item) == 0):
                return item
            else:
                self.currentExporter.export_item(item)
                return item
        elif (isinstance(item,CoronavirusYestItem)):
            if (len(item) == 0):
                return item
            else:
                self.yesterdayExporter.export_item(item)
                return item
        elif (isinstance(item,Coronavirus2DaysItem)):
            if (len(item) == 0):
                return item
            else:
                self.twoDaysExporter.export_item(item)
                return item

    def checkMonthDay(self,dayOrMonth):
        if (int(dayOrMonth) <= 9):
            concatStr = "0" + str(dayOrMonth)
            return concatStr
        else:
            return str(dayOrMonth)

class PopulationPipeline:
    def __init__(self):
        self.populationDir = "csv_files/population"
        self.populationList = ["country","population","yearlyChange","netChange","density","landArea", \
            "migrants","fertilizationRate","medianAge","urbanPopPercent","worldShare"]

        self.populationWriter = ""
        self.populationFileName = ""
        self.populationExporter = ""

    @classmethod
    def from_crawler(cls,crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened,signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed,signals.spider_closed)
        return pipeline

    def spider_opened(self,spider):
        # check system; change if on windows
        if (platform != "linux"):
            self.populationDir = "csv_files\\population"

        today = datetime.today()
        dt = datetime(today.year,today.month,today.day)

        self.populationFileName = "population_" + self.checkMonthDay(dt.month) + "_" + self.checkMonthDay(dt.day) + "_" \
            + str(dt.year) + ".csv"

        absolutePathPopulation = os.path.join(os.getcwd(),self.populationDir)

        self.populationWriter = open(os.path.join(absolutePathPopulation,self.populationFileName),"wb+")
        self.populationExporter = CsvItemExporter(self.populationWriter)
        self.populationExporter.fields_to_export = self.populationList
        self.populationExporter.start_exporting()

    def spider_closed(self,spider):
        self.populationExporter.finish_exporting()
        self.populationWriter.close()

    def process_item(self,item,spider):
        if (isinstance(item,PopulationItem)):
            if (len(item) == 0):
                return item
            else:
                self.populationExporter.export_item(item)
                return item

    def checkMonthDay(self,dayOrMonth):
        if (int(dayOrMonth) <= 9):
            concatStr = "0" + str(dayOrMonth)
            return concatStr
        else:
            return str(dayOrMonth)