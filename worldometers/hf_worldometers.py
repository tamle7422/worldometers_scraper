import re
import pickle
from datetime import datetime
from scrapy.loader import ItemLoader
from .items import CoronavirusCurrItem,CoronavirusYestItem,Coronavirus2DaysItem,PopulationItem

def setRankCurrent(self,elemCurr):
    try:
        rankCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[1]").get_attribute("innerText"))
        if (rankCurr != "None"):
            self.rankCurr = rankCurr
        else:
            self.rankCurr = "None"

    except Exception as ex:
        print("exception --- error in set rank current => {0}".format(ex))
        self.rankCurr = "None"

def setCountryCurrent(self,elemCurr):
    # some countries have a or span tags
    try:
        countryCurr = checkEmpty(elemCurr.find_element(by="xpath", value=".//td[2]/a").get_attribute("innerText"))
        if (countryCurr != "None"):
            self.countryCurr = countryCurr
        else:
            countryCurr = checkEmpty(elemCurr.find_element_by_xpath(".//td[2]/span").get_attribute("innerText"))
            if (countryCurr != "None"):
                self.countryCurr = countryCurr
            else:
                self.countryCurr = "None"

    except Exception as ex:
        print("exception --- error in set country current => {0}".format(ex))
        self.countryCurr = "None"

def setTotalCasesCurrent(self,elemCurr):
    try:
        totalCasesCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[3]").get_attribute("innerText"))
        if (totalCasesCurr != "None"):
            self.totalCasesCurr = re.sub("[\,]+","",totalCasesCurr)
        else:
            self.totalCasesCurr = "None"

    except Exception as ex:
        print("exception --- error in set total cases current => {0}".format(ex))
        self.totalCasesCurr = "None"

def setNewCasesCurrent(self,elemCurr):
    try:
        newCasesCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[4]").get_attribute("innerText"))
        if (newCasesCurr != "None"):
            self.newCasesCurr = re.sub("[\,]+","",newCasesCurr)
        else:
            self.newCasesCurr = "None"

    except Exception as ex:
        print("exception --- error in set new cases current => {0}".format(ex))
        self.newCasesCurr = "None"

def setTotalDeathsCurrent(self,elemCurr):
    try:
        totalDeathsCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[5]").get_attribute("innerText"))
        if (totalDeathsCurr != "None"):
            self.totalDeathsCurr = totalDeathsCurr.replace(",","")
        else:
            self.totalDeathsCurr = "None"

    except Exception as ex:
        print("exception --- error in set total deaths current => {0}".format(ex))
        self.totalDeathsCurr = "None"

def setNewDeathsCurrent(self,elemCurr):
    try:
        newDeathsCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[6]").get_attribute("innerText"))
        if (newDeathsCurr != "None"):
            self.newDeathsCurr = re.sub(r"[^0-9]+","",newDeathsCurr)
        else:
            self.newDeathsCurr = "None"

    except Exception as ex:
        print("exception --- error in set new deaths current => {0}".format(ex))
        self.nowNewDeaths = "None"

def setTotalRecoveredCurrent(self,elemCurr):
    try:
        totalRecoveredCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[7]").get_attribute("innerText"))
        if (totalRecoveredCurr != "None"):
            self.totalRecoveredCurr = totalRecoveredCurr.replace(",","")
        else:
            self.totalRecoveredCurr = "None"

    except Exception as ex:
        print("exception --- error in set total recovered current => {0}".format(ex))
        self.totalRecoveredCurr = "None"

def setNewRecoveredCurrent(self,elemCurr):
    try:
        newRecoveredCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[8]").get_attribute("innerText"))
        if (newRecoveredCurr != "None"):
            self.newRecoveredCurr = re.sub(r"[^0-9]+","",newRecoveredCurr)
        else:
            self.newRecoveredCurr = "None"

    except Exception as ex:
        print("exception --- error in set new recovered current => {0}".format(ex))
        self.newRecoveredCurr = "None"

def setActiveCasesCurrent(self,elemCurr):
    try:
        activeCasesCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[9]").get_attribute("innerText"))
        if (activeCasesCurr != "None"):
            self.activeCasesCurr = re.sub(r"[^0-9]","",activeCasesCurr)
        else:
            self.activeCasesCurr = "None"

    except Exception as ex:
        print("exception --- error in set active cases current => {0}".format(ex))
        self.activeCasesCurr = "None"
# ----------------------------------------------------------------------------------------------------------------------
def setCountryYesterday(self,elemYest):
    try:
        # some countries have a or span tags
        countryYest = checkEmpty(elemYest.find_element(by="xpath", value=".//td[2]/a").get_attribute("innerText"))
        if (countryYest != "None"):
            self.countryYest = countryYest
        else:
            countryYest = checkEmpty(
                elemYest.find_element(by="xpath", value=".//td[2]/span").get_attribute("innerText"))
            if (countryYest != "None"):
                self.countryYest = countryYest
            else:
                self.countryYest = "None"

    except Exception as ex:
        print("exception --- error in set country yesterday => {0}".format(ex))
        self.countryYest = "None"

# ----------------------------------------------------------------------------------------------------------------------
def setCountry2Days(self,elem2Days):
    try:
        # some countries have a or span tags
        country2Days = checkEmpty(elem2Days.find_element(by="xpath",value=".//td[2]/a").get_attribute("innerText"))
        if (country2Days != "None"):
            self.country2Days = country2Days
        else:
            country2Days = checkEmpty(elem2Days.find_element(by="xpath",value=".//td[2]/span").get_attribute("innerText"))
            if (country2Days != "None"):
                self.country2Days = country2Days
            else:
                self.country2Days = "None"

    except Exception as ex:
        print("exception --- error in set country 2 days => {0}".format(ex))
        self.country2Days = "None"
# ----------------------------------------------------------------------------------------------------------------------
def setCountryPopulation(self,elem):
    try:
        # //*[@id="example2"]/tbody/tr[1]/td[2]/a
        country = checkEmpty(elem.find_element(by="xpath",value=".//td[2]/a").get_attribute("innerText"))
        if (country != "None"):
            self.country = country
        else:
            self.country = "None"

    except Exception as ex:
        print("exception --- error in set country population => {0}".format(ex))
        self.country = "None"

def setPopulationPopulation(self,elem):
    try:
        # //*[@id="example2"]/tbody/tr[1]/td[3]
        population = checkEmpty(elem.find_element(by="xpath",value=".//td[3]").get_attribute("innerText"))
        if (population != "None"):
            self.population = re.sub("[\,]+","",population)
        else:
            self.population = "None"

    except Exception as ex:
        print("exception --- error in set population population => {0}".format(ex))
        self.population = "None"

def setYearlyChangePopulation(self,elem):
    try:
        # //*[@id="example2"]/tbody/tr[1]/td[4]
        yearlyChange = checkEmpty(elem.find_element(by="xpath",value=".//td[4]").get_attribute("innerText"))
        if (yearlyChange != "None"):
            self.yearlyChange = re.sub("[\%]+","",yearlyChange)
        else:
            self.yearlyChange = "None"

    except Exception as ex:
        print("exception --- error in set yearly change population => {0}".format(ex))
        self.yearlyChange = "None"

def setNetChangePopulation(self,elem):
    try:
        # //*[@id="example2"]/tbody/tr[1]/td[5]
        netChange = checkEmpty(elem.find_element(by="xpath",value=".//td[5]").get_attribute("innerText"))
        if (netChange != "None"):
            self.netChange = re.sub("[\,]+","",netChange)
        else:
            self.netChange = "None"

    except Exception as ex:
        print("exception --- error in set net change population => {0}".format(ex))
        self.netChange = "None"

def setDensityPopulation(self,elem):
    try:
        # //*[@id="example2"]/tbody/tr[1]/td[6]
        density = checkEmpty(elem.find_element(by="xpath",value=".//td[6]").get_attribute("innerText"))
        if (density != "None"):
            self.density = re.sub("[\,]+","",density)
        else:
            self.density = "None"

    except Exception as ex:
        print("exception --- error in set density population => {0}".format(ex))
        self.density = "None"

def setLandAreaPopulation(self,elem):
    try:
        # //*[@id="example2"]/tbody/tr[1]/td[7]
        landArea = checkEmpty(elem.find_element(by="xpath",value=".//td[7]").get_attribute("innerText"))
        if (landArea != "None"):
            self.landArea = re.sub("[\,]+","",landArea)
        else:
            self.landArea = "None"

    except Exception as ex:
        print("exception --- error in set land area population => {0}".format(ex))
        self.landArea = "None"

def setMigrantsPopulation(self,elem):
    try:
        # //*[@id="example2"]/tbody/tr[1]/td[8]
        migrants = checkEmpty(elem.find_element(by="xpath",value=".//td[8]").get_attribute("innerText"))
        if (migrants != "None"):
            self.migrants = re.sub("[\,]+","",migrants)
        else:
            self.migrants = "None"

    except Exception as ex:
        print("exception --- error in set migrants population => {0}".format(ex))
        self.migrants = "None"

def setFertilizationRatePopulation(self,elem):
    try:
        # //*[@id="example2"]/tbody/tr[1]/td[9]
        fertilizationRate = checkEmpty(elem.find_element(by="xpath",value=".//td[9]").get_attribute("innerText"))
        if (fertilizationRate != "None"):
            self.fertilizationRate = fertilizationRate
        else:
            self.fertilizationRate = "None"

    except Exception as ex:
        print("exception --- error in set fertilization rate population => {0}".format(ex))
        self.fertilizationRate = "None"

def setMedianAgePopulation(self,elem):
    try:
        # //*[@id="example2"]/tbody/tr[1]/td[10]
        medianAge = checkEmpty(elem.find_element(by="xpath",value=".//td[10]").get_attribute("innerText"))
        if (medianAge != "None"):
            self.medianAge = medianAge
        else:
            self.medianAge = "None"

    except Exception as ex:
        print("exception --- error in set median age population => {0}".format(ex))
        self.medianAge = "None"

def setUrbanPopPercentPopulation(self,elem):
    try:
        # //*[@id="example2"]/tbody/tr[1]/td[11]
        urbanPopPercent = checkEmpty(elem.find_element(by="xpath",value=".//td[11]").get_attribute("innerText"))
        if (urbanPopPercent != "None"):
            self.urbanPopPercent = re.sub("[\%\s]+","",urbanPopPercent)
        else:
            self.urbanPopPercent = "None"

    except Exception as ex:
        print("exception --- error in set urban pop percent population => {0}".format(ex))
        self.urbanPopPercent = "None"

def setWorldSharePopulation(self,elem):
    try:
        # //*[@id="example2"]/tbody/tr[1]/td[12]
        worldShare = checkEmpty(elem.find_element(by="xpath",value=".//td[12]").get_attribute("innerText"))
        if (worldShare != "None"):
            self.worldShare = re.sub("[\%]+","",worldShare)
        else:
            self.worldShare = "None"

    except Exception as ex:
        print("exception --- error in set world share population => {0}".format(ex))
        self.worldShare = "None"
# ----------------------------------------------------------------------------------------------------------------------
# dynamic variable setter
def setValue(self,value,type):
    try:
        if (value != "None"):
            setattr(self,type,re.sub(r"[^0-9]+","",value))
        else:
            setattr(self,type,"None")

    except Exception as ex:
        print("exception --- error in set value => {0} {1} {2}".format(value,type,ex))
        setattr(self,type,"None")

def loadCoronavirusCurrItem(self,response):
    try:
        self.rankCurr = self.rankCurr if (len(self.rankCurr) != 0) else "None"
        self.countryCurr = self.countryCurr if (len(self.countryCurr) != 0) else "None"
        self.totalCasesCurr = self.totalCasesCurr if (len(self.totalCasesCurr) != 0) else "None"
        self.newCasesCurr = self.newCasesCurr if (len(self.newCasesCurr) != 0) else "None"
        self.totalDeathsCurr = self.totalDeathsCurr if (len(self.totalDeathsCurr) != 0) else "None"
        self.newDeathsCurr = self.newDeathsCurr if (len(self.newDeathsCurr) != 0) else "None"
        self.totalRecoveredCurr = self.totalRecoveredCurr if (len(self.totalRecoveredCurr) != 0) else "None"
        self.newRecoveredCurr = self.newRecoveredCurr if (len(self.newRecoveredCurr) != 0) else "None"
        self.activeCasesCurr = self.activeCasesCurr if (len(self.activeCasesCurr) != 0) else "None"
        self.seriousCriticalCurr = self.seriousCriticalCurr if (len(self.seriousCriticalCurr) != 0) else "None"
        self.casesPerMillionCurr = self.casesPerMillionCurr if (len(self.casesPerMillionCurr) != 0) else "None"
        self.deathsPerMillionCurr = self.deathsPerMillionCurr if (len(self.deathsPerMillionCurr) != 0) else "None"
        self.totalTestsCurr = self.totalTestsCurr if (len(self.totalTestsCurr) != 0) else "None"
        self.testsPerMillionCurr = self.testsPerMillionCurr if (len(self.testsPerMillionCurr) != 0) else "None"
        self.populationCurr = self.populationCurr if (len(self.populationCurr) != 0) else "None"

        loader = ItemLoader(item=CoronavirusCurrItem(),response=response)
        loader.add_value("rankCurr",self.rankCurr)
        loader.add_value("countryCurr",self.countryCurr)
        loader.add_value("totalCasesCurr", self.totalCasesCurr)
        loader.add_value("newCasesCurr", self.newCasesCurr)
        loader.add_value("totalDeathsCurr", self.totalDeathsCurr)
        loader.add_value("newDeathsCurr",self.newDeathsCurr)
        loader.add_value("totalRecoveredCurr",self.totalRecoveredCurr)
        loader.add_value("newRecoveredCurr",self.newRecoveredCurr)
        loader.add_value("activeCasesCurr",self.activeCasesCurr)
        loader.add_value("seriousCriticalCurr", self.seriousCriticalCurr)
        loader.add_value("casesPerMillionCurr",self.casesPerMillionCurr)
        loader.add_value("deathsPerMillionCurr",self.deathsPerMillionCurr)
        loader.add_value("totalTestsCurr", self.totalTestsCurr)
        loader.add_value("testsPerMillionCurr", self.testsPerMillionCurr)
        loader.add_value("populationCurr",self.populationCurr)
        return loader

    except Exception as ex:
        print("exception --- error in load coronavirus current item => {0}".format(ex))

def loadCoronavirusYestItem(self,response):
    try:
        self.rankYest = self.rankYest if (len(self.rankYest) != 0) else "None"
        self.countryYest = self.countryYest if (len(self.countryYest) != 0) else "None"
        self.totalCasesYest = self.totalCasesYest if (len(self.totalCasesYest) != 0) else "None"
        self.newCasesYest = self.newCasesYest if (len(self.newCasesYest) != 0) else "None"
        self.totalDeathsYest = self.totalDeathsYest if (len(self.totalDeathsYest) != 0) else "None"
        self.newDeathsYest = self.newDeathsYest if (len(self.newDeathsYest) != 0) else "None"
        self.totalRecoveredYest = self.totalRecoveredYest if (len(self.totalRecoveredYest) != 0) else "None"
        self.newRecoveredYest = self.newRecoveredYest if (len(self.newRecoveredYest) != 0) else "None"
        self.activeCasesYest = self.activeCasesYest if (len(self.activeCasesYest) != 0) else "None"
        self.seriousCriticalYest = self.seriousCriticalYest if (len(self.seriousCriticalYest) != 0) else "None"
        self.casesPerMillionYest = self.casesPerMillionYest if (len(self.casesPerMillionYest) != 0) else "None"
        self.deathsPerMillionYest = self.deathsPerMillionYest if (len(self.deathsPerMillionYest) != 0) else "None"
        self.totalTestsYest = self.totalTestsYest if (len(self.totalTestsYest) != 0) else "None"
        self.testsPerMillionYest = self.testsPerMillionYest if (len(self.testsPerMillionYest) != 0) else "None"
        self.populationYest = self.populationYest if (len(self.populationYest) != 0) else "None"

        loader = ItemLoader(item=CoronavirusYestItem(),response=response)
        loader.add_value("rankYest",self.rankYest)
        loader.add_value("countryYest",self.countryYest)
        loader.add_value("totalCasesYest",self.totalCasesYest)
        loader.add_value("newCasesYest",self.newCasesYest)
        loader.add_value("totalDeathsYest", self.totalDeathsYest)
        loader.add_value("newDeathsYest", self.newDeathsYest)
        loader.add_value("totalRecoveredYest", self.totalRecoveredYest)
        loader.add_value("newRecoveredYest", self.newRecoveredYest)
        loader.add_value("activeCasesYest", self.activeCasesYest)
        loader.add_value("seriousCriticalYest",self.seriousCriticalYest)
        loader.add_value("casesPerMillionYest",self.casesPerMillionYest)
        loader.add_value("deathsPerMillionYest",self.deathsPerMillionYest)
        loader.add_value("totalTestsYest",self.totalTestsYest)
        loader.add_value("testsPerMillionYest",self.testsPerMillionYest)
        loader.add_value("populationYest",self.populationYest)
        return loader

    except Exception as ex:
        print("exception --- error in load coronavirus yesterday item => {0}".format(ex))

def loadCoronavirus2DaysItem(self,response):
    try:
        self.rank2Days = self.rank2Days if (len(self.rank2Days) != 0) else "None"
        self.country2Days = self.country2Days if (len(self.country2Days) != 0) else "None"
        self.totalCases2Days = self.totalCases2Days if (len(self.totalCases2Days) != 0) else "None"
        self.newCases2Days = self.newCases2Days if (len(self.newCases2Days) != 0) else "None"
        self.totalDeaths2Days = self.totalDeaths2Days if (len(self.totalDeaths2Days) != 0) else "None"
        self.newDeaths2Days = self.newDeaths2Days if (len(self.newDeaths2Days) != 0) else "None"
        self.totalRecovered2Days = self.totalRecovered2Days if (len(self.totalRecovered2Days) != 0) else "None"
        self.newRecovered2Days = self.newRecovered2Days if (len(self.newRecovered2Days) != 0) else "None"
        self.activeCases2Days = self.activeCases2Days if (len(self.activeCases2Days) != 0) else "None"
        self.seriousCritical2Days = self.seriousCritical2Days if (len(self.seriousCritical2Days) != 0) else "None"
        self.casesPerMillion2Days = self.casesPerMillion2Days if (len(self.casesPerMillion2Days) != 0) else "None"
        self.deathsPerMillion2Days = self.deathsPerMillion2Days if (len(self.deathsPerMillion2Days) != 0) else "None"
        self.totalTests2Days = self.totalTests2Days if (len(self.totalTests2Days) != 0) else "None"
        self.testsPerMillion2Days = self.testsPerMillion2Days if (len(self.testsPerMillion2Days) != 0) else "None"
        self.population2Days = self.population2Days if (len(self.population2Days) != 0) else "None"

        loader = ItemLoader(item=Coronavirus2DaysItem(),response=response)
        loader.add_value("rank2Days",self.rank2Days)
        loader.add_value("country2Days",self.country2Days)
        loader.add_value("totalCases2Days",self.totalCases2Days)
        loader.add_value("newCases2Days",self.newCases2Days)
        loader.add_value("totalDeaths2Days", self.totalDeaths2Days)
        loader.add_value("newDeaths2Days", self.newDeaths2Days)
        loader.add_value("totalRecovered2Days", self.totalRecovered2Days)
        loader.add_value("newRecovered2Days", self.newRecovered2Days)
        loader.add_value("activeCases2Days", self.activeCases2Days)
        loader.add_value("seriousCritical2Days",self.seriousCritical2Days)
        loader.add_value("casesPerMillion2Days",self.casesPerMillion2Days)
        loader.add_value("deathsPerMillion2Days",self.deathsPerMillion2Days)
        loader.add_value("totalTests2Days",self.totalTests2Days)
        loader.add_value("testsPerMillion2Days",self.testsPerMillion2Days)
        loader.add_value("population2Days",self.population2Days)
        return loader

    except Exception as ex:
        print("exception --- error in load coronavirus 2 days item => {0}".format(ex))

# ----------------------------------------------------------------------------------------------------------------------
def loadPopulationItem(self,response):
    try:
        self.country = self.country if (len(self.country) != 0) else "None"
        self.population = self.population if (len(self.population) != 0) else "None"
        self.yearlyChange = self.yearlyChange if (len(self.yearlyChange) != 0) else "None"
        self.netChange = self.netChange if (len(self.netChange) != 0) else "None"
        self.density = self.density if (len(self.density) != 0) else "None"
        self.landArea = self.landArea if (len(self.landArea) != 0) else "None"
        self.migrants = self.migrants if (len(self.migrants) != 0) else "None"
        self.fertilizationRate = self.fertilizationRate if (len(self.fertilizationRate) != 0) else "None"
        self.medianAge = self.medianAge if (len(self.medianAge) != 0) else "None"
        self.urbanPopPercent = self.urbanPopPercent if (len(self.urbanPopPercent) != 0) else "None"
        self.worldShare = self.worldShare if (len(self.worldShare) != 0) else "None"

        loader = ItemLoader(item=PopulationItem(),response=response)
        loader.add_value("country",self.country)
        loader.add_value("population",self.population)
        loader.add_value("yearlyChange",self.yearlyChange)
        loader.add_value("netChange",self.netChange)
        loader.add_value("density",self.density)
        loader.add_value("landArea",self.landArea)
        loader.add_value("migrants",self.migrants)
        loader.add_value("fertilizationRate",self.fertilizationRate)
        loader.add_value("medianAge",self.medianAge)
        loader.add_value("urbanPopPercent",self.urbanPopPercent)
        loader.add_value("worldShare",self.worldShare)
        return loader

    except Exception as ex:
        print("exception --- error in load population item => {0}".format(ex))

def checkEmpty(data):
    try:
        if (data == None or len(data) == 0):
            data = "None"
            return data
        else:
            return data

    except Exception as ex:
        print("exception --- error in check empty => {0}".format(ex))

def getTime():
    try:
        now = datetime.now()
        currentDate = now.strftime("%m_%d_%y")
        return currentDate

    except Exception as ex:
        print("exception --- error in get time => {0}".format(ex))
