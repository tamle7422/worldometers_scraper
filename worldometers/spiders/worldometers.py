import os
import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from ..hf_worldometers import checkEmpty

class CoronaVirusSpider(scrapy.Spider):
    name = "coronavirus"
    allowed_domains = ["worldometers.info"]
    start_urls = [
        'https://www.worldometers.info/coronavirus/#countries'
    ]

    def __init__(self):
        self.nowRank = ""
        self.nowCountry = ""
        self.nowTotalCases = ""
        self.nowNewCases = ""
        self.nowTotalDeaths = ""
        self.nowNewDeaths = ""


        self.options = Options()
        print(os.getcwd())
        self.path = os.path.join(os.getcwd(),"geckodriver.exe")

    def parse(self,response):
        self.options.headless = True
        self.driver = webdriver.Firefox(executable_path=self.path,options=self.options)
        self.driver.get(response.url)

        # //*[@id="nav-yesterday-tab"]/a
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

                test2 = webElem.find_element_by_xpath(".//td[2]/a").get_attribute("innerText")
                test3 = webElem.find_element_by_xpath(".//td[3]").get_attribute("innerText")

                # //*[@id="main_table_countries_yesterday"]/tbody[1]/tr[5]/td[3]

                # /html/body/div[3]/div[3]/div/div[6]/div[2]/div/table/tbody[1]/tr[5]/td[9]
                print("")

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