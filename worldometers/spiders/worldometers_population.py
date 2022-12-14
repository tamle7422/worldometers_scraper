import os,re
import time
import random
import scrapy
import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from scrapy.utils.log import configure_logging
from ..settings import USER_AGENT_LIST
from ..hf_worldometers import checkEmpty,setCountryPopulation,setPopulationPopulation,setYearlyChangePopulation, \
    setNetChangePopulation,setDensityPopulation,setLandAreaPopulation,setMigrantsPopulation,setFertilizationRatePopulation, \
    setMedianAgePopulation,setUrbanPopPercentPopulation,setWorldSharePopulation,loadPopulationItem

class WorldometersPopulationSpider(scrapy.Spider):
    name = "worldometers_population"
    allowed_domains = ["worldometers.info"]
    # start_urls = [
    #     'https://www.worldometers.info/coronavirus/#countries'
    # ]

    custom_settings = {
        "ITEM_PIPELINES": {
            'worldometers.pipelines.PopulationPipeline': 329,
        },
        "CLOSESPIDER_ITEMCOUNT": 2500
    }

    configure_logging(install_root_handler=False)
    logging.basicConfig(filename="population_log.txt",format='%(levelname)s: %(message)s',level=logging.INFO,
        filemode="w+")

    def __init__(self,*args,**kwargs):
        super(WorldometersPopulationSpider,self).__init__(*args,**kwargs)

        self.country = ""
        self.population = ""
        self.yearlyChange = ""
        self.netChange = ""
        self.density = ""
        self.landArea = ""
        self.migrants = ""
        self.fertilizationRate = ""
        self.medianAge = ""
        self.urbanPopPercent = ""
        self.worldShare = ""

        self.url = "https://www.worldometers.info/world-population/population-by-country/"

        self.options = Options()
        print(os.getcwd())
        self.path = os.path.join(os.getcwd(),"geckodriver.exe")

    def start_requests(self):
        yield scrapy.Request(url=self.url,callback=self.parsePopulation,headers={"User-Agent": random.choice(USER_AGENT_LIST)})

    def parsePopulation(self,response):
        try:
            self.options.headless = True
            self.driver = webdriver.Firefox(executable_path=self.path,options=self.options)
            self.driver.get(self.url)

            # //*[@id="example2"]/tbody/tr[1]
            # trTags = checkEmpty(response.xpath("..//html/body/div[3]/div[2]/div/div/div[2]/table/tbody/tr[@class='odd']"))
            trTags = self.driver.find_elements(by="xpath", \
                value=".//html/body/div[3]/div[2]/div/div/div[2]/table/tbody/tr")

            for elem in trTags:
                setCountryPopulation(self,elem)
                setPopulationPopulation(self,elem)
                setYearlyChangePopulation(self,elem)
                setNetChangePopulation(self,elem)
                setDensityPopulation(self,elem)
                setLandAreaPopulation(self,elem)
                setMigrantsPopulation(self,elem)
                setFertilizationRatePopulation(self,elem)
                setMedianAgePopulation(self,elem)
                setUrbanPopPercentPopulation(self,elem)
                setWorldSharePopulation(self,elem)

                loader = loadPopulationItem(self,response)
                yield loader.load_item()

        except Exception as ex:
            print("exception --- error in parse population => {0}".format(ex))

