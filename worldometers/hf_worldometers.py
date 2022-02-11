from datetime import datetime

def printTime():
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

def checkEmpty(data):
    if (data == None or len(data) == 0):
        data = "None"
        return data
    else:
        return data