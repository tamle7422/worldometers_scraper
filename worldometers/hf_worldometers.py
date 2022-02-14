import re
from datetime import datetime

def getTime():
    now = datetime.now()
    currentDate = now.strftime("%m_%d_%y")
    return currentDate


def setNowTotalCases(self,nowTotalCases):
    try:
        if (nowTotalCases != "None"):
            self.nowTotalCases = int(nowTotalCases.replace(",",""))
        else:
            self.nowTotalCases = "None"

    except Exception as ex:
        print("exception => error setting now total cases --- {0}".format(ex))
        self.nowTotalCases = "None"

def setNowNewCases(self,nowNewCases):
    try:
        if (nowNewCases != "None"):
            self.nowNewCases = int(nowNewCases.replace(",",""))
        else:
            self.nowNewCases = "None"

    except Exception as ex:
        print("exception => error setting now new cases --- {0}".format(ex))
        self.nowNewCases = "None"

def setNowTotalDeaths(self,nowTotalDeaths):
    try:
        if (nowTotalDeaths != "None"):
            self.nowTotalDeaths = int(nowTotalDeaths.replace(",",""))
        else:
            self.nowTotalDeaths = "None"

    except Exception as ex:
        print("exception => error setting now total deaths --- {0}".format(ex))
        self.nowTotalDeaths = "None"

def setNowNewDeaths(self,nowNewDeaths):
    try:
        if (nowNewDeaths != "None"):
            self.nowNewDeaths = int(re.sub(r"[^0-9]","",nowNewDeaths))
        else:
            self.nowNewDeaths = "None"

    except Exception as ex:
        print("exception => error setting now new deaths --- {0}".format(ex))
        self.nowNewDeaths = "None"

def setNowTotalRecovered(self,nowTotalRecovered):
    try:
        if (nowTotalRecovered != "None"):
            self.nowTotalRecovered = int(nowTotalRecovered.replace(",",""))
        else:
            self.nowTotalRecovered = "None"

    except Exception as ex:
        print("exception => error setting now total recovered --- {0}".format(ex))
        self.nowTotalRecovered = "None"


def checkEmpty(data):
    if (data == None or len(data) == 0):
        data = "None"
        return data
    else:
        return data