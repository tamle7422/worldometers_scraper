import os,re
import time
import random
import scrapy
import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from scrapy.utils.log import configure_logging
from ..settings import USER_AGENT_LIST
from ..hf_worldometers import checkEmpty,setRankCurrent,setCountryCurrent,setTotalCasesCurrent,setNewCasesCurrent, \
    setTotalDeathsCurrent,setNewDeathsCurrent,setTotalRecoveredCurrent,setNewRecoveredCurrent,setActiveCasesCurrent, \
    setValue,loadCoronavirusCurrItem,setCountryYesterday,loadCoronavirusYestItem,setCountry2Days, \
    loadCoronavirus2DaysItem

class WorldometersCoronavirusSpider(scrapy.Spider):
    name = "worldometers_coronavirus"
    allowed_domains = ["worldometers.info"]
    # start_urls = [
    #     'https://www.worldometers.info/coronavirus/#countries'
    # ]

    custom_settings = {
        "ITEM_PIPELINES": {
            'worldometers.pipelines.CoronavirusPipeline': 198,
        },
        "CLOSESPIDER_ITEMCOUNT": 25
    }

    configure_logging(install_root_handler=False)
    logging.basicConfig(filename="coronavirus_log.txt", format='%(levelname)s: %(message)s', level=logging.INFO,
                        filemode="w+")

    def __init__(self,*args,**kwargs):
        super(WorldometersCoronavirusSpider,self).__init__(*args,**kwargs)

        self.rankCurr = ""
        self.countryCurr = ""
        self.totalCasesCurr = ""
        self.newCasesCurr = ""
        self.totalDeathsCurr = ""
        self.newDeathsCurr = ""
        self.totalRecoveredCurr = ""
        self.newRecoveredCurr = ""
        self.activeCasesCurr = ""
        self.seriousCriticalCurr = ""
        self.casesPerMillionCurr = ""
        self.deathsPerMillionCurr = ""
        self.totalTestsCurr = ""
        self.testsPerMillionCurr = ""
        self.populationCurr = ""

        self.rankYest = ""
        self.countryYest = ""
        self.totalCasesYest = ""
        self.newCasesYest = ""
        self.totalDeathsYest = ""
        self.newDeathsYest = ""
        self.totalRecoveredYest = ""
        self.newRecoveredYest = ""
        self.activeCasesYest = ""
        self.seriousCriticalYest = ""
        self.casesPerMillionYest = ""
        self.deathsPerMillionYest = ""
        self.totalTestsYest = ""
        self.testsPerMillionYest = ""
        self.populationYest = ""

        self.twoDaysRank = ""
        self.twoDaysCountry = ""
        self.twoDaysTotalCases = ""
        self.twoDaysNewCases = ""
        self.twoDaysTotalDeaths = ""
        self.twoDaysNewDeaths = ""
        self.twoDaysTotalRecovered = ""
        self.twoDaysNewRecovered = ""
        self.twoDaysActiveCases = ""
        self.twoDaysSeriousCritical = ""
        self.twoDaysCasesPerMillion = ""
        self.twoDaysDeathsPerMillion = ""
        self.twoDaysTotalTests = ""
        self.twoDaysTestsPerMillion = ""
        self.twoDaysPopulation = ""

        self.url = "https://www.worldometers.info/coronavirus/#countries"

        self.options = Options()
        print(os.getcwd())
        self.path = os.path.join(os.getcwd(),"geckodriver.exe")

    def start_requests(self):
        yield scrapy.Request(url=self.url,callback=self.parseCoronavirus, \
            headers={"User-Agent": random.choice(USER_AGENT_LIST)})

    def parseCoronavirus(self,response):
        try:
            self.options.headless = True
            self.driver = webdriver.Firefox(executable_path=self.path, options=self.options)
            self.driver.get(self.url)

            # simulate button click
            btnCurrent = self.driver.find_element(by="xpath",value="//li[contains(@id,'nav-today-tab')]/a")
            time.sleep(1.25)
            self.driver.execute_script("arguments[0].click();",btnCurrent)
            trTagsCurr = self.driver.find_elements(by="xpath", \
                value="//table[contains(@id,'main_table_countries_today')]/tbody/tr[@class='odd' or @class='even']")

            for elemCurr in trTagsCurr:
                # filter tags
                if (len(elemCurr.text) == 0):
                    continue

                setRankCurrent(self,elemCurr)
                setCountryCurrent(self,elemCurr)
                setTotalCasesCurrent(self,elemCurr)
                setNewCasesCurrent(self,elemCurr)
                setTotalDeathsCurrent(self,elemCurr)
                setNewDeathsCurrent(self,elemCurr)
                setTotalRecoveredCurrent(self,elemCurr)
                setNewRecoveredCurrent(self,elemCurr)
                setActiveCasesCurrent(self,elemCurr)

                seriousCriticalCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[10]").get_attribute("innerText"))
                setValue(self,seriousCriticalCurr,"seriousCriticalCurr")

                casesPerMillionCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[11]").get_attribute("innerText"))
                setValue(self,casesPerMillionCurr,"casesPerMillionCurr")

                deathsPerMillionCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[12]").get_attribute("innerText"))
                setValue(self,deathsPerMillionCurr,"deathsPerMillionCurr")

                totalTestsCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[13]").get_attribute("innerText"))
                setValue(self,totalTestsCurr,"totalTestsCurr")

                testsPerMillionCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[14]").get_attribute("innerText"))
                setValue(self,testsPerMillionCurr,"testsPerMillionCurr")

                populationCurr = checkEmpty(elemCurr.find_element(by="xpath",value=".//td[15]").get_attribute("innerText"))
                setValue(self,populationCurr,"populationCurr")

                loader = loadCoronavirusCurrItem(self,response)
                yield loader.load_item()

        except Exception as ex:
            print("exception --- error in parse coronavirus --- current item => {0}".format(ex))

        try:
            btnYest = self.driver.find_element(by="xpath",value="//li[contains(@id,'nav-yesterday-tab')]/a")
            time.sleep(1.25)
            self.driver.execute_script("arguments[0].click();",btnYest)
            trTagsYest = self.driver.find_elements(by="xpath",
                value="//table[contains(@id,'main_table_countries_yesterday')]/tbody/tr[@class='odd' or @class='even']")

            for elemYest in trTagsYest:
                # filter tags
                if (len(elemYest.text) == 0):
                    continue

                rankYest = checkEmpty(elemYest.find_element(by="xpath",value=".//td[1]").get_attribute("innerText"))
                setValue(self,rankYest,"rankYest")

                setCountryYesterday(self,elemYest)

                totalCasesYest = checkEmpty(elemYest.find_element(by="xpath",value=".//td[3]").get_attribute("innerText"))
                setValue(self,totalCasesYest,"totalCasesYest")

                newCasesYest = checkEmpty(elemYest.find_element(by="xpath",value=".//td[4]").get_attribute("innerText"))
                setValue(self,newCasesYest,"newCasesYest")

                totalDeathsYest = checkEmpty(elemYest.find_element(by="xpath",value=".//td[5]").get_attribute("innerText"))
                setValue(self,totalDeathsYest,"totalDeathsYest")

                newDeathsYest = checkEmpty(elemYest.find_element(by="xpath",value=".//td[6]").get_attribute("innerText"))
                setValue(self,newDeathsYest,"newDeathsYest")

                totalRecoveredYest = checkEmpty(elemYest.find_element(by="xpath",value=".//td[7]").get_attribute("innerText"))
                setValue(self,totalRecoveredYest,"totalRecoveredYest")

                newRecoveredYest = checkEmpty(elemYest.find_element(by="xpath",value=".//td[8]").get_attribute("innerText"))
                setValue(self,newRecoveredYest,"newRecoveredYest")

                activeCasesYest = checkEmpty(elemYest.find_element(by="xpath",value=".//td[9]").get_attribute("innerText"))
                setValue(self,activeCasesYest,"activeCasesYest")

                seriousCriticalYest = checkEmpty(elemYest.find_element(by="xpath", \
                    value=".//td[10]").get_attribute("innerText"))
                setValue(self,seriousCriticalYest,"seriousCriticalYest")

                casesPerMillionYest = checkEmpty(elemYest.find_element(by="xpath", \
                    value=".//td[11]").get_attribute("innerText"))
                setValue(self,casesPerMillionYest,"casesPerMillionYest")

                deathsPerMillionYest = checkEmpty(elemYest.find_element(by="xpath", \
                    value=".//td[12]").get_attribute("innerText"))
                setValue(self,deathsPerMillionYest,"deathsPerMillionYest")

                totalTestsYest = checkEmpty(elemYest.find_element(by="xpath", \
                    value=".//td[13]").get_attribute("innerText"))
                setValue(self,totalTestsYest,"totalTestsYest")

                testsPerMillionYest = checkEmpty(elemYest.find_element(by="xpath", \
                    value=".//td[14]").get_attribute("innerText"))
                setValue(self,testsPerMillionYest,"testsPerMillionYest")

                populationYest = checkEmpty(elemYest.find_element(by="xpath",value=".//td[15]").get_attribute("innerText"))
                setValue(self,populationYest,"populationYest")

                loader = loadCoronavirusYestItem(self,response)
                yield loader.load_item()

        except Exception as ex:
            print("exception --- error in parse coronavirus --- yesterday item => {0}".format(ex))

        try:
            btn2Days = self.driver.find_element(by="xpath",value="//li[contains(@id,'nav-yesterday2-tab')]/a")
            time.sleep(1.25)
            self.driver.execute_script("arguments[0].click();",btn2Days)
            trTags2Days = self.driver.find_elements(by="xpath", \
                value="//table[contains(@id,'main_table_countries_yesterday2')]/tbody/tr[@class='odd' or @class='even']")

            for elem2Days in trTags2Days:
                # filter tags
                if (len(elem2Days.text) == 0):
                    continue

                rank2Days = checkEmpty(elem2Days.find_element(by="xpath",value=".//td[1]").get_attribute("innerText"))
                setValue(self,rank2Days,"rank2Days")

                setCountry2Days(self,elem2Days)

                totalCases2Days = checkEmpty(elem2Days.find_element(by="xpath",value=".//td[3]").get_attribute("innerText"))
                setValue(self,totalCases2Days,"totalCases2Days")

                newCases2Days = checkEmpty(elem2Days.find_element(by="xpath",value=".//td[4]").get_attribute("innerText"))
                setValue(self,newCases2Days,"newCases2Days")

                totalDeaths2Days = checkEmpty(elem2Days.find_element(by="xpath",value=".//td[5]").get_attribute("innerText"))
                setValue(self,totalDeaths2Days,"totalDeaths2Days")

                newDeaths2Days = checkEmpty(elem2Days.find_element(by="xpath",value=".//td[6]").get_attribute("innerText"))
                setValue(self,newDeaths2Days,"newDeaths2Days")

                totalRecovered2Days = checkEmpty(elem2Days.find_element(by="xpath", \
                    value=".//td[7]").get_attribute("innerText"))
                setValue(self,totalRecovered2Days,"totalRecovered2Days")

                newRecovered2Days = checkEmpty(elem2Days.find_element(by="xpath", \
                    value=".//td[8]").get_attribute("innerText"))
                setValue(self,newRecovered2Days,"newRecovered2Days")

                activeCases2Days = checkEmpty(elem2Days.find_element(by="xpath",value=".//td[9]").get_attribute("innerText"))
                setValue(self,activeCases2Days,"activeCases2Days")

                seriousCritical2Days = checkEmpty(elem2Days.find_element(by="xpath", \
                    value=".//td[10]").get_attribute("innerText"))
                setValue(self,seriousCritical2Days,"seriousCritical2Days")

                casesPerMillion2Days = checkEmpty(elem2Days.find_element(by="xpath", \
                    value=".//td[11]").get_attribute("innerText"))
                setValue(self,casesPerMillion2Days,"casesPerMillion2Days")

                deathsPerMillion2Days = checkEmpty(elem2Days.find_element(by="xpath", \
                    value=".//td[12]").get_attribute("innerText"))
                setValue(self,deathsPerMillion2Days,"deathsPerMillion2Days")

                totalTests2Days = checkEmpty(elem2Days.find_element(by="xpath",value=".//td[13]").get_attribute("innerText"))
                setValue(self,totalTests2Days,"totalTests2Days")

                testsPerMillion2Days = checkEmpty(elem2Days.find_element(by="xpath", \
                    value=".//td[14]").get_attribute("innerText"))
                setValue(self,testsPerMillion2Days,"testsPerMillion2Days")

                population2Days = checkEmpty(elem2Days.find_element(by="xpath",value=".//td[15]").get_attribute("innerText"))
                setValue(self,population2Days,"population2Days")

                loader = loadCoronavirus2DaysItem(self,response)
                yield loader.load_item()

        except Exception as ex:
            print("exception --- error in parse coronavirus --- 2 days item => {0}".format(ex))

        self.driver.quit()
