import os
import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from ..hf_worldometers import checkEmpty,setNowTotalCases,setNowNewCases,setNowTotalDeaths,setNowNewDeaths, \
    setNowTotalRecovered,setNowNewRecovered,setNowActiveCases,setValue

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
        "CLOSESPIDER_ITEMCOUNT": 21
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

        try:
            self.driver.execute_script("arguments[0].click();",nowButton)

            trTagsNow = self.driver.find_elements_by_xpath("//table[contains(@id,'main_table_countries')]/tbody/tr[@class='odd' or @class='even']")

            for webElem in trTagsNow:
                nowRank = checkEmpty(webElem.find_element_by_xpath(".//td[1]").get_attribute("innerText"))
                if (nowRank != "None"):
                    self.nowRank = nowRank
                else:
                    self.nowRank = "None"

                nowCountry = webElem.find_element_by_xpath(".//td[2]/a").get_attribute("innerText")
                if (nowCountry != "None"):
                    self.nowCountry = nowCountry
                else:
                    self.nowCountry = "None"

                nowTotalCases = webElem.find_element_by_xpath(".//td[3]").get_attribute("innerText")
                setNowTotalCases(self,nowTotalCases)

                nowNewCases = webElem.find_element_by_xpath(".//td[4]").get_attribute("innerText")
                setNowNewCases(self,nowNewCases)

                nowTotalDeaths = webElem.find_element_by_xpath(".//td[5]").get_attribute("innerText")
                setNowTotalDeaths(self,nowTotalDeaths)

                nowNewDeaths = webElem.find_element_by_xpath(".//td[6]").get_attribute("innerText")
                setNowNewDeaths(self,nowNewDeaths)

                nowTotalRecovered = webElem.find_element_by_xpath(".//td[7]").get_attribute("innerText")
                setNowTotalRecovered(self, nowTotalRecovered)

                nowNewRecovered = webElem.find_element_by_xpath(".//td[8]").get_attribute("innerText")
                setNowNewRecovered(self,nowNewRecovered)

                nowActiveCases = webElem.find_element_by_xpath(".//td[9]").get_attribute("innerText")
                setNowActiveCases(self,nowActiveCases)

                nowSeriousCritical = webElem.find_element_by_xpath(".//td[10]").get_attribute("innerText")
                setValue(self,nowSeriousCritical,"nowSeriousCritical")

                nowCasesPerMillion = webElem.find_element_by_xpath(".//td[11]").get_attribute("innerText")
                setValue(self,nowCasesPerMillion,"nowCasesPerMillion")


                print("")



            self.driver.execute_script("arguments[0].click();", yesterdayButton)
            # yesterdayButton.click()

            trTagsYesterday = self.driver.find_elements_by_xpath("//table[contains(@id,'main_table_countries')]/tbody/tr[@class='odd' or @class='even']")

            for webElem in trTagsYesterday:
                test1 = webElem.find_element_by_xpath(".//td[1]").get_attribute("innerText")
                test2 = webElem.find_element_by_xpath(".//td[2]/a").get_attribute("innerText")
                test3 = webElem.find_element_by_xpath(".//td[3]").get_attribute("innerText")

                # //*[@id="main_table_countries_yesterday"]/tbody[1]/tr[5]/td[3]

                # /html/body/div[3]/div[3]/div/div[6]/div[2]/div/table/tbody[1]/tr[5]/td[9]
                print("")

                print("")

        except Exception as ex:
            print("exception => error click yesterday --- {0}".format(ex))
            self.driver.quit()


        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')