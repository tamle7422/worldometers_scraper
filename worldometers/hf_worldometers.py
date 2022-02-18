import re
import pickle
from datetime import datetime
from scrapy.loader import ItemLoader
from .items import CoronaItem

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

def loadCoronaItem(self,response):
    self.nowRank = self.nowRank if (self.nowRank != "") else "None"
    self.nowCountry = self.nowCountry if (self.nowCountry != "") else "None"
    self.nowTotalCases = self.nowTotalCases if (self.nowTotalCases != "") else "None"
    self.nowNewCases = self.nowNewCases if (self.nowNewCases != "") else "None"
    self.nowTotalDeaths = self.nowTotalDeaths if (self.nowTotalDeaths != "") else "None"
    self.nowNewDeaths = self.nowNewDeaths if (self.nowNewDeaths != "") else "None"
    self.nowTotalRecovered = self.nowTotalRecovered if (self.nowTotalRecovered != "") else "None"
    self.nowNewRecovered = self.nowNewRecovered if (self.nowNewRecovered != "") else "None"
    self.nowActiveCases = self.nowActiveCases if (self.nowActiveCases != "") else "None"
    self.nowSeriousCritical = self.nowSeriousCritical if (self.nowSeriousCritical != "") else "None"
    self.nowCasesPerMillion = self.nowCasesPerMillion if (self.nowCasesPerMillion != "") else "None"
    self.nowDeathsPerMillion = self.nowDeathsPerMillion if (self.nowDeathsPerMillion != "") else "None"
    self.nowTotalTests = self.nowTotalTests if (self.nowTotalTests != "") else "None"
    self.nowTestsPerMillion = self.nowTestsPerMillion if (self.nowTestsPerMillion != "") else "None"
    self.nowPopulation = self.nowPopulation if (self.nowPopulation != "") else "None"

    loader = ItemLoader(item=CoronaItem(),response=response)
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


def checkEmpty(data):
    if (data == None or len(data) == 0):
        data = "None"
        return data
    else:
        return data