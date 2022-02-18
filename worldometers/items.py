# define here the models for your scraped items
#
# see documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CoronaItem(scrapy.Item):
    nowRank = scrapy.Field()
    nowCountry = scrapy.Field()
    nowTotalCases = scrapy.Field()
    nowNewCases = scrapy.Field()
    nowTotalDeaths = scrapy.Field()
    nowNewDeaths = scrapy.Field()
    nowTotalRecovered = scrapy.Field()
    nowNewRecovered = scrapy.Field()
    nowActiveCases = scrapy.Field()
    nowSeriousCritical = scrapy.Field()
    nowCasesPerMillion = scrapy.Field()
    nowDeathsPerMillion = scrapy.Field()
    nowTotalTests = scrapy.Field()
    nowTestsPerMillion = scrapy.Field()
    nowPopulation = scrapy.Field()






