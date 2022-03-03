import os,re
import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from ..hf_worldometers import checkEmpty,setNowTotalCases,setNowNewCases,setNowTotalDeaths,setNowNewDeaths, \
    setNowTotalRecovered,setNowNewRecovered,setNowActiveCases,setValue,loadNowCoronaItem,loadYesterdayCoronaItem, \
    loadTwoDaysCoronaItem

# using selenium
class CoronavirusSpider(scrapy.Spider):
    name = "coronavirus"
    allowed_domains = ["worldometers.info"]
    start_urls = [
        'https://www.worldometers.info/coronavirus/#countries'
    ]

    custom_settings = {
        "ITEM_PIPELINES": {
            'worldometers.pipelines.CoronavirusPipeline': 198,
        },
        "CLOSESPIDER_ITEMCOUNT": 11111
    }

    def __init__(self):
        self.nowRank = ""
        self.nowCountry = ""
        self.nowTotalCases = ""
        self.nowNewCases = ""
        self.nowTotalDeaths = ""
        self.nowNewDeaths = ""
        self.nowTotalRecovered = ""
        self.nowNewRecovered = ""
        self.nowActiveCases = ""
        self.nowSeriousCritical = ""
        self.nowCasesPerMillion = ""
        self.nowDeathsPerMillion = ""
        self.nowTotalTests = ""
        self.nowTestsPerMillion = ""
        self.nowPopulation = ""

        self.yesterdayRank = ""
        self.yesterdayCountry = ""
        self.yesterdayTotalCases = ""
        self.yesterdayNewCases = ""
        self.yesterdayTotalDeaths = ""
        self.yesterdayNewDeaths = ""
        self.yesterdayTotalRecovered = ""
        self.yesterdayNewRecovered = ""
        self.yesterdayActiveCases = ""
        self.yesterdaySeriousCritical = ""
        self.yesterdayCasesPerMillion = ""
        self.yesterdayDeathsPerMillion = ""
        self.yesterdayTotalTests = ""
        self.yesterdayTestsPerMillion = ""
        self.yesterdayPopulation = ""

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

        self.options = Options()
        print(os.getcwd())
        self.path = os.path.join(os.getcwd(),"geckodriver.exe")

    def parse(self,response):
        self.options.headless = True
        self.driver = webdriver.Firefox(executable_path=self.path,options=self.options)
        self.driver.get(response.url)

        # simulate button click
        nowButton = self.driver.find_element_by_xpath("//li[contains(@id,'nav-today-tab')]/a")
        yesterdayButton = self.driver.find_element_by_xpath("//li[contains(@id,'nav-yesterday-tab')]/a")
        _2DaysButton = self.driver.find_element_by_xpath("//li[contains(@id,'nav-yesterday2-tab')]/a")

        # try:
        #     self.driver.execute_script("arguments[0].click();",nowButton)
        #     trTagsNow = self.driver.find_elements_by_xpath("//table[contains(@id,'main_table_countries_today')]/tbody/tr[@class='odd' or @class='even']")
        #
        #     for nWebElem in trTagsNow:
        #         # unwanted tags
        #         if (len(nWebElem.text) == 0):
        #             continue
        #
        #         nowRank = checkEmpty(nWebElem.find_element_by_xpath(".//td[1]").get_attribute("innerText"))
        #         if (nowRank != "None"):
        #             self.nowRank = nowRank
        #         else:
        #             self.nowRank = "None"
        #
        #         # some countries have a or span tags
        #         try:
        #             nowCountry = nWebElem.find_element_by_xpath(".//td[2]/a").get_attribute("innerText")
        #             if (nowCountry != "None"):
        #                 self.nowCountry = nowCountry
        #             else:
        #                 self.nowCountry = "None"
        #
        #         except:
        #             nowCountry = nWebElem.find_element_by_xpath(".//td[2]/span").get_attribute("innerText")
        #             if (nowCountry != "None"):
        #                 self.nowCountry = nowCountry
        #             else:
        #                 self.nowCountry = "None"
        #
        #         nowTotalCases = nWebElem.find_element_by_xpath(".//td[3]").get_attribute("innerText")
        #         setNowTotalCases(self,nowTotalCases)
        #
        #         nowNewCases = nWebElem.find_element_by_xpath(".//td[4]").get_attribute("innerText")
        #         setNowNewCases(self,nowNewCases)
        #
        #         nowTotalDeaths = nWebElem.find_element_by_xpath(".//td[5]").get_attribute("innerText")
        #         setNowTotalDeaths(self,nowTotalDeaths)
        #
        #         nowNewDeaths = nWebElem.find_element_by_xpath(".//td[6]").get_attribute("innerText")
        #         setNowNewDeaths(self,nowNewDeaths)
        #
        #         nowTotalRecovered = nWebElem.find_element_by_xpath(".//td[7]").get_attribute("innerText")
        #         setNowTotalRecovered(self, nowTotalRecovered)
        #
        #         nowNewRecovered = nWebElem.find_element_by_xpath(".//td[8]").get_attribute("innerText")
        #         setNowNewRecovered(self,nowNewRecovered)
        #
        #         nowActiveCases = nWebElem.find_element_by_xpath(".//td[9]").get_attribute("innerText")
        #         setNowActiveCases(self,nowActiveCases)
        #
        #         nowSeriousCritical = nWebElem.find_element_by_xpath(".//td[10]").get_attribute("innerText")
        #         setValue(self,nowSeriousCritical,"nowSeriousCritical")
        #
        #         nowCasesPerMillion = nWebElem.find_element_by_xpath(".//td[11]").get_attribute("innerText")
        #         setValue(self,nowCasesPerMillion,"nowCasesPerMillion")
        #
        #         nowDeathsPerMillion = nWebElem.find_element_by_xpath(".//td[12]").get_attribute("innerText")
        #         setValue(self,nowDeathsPerMillion,"nowDeathsPerMillion")
        #
        #         nowTotalTests = nWebElem.find_element_by_xpath(".//td[13]").get_attribute("innerText")
        #         setValue(self,nowTotalTests,"nowTotalTests")
        #
        #         nowTestsPerMillion = nWebElem.find_element_by_xpath(".//td[14]").get_attribute("innerText")
        #         setValue(self,nowTestsPerMillion,"nowTestsPerMillion")
        #
        #         nowPopulation = nWebElem.find_element_by_xpath(".//td[15]").get_attribute("innerText")
        #         setValue(self,nowPopulation,"nowPopulation")
        #
        #         loader = loadNowCoronaItem(self,response)
        #         yield loader.load_item()
        #
        # except Exception as ex:
        #     print("exception => error click today --- {0}".format(ex))


        # try:
        #     self.driver.execute_script("arguments[0].click();",yesterdayButton)
        #     trTagsYesterday = self.driver.find_elements_by_xpath("//table[contains(@id,'main_table_countries_yesterday')]/tbody/tr[@class='odd' or @class='even']")
        #
        #     for yWebElem in trTagsYesterday:
        #         # unwanted tags
        #         if (len(yWebElem.text) == 0):
        #             continue
        #
        #         yesterdayRank = checkEmpty(yWebElem.find_element_by_xpath(".//td[1]").get_attribute("innerText"))
        #         if (yesterdayRank != "None"):
        #             self.yesterdayRank = yesterdayRank
        #         else:
        #             self.yesterdayRank = "None"
        #
        #         # some countries have a or span tags
        #         try:
        #             yesterdayCountry = yWebElem.find_element_by_xpath(".//td[2]/a").get_attribute("innerText")
        #             if (yesterdayCountry != "None"):
        #                 self.yesterdayCountry = yesterdayCountry
        #             else:
        #                 self.yesterdayCountry = "None"
        #
        #         except:
        #             yesterdayCountry = yWebElem.find_element_by_xpath(".//td[2]/span").get_attribute("innerText")
        #             if (yesterdayCountry != "None"):
        #                 self.yesterdayCountry = yesterdayCountry
        #             else:
        #                 self.yesterdayCountry = "None"
        #
        #         yesterdayTotalCases = yWebElem.find_element_by_xpath(".//td[3]").get_attribute("innerText")
        #         setValue(self,yesterdayTotalCases,"yesterdayTotalCases")
        #
        #         yesterdayNewCases = yWebElem.find_element_by_xpath(".//td[4]").get_attribute("innerText")
        #         setValue(self,yesterdayNewCases,"yesterdayNewCases")
        #
        #         yesterdayTotalDeaths = yWebElem.find_element_by_xpath(".//td[5]").get_attribute("innerText")
        #         setValue(self,yesterdayTotalDeaths,"yesterdayTotalDeaths")
        #
        #         yesterdayNewDeaths = yWebElem.find_element_by_xpath(".//td[6]").get_attribute("innerText")
        #         setValue(self,yesterdayNewDeaths,"yesterdayNewDeaths")
        #
        #         yesterdayTotalRecovered = yWebElem.find_element_by_xpath(".//td[7]").get_attribute("innerText")
        #         setValue(self,yesterdayTotalRecovered,"yesterdayTotalRecovered")
        #
        #         yesterdayNewRecovered = yWebElem.find_element_by_xpath(".//td[8]").get_attribute("innerText")
        #         setValue(self,yesterdayNewRecovered,"yesterdayNewRecovered")
        #
        #         yesterdayActiveCases = yWebElem.find_element_by_xpath(".//td[9]").get_attribute("innerText")
        #         setValue(self,yesterdayActiveCases,"yesterdayActiveCases")
        #
        #         yesterdaySeriousCritical = yWebElem.find_element_by_xpath(".//td[10]").get_attribute("innerText")
        #         setValue(self,yesterdaySeriousCritical,"yesterdaySeriousCritical")
        #
        #         yesterdayCasesPerMillion = yWebElem.find_element_by_xpath(".//td[11]").get_attribute("innerText")
        #         setValue(self,yesterdayCasesPerMillion,"yesterdayCasesPerMillion")
        #
        #         yesterdayDeathsPerMillion = yWebElem.find_element_by_xpath(".//td[12]").get_attribute("innerText")
        #         setValue(self,yesterdayDeathsPerMillion,"yesterdayDeathsPerMillion")
        #
        #         yesterdayTotalTests = yWebElem.find_element_by_xpath(".//td[13]").get_attribute("innerText")
        #         setValue(self,yesterdayTotalTests,"yesterdayTotalTests")
        #
        #         yesterdayTestsPerMillion = yWebElem.find_element_by_xpath(".//td[14]").get_attribute("innerText")
        #         setValue(self, yesterdayTestsPerMillion,"yesterdayTestsPerMillion")
        #
        #         yesterdayPopulation = yWebElem.find_element_by_xpath(".//td[15]").get_attribute("innerText")
        #         setValue(self,yesterdayPopulation,"yesterdayPopulation")
        #
        #         loader = loadYesterdayCoronaItem(self,response)
        #         yield loader.load_item()
        #
        # except Exception as ex:
        #     print("exception => error click yesterday --- {0}".format(ex))

        try:
            self.driver.execute_script("arguments[0].click();",_2DaysButton)
            trTags2Days = self.driver.find_elements_by_xpath("//table[contains(@id,'main_table_countries_yesterday2')]/tbody/tr[@class='odd' or @class='even']")

            for twoWebElem in trTags2Days:
                # unwanted tags
                if (len(twoWebElem.text) == 0):
                    continue

                twoDaysRank = checkEmpty(twoWebElem.find_element_by_xpath(".//td[1]").get_attribute("innerText"))
                if (twoDaysRank != "None"):
                    self.twoDaysRank = twoDaysRank
                else:
                    self.twoDaysRank = "None"

                # some countries have a or span tags
                try:
                    twoDaysCountry = twoWebElem.find_element_by_xpath(".//td[2]/a").get_attribute("innerText")
                    if (twoDaysCountry != "None"):
                        self.twoDaysCountry = twoDaysCountry
                    else:
                        self.twoDaysCountry = "None"

                except:
                    twoDaysCountry = twoWebElem.find_element_by_xpath(".//td[2]/span").get_attribute("innerText")
                    if (twoDaysCountry != "None"):
                        self.twoDaysCountry = twoDaysCountry
                    else:
                        self.twoDaysCountry = "None"

                twoDaysTotalCases = twoWebElem.find_element_by_xpath(".//td[3]").get_attribute("innerText")
                setValue(self,twoDaysTotalCases,"twoDaysTotalCases")

                twoDaysNewCases = twoWebElem.find_element_by_xpath(".//td[4]").get_attribute("innerText")
                setValue(self,twoDaysNewCases,"twoDaysNewCases")

                twoDaysTotalDeaths = twoWebElem.find_element_by_xpath(".//td[5]").get_attribute("innerText")
                setValue(self,twoDaysTotalDeaths,"twoDaysTotalDeaths")

                twoDaysNewDeaths = twoWebElem.find_element_by_xpath(".//td[6]").get_attribute("innerText")
                setValue(self,twoDaysNewDeaths,"twoDaysNewDeaths")

                twoDaysTotalRecovered = twoWebElem.find_element_by_xpath(".//td[7]").get_attribute("innerText")
                setValue(self,twoDaysTotalRecovered,"twoDaysTotalRecovered")

                twoDaysNewRecovered = twoWebElem.find_element_by_xpath(".//td[8]").get_attribute("innerText")
                setValue(self,twoDaysNewRecovered,"twoDaysNewRecovered")

                twoDaysActiveCases = twoWebElem.find_element_by_xpath(".//td[9]").get_attribute("innerText")
                setValue(self,twoDaysActiveCases,"twoDaysActiveCases")

                twoDaysSeriousCritical = twoWebElem.find_element_by_xpath(".//td[10]").get_attribute("innerText")
                setValue(self,twoDaysSeriousCritical,"twoDaysSeriousCritical")

                twoDaysCasesPerMillion = twoWebElem.find_element_by_xpath(".//td[11]").get_attribute("innerText")
                setValue(self,twoDaysCasesPerMillion,"twoDaysCasesPerMillion")

                twoDaysDeathsPerMillion = twoWebElem.find_element_by_xpath(".//td[12]").get_attribute("innerText")
                setValue(self,twoDaysDeathsPerMillion,"twoDaysDeathsPerMillion")

                twoDaysTotalTests = twoWebElem.find_element_by_xpath(".//td[13]").get_attribute("innerText")
                setValue(self,twoDaysTotalTests,"twoDaysTotalTests")

                twoDaysTestsPerMillion = twoWebElem.find_element_by_xpath(".//td[14]").get_attribute("innerText")
                setValue(self,twoDaysTestsPerMillion,"twoDaysTestsPerMillion")

                twoDaysPopulation = twoWebElem.find_element_by_xpath(".//td[15]").get_attribute("innerText")
                setValue(self,twoDaysPopulation,"twoDaysPopulation")

                loader = loadTwoDaysCoronaItem(self,response)
                yield loader.load_item()

        except Exception as ex:
            print("exception => error click two days --- {0}".format(ex))

        self.driver.quit()
