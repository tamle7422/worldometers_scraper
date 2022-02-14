# define here the models for your scraped items
#
# see documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CoronaItem(scrapy.Item):
    nowCountry = scrapy.Field()
    nowTotalCases = scrapy.Field()
    nowNewCases = scrapy.Field()
    nowTotalDeaths = scrapy.Field()
    nowNewDeaths = scrapy.Field()
    nowTotalRecovered = scrapy.Field()