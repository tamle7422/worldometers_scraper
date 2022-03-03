import re
import pickle
from datetime import datetime
from scrapy.loader import ItemLoader
from .items import NowCoronaItem,YesterdayCoronaItem,TwoDaysCoronaItem

def getTime():
    now = datetime.now()
    currentDate = now.strftime("%m_%d_%y")
    return currentDate

def setNowTotalCases(self,nowTotalCases):
    try:
        if (nowTotalCases != "None"):
            self.nowTotalCases = nowTotalCases.replace(",","")
        else:
            self.nowTotalCases = "None"

    except Exception as ex:
        print("exception => error setting now total cases --- {0}".format(ex))
        self.nowTotalCases = "None"

def setNowNewCases(self,nowNewCases):
    try:
        if (nowNewCases != "None"):
            self.nowNewCases = re.sub(r"[^0-9]","",nowNewCases)
        else:
            self.nowNewCases = "None"

    except Exception as ex:
        print("exception => error setting now new cases --- {0}".format(ex))
        self.nowNewCases = "None"

def setNowTotalDeaths(self,nowTotalDeaths):
    try:
        if (nowTotalDeaths != "None"):
            self.nowTotalDeaths = nowTotalDeaths.replace(",","")
        else:
            self.nowTotalDeaths = "None"

    except Exception as ex:
        print("exception => error setting now total deaths --- {0}".format(ex))
        self.nowTotalDeaths = "None"

def setNowNewDeaths(self,nowNewDeaths):
    try:
        if (nowNewDeaths != "None"):
            self.nowNewDeaths = re.sub(r"[^0-9]","",nowNewDeaths)
        else:
            self.nowNewDeaths = "None"

    except Exception as ex:
        print("exception => error setting now new deaths --- {0}".format(ex))
        self.nowNewDeaths = "None"

def setNowTotalRecovered(self,nowTotalRecovered):
    try:
        if (nowTotalRecovered != "None"):
            self.nowTotalRecovered = nowTotalRecovered.replace(",","")
        else:
            self.nowTotalRecovered = "None"

    except Exception as ex:
        print("exception => error setting now total recovered --- {0}".format(ex))
        self.nowTotalRecovered = "None"

def setNowNewRecovered(self,nowNewRecovered):
    try:
        if (nowNewRecovered != "None"):
            self.nowNewRecovered = re.sub(r"[^0-9]","",nowNewRecovered)
        else:
            self.nowNewRecovered = "None"

    except Exception as ex:
        print("exception => error setting now new recovered --- {0}".format(ex))
        self.nowNewRecovered = "None"

def setNowActiveCases(self,nowActiveCases):
    try:
        if (nowActiveCases != "None"):
            self.nowActiveCases = re.sub(r"[^0-9]","",nowActiveCases)
        else:
            self.nowActiveCases = "None"

    except Exception as ex:
        print("exception => error setting now active cases recovered --- {0}".format(ex))
        self.nowActiveCases = "None"

# dynamic assignment
def setValue(self,value,type):
    try:
        if (value != "None"):
            setattr(self,type,re.sub(r"[^0-9]","",value))
        else:
            setattr(self,type,"None")

    except Exception as ex:
        print("exception => error setting {0} --- {1}".format(type,ex))
        setattr(self,type,"None")

def loadNowCoronaItem(self,response):
    self.nowRank = self.nowRank if (len(self.nowRank) != 0) else "None"
    self.nowCountry = self.nowCountry if (len(self.nowCountry) != 0) else "None"
    self.nowTotalCases = self.nowTotalCases if (len(self.nowTotalCases) != 0) else "None"
    self.nowNewCases = self.nowNewCases if (len(self.nowNewCases) != 0) else "None"
    self.nowTotalDeaths = self.nowTotalDeaths if (len(self.nowTotalDeaths) != 0) else "None"
    self.nowNewDeaths = self.nowNewDeaths if (len(self.nowNewDeaths) != 0) else "None"
    self.nowTotalRecovered = self.nowTotalRecovered if (len(self.nowTotalRecovered) != 0) else "None"
    self.nowNewRecovered = self.nowNewRecovered if (len(self.nowNewRecovered) != 0) else "None"
    self.nowActiveCases = self.nowActiveCases if (len(self.nowActiveCases) != 0) else "None"
    self.nowSeriousCritical = self.nowSeriousCritical if (len(self.nowSeriousCritical) != 0) else "None"
    self.nowCasesPerMillion = self.nowCasesPerMillion if (len(self.nowCasesPerMillion) != 0) else "None"
    self.nowDeathsPerMillion = self.nowDeathsPerMillion if (len(self.nowDeathsPerMillion) != 0) else "None"
    self.nowTotalTests = self.nowTotalTests if (len(self.nowTotalTests) != 0) else "None"
    self.nowTestsPerMillion = self.nowTestsPerMillion if (len(self.nowTestsPerMillion) != 0) else "None"
    self.nowPopulation = self.nowPopulation if (len(self.nowPopulation) != 0) else "None"

    loader = ItemLoader(item=NowCoronaItem(),response=response)
    loader.add_value("nowRank",self.nowRank)
    loader.add_value("nowCountry",self.nowCountry)
    loader.add_value("nowTotalCases",self.nowTotalCases)
    loader.add_value("nowNewCases",self.nowNewCases)
    loader.add_value("nowTotalDeaths",self.nowTotalDeaths)
    loader.add_value("nowNewDeaths",self.nowNewDeaths)
    loader.add_value("nowTotalRecovered",self.nowTotalRecovered)
    loader.add_value("nowNewRecovered",self.nowNewRecovered)
    loader.add_value("nowActiveCases",self.nowActiveCases)
    loader.add_value("nowSeriousCritical",self.nowSeriousCritical)
    loader.add_value("nowCasesPerMillion",self.nowCasesPerMillion)
    loader.add_value("nowDeathsPerMillion",self.nowDeathsPerMillion)
    loader.add_value("nowTotalTests",self.nowTotalTests)
    loader.add_value("nowTestsPerMillion",self.nowTestsPerMillion)
    loader.add_value("nowPopulation",self.nowPopulation)
    return loader

def loadYesterdayCoronaItem(self,response):
    self.yesterdayRank = self.yesterdayRank if (len(self.yesterdayRank) != 0) else "None"
    self.yesterdayCountry = self.yesterdayCountry if (len(self.yesterdayCountry) != 0) else "None"
    self.yesterdayTotalCases = self.yesterdayTotalCases if (len(self.yesterdayTotalCases) != 0) else "None"
    self.yesterdayNewCases = self.yesterdayNewCases if (len(self.yesterdayNewCases) != 0) else "None"
    self.yesterdayTotalDeaths = self.yesterdayTotalDeaths if (len(self.yesterdayTotalDeaths) != 0) else "None"
    self.yesterdayNewDeaths = self.yesterdayNewDeaths if (len(self.yesterdayNewDeaths) != 0) else "None"
    self.yesterdayTotalRecovered = self.yesterdayTotalRecovered if (len(self.yesterdayTotalRecovered) != 0) else "None"
    self.yesterdayNewRecovered = self.yesterdayNewRecovered if (len(self.yesterdayNewRecovered) != 0) else "None"
    self.yesterdayActiveCases = self.yesterdayActiveCases if (len(self.yesterdayActiveCases) != 0) else "None"
    self.yesterdaySeriousCritical = self.yesterdaySeriousCritical if (len(self.yesterdaySeriousCritical) != 0) else "None"
    self.yesterdayCasesPerMillion = self.yesterdayCasesPerMillion if (len(self.yesterdayCasesPerMillion) != 0) else "None"
    self.yesterdayDeathsPerMillion = self.yesterdayDeathsPerMillion if (len(self.yesterdayDeathsPerMillion) != 0) else "None"
    self.yesterdayTotalTests = self.yesterdayTotalTests if (len(self.yesterdayTotalTests) != 0) else "None"
    self.yesterdayTestsPerMillion = self.yesterdayTestsPerMillion if (len(self.yesterdayTestsPerMillion) != 0) else "None"
    self.yesterdayPopulation = self.yesterdayPopulation if (len(self.yesterdayPopulation) != 0) else "None"

    loader = ItemLoader(item=YesterdayCoronaItem(),response=response)
    loader.add_value("yesterdayRank",self.yesterdayRank)
    loader.add_value("yesterdayCountry",self.yesterdayCountry)
    loader.add_value("yesterdayTotalCases",self.yesterdayTotalCases)
    loader.add_value("yesterdayNewCases",self.yesterdayNewCases)
    loader.add_value("yesterdayTotalDeaths",self.yesterdayTotalDeaths)
    loader.add_value("yesterdayNewDeaths",self.yesterdayNewDeaths)
    loader.add_value("yesterdayTotalRecovered",self.yesterdayTotalRecovered)
    loader.add_value("yesterdayNewRecovered",self.yesterdayNewRecovered)
    loader.add_value("yesterdayActiveCases",self.yesterdayActiveCases)
    loader.add_value("yesterdaySeriousCritical",self.yesterdaySeriousCritical)
    loader.add_value("yesterdayCasesPerMillion",self.yesterdayCasesPerMillion)
    loader.add_value("yesterdayDeathsPerMillion",self.yesterdayDeathsPerMillion)
    loader.add_value("yesterdayTotalTests",self.yesterdayTotalTests)
    loader.add_value("yesterdayTestsPerMillion",self.yesterdayTestsPerMillion)
    loader.add_value("yesterdayPopulation",self.yesterdayPopulation)
    return loader

def loadTwoDaysCoronaItem(self,response):
    self.twoDaysRank = self.twoDaysRank if (len(self.twoDaysRank) != 0) else "None"
    self.twoDaysCountry = self.twoDaysCountry if (len(self.twoDaysCountry) != 0) else "None"
    self.twoDaysTotalCases = self.twoDaysTotalCases if (len(self.twoDaysTotalCases) != 0) else "None"
    self.twoDaysNewCases = self.twoDaysNewCases if (len(self.twoDaysNewCases) != 0) else "None"
    self.twoDaysTotalDeaths = self.twoDaysTotalDeaths if (len(self.twoDaysTotalDeaths) != 0) else "None"
    self.twoDaysNewDeaths = self.twoDaysNewDeaths if (len(self.twoDaysNewDeaths) != 0) else "None"
    self.twoDaysTotalRecovered = self.twoDaysTotalRecovered if (len(self.twoDaysTotalRecovered) != 0) else "None"
    self.twoDaysNewRecovered = self.twoDaysNewRecovered if (len(self.twoDaysNewRecovered) != 0) else "None"
    self.twoDaysActiveCases = self.twoDaysActiveCases if (len(self.twoDaysActiveCases) != 0) else "None"
    self.twoDaysSeriousCritical = self.twoDaysSeriousCritical if (len(self.twoDaysSeriousCritical) != 0) else "None"
    self.twoDaysCasesPerMillion = self.twoDaysCasesPerMillion if (len(self.twoDaysCasesPerMillion) != 0) else "None"
    self.twoDaysDeathsPerMillion = self.twoDaysDeathsPerMillion if (len(self.twoDaysDeathsPerMillion) != 0) else "None"
    self.twoDaysTotalTests = self.twoDaysTotalTests if (len(self.twoDaysTotalTests) != 0) else "None"
    self.twoDaysTestsPerMillion = self.twoDaysTestsPerMillion if (len(self.twoDaysTestsPerMillion) != 0) else "None"
    self.twoDaysPopulation = self.twoDaysPopulation if (len(self.twoDaysPopulation) != 0) else "None"

    loader = ItemLoader(item=TwoDaysCoronaItem(),response=response)
    loader.add_value("twoDaysRank",self.twoDaysRank)
    loader.add_value("twoDaysCountry",self.twoDaysCountry)
    loader.add_value("twoDaysTotalCases",self.twoDaysTotalCases)
    loader.add_value("twoDaysNewCases",self.twoDaysNewCases)
    loader.add_value("twoDaysTotalDeaths",self.twoDaysTotalDeaths)
    loader.add_value("twoDaysNewDeaths",self.twoDaysNewDeaths)
    loader.add_value("twoDaysTotalRecovered",self.twoDaysTotalRecovered)
    loader.add_value("twoDaysNewRecovered",self.twoDaysNewRecovered)
    loader.add_value("twoDaysActiveCases",self.twoDaysActiveCases)
    loader.add_value("twoDaysSeriousCritical",self.twoDaysSeriousCritical)
    loader.add_value("twoDaysCasesPerMillion",self.twoDaysCasesPerMillion)
    loader.add_value("twoDaysDeathsPerMillion",self.twoDaysDeathsPerMillion)
    loader.add_value("twoDaysTotalTests",self.twoDaysTotalTests)
    loader.add_value("twoDaysTestsPerMillion",self.twoDaysTestsPerMillion)
    loader.add_value("twoDaysPopulation",self.twoDaysPopulation)
    return loader

def checkEmpty(data):
    if (data == None or len(data) == 0):
        data = "None"
        return data
    else:
        return data