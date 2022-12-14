# define here the models for your scraped items
#
# see documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CoronavirusCurrItem(scrapy.Item):
    try:
        rankCurr = scrapy.Field()
        countryCurr = scrapy.Field()
        totalCasesCurr = scrapy.Field()
        newCasesCurr = scrapy.Field()
        totalDeathsCurr = scrapy.Field()
        newDeathsCurr = scrapy.Field()
        totalRecoveredCurr = scrapy.Field()
        newRecoveredCurr = scrapy.Field()
        activeCasesCurr = scrapy.Field()
        seriousCriticalCurr = scrapy.Field()
        casesPerMillionCurr = scrapy.Field()
        deathsPerMillionCurr = scrapy.Field()
        totalTestsCurr = scrapy.Field()
        testsPerMillionCurr = scrapy.Field()
        populationCurr = scrapy.Field()

    except Exception as ex:
        print("exception --- error in class coronavirus current item => {0}".format(ex))

class CoronavirusYestItem(scrapy.Item):
    try:
        rankYest = scrapy.Field()
        countryYest = scrapy.Field()
        totalCasesYest = scrapy.Field()
        newCasesYest = scrapy.Field()
        totalDeathsYest = scrapy.Field()
        newDeathsYest = scrapy.Field()
        totalRecoveredYest = scrapy.Field()
        newRecoveredYest = scrapy.Field()
        activeCasesYest = scrapy.Field()
        seriousCriticalYest = scrapy.Field()
        casesPerMillionYest = scrapy.Field()
        deathsPerMillionYest = scrapy.Field()
        totalTestsYest = scrapy.Field()
        testsPerMillionYest = scrapy.Field()
        populationYest = scrapy.Field()

    except Exception as ex:
        print("exception --- error in class coronavirus yesterday item => {0}".format(ex))

class Coronavirus2DaysItem(scrapy.Item):
    try:
        rank2Days = scrapy.Field()
        country2Days = scrapy.Field()
        totalCases2Days = scrapy.Field()
        newCases2Days = scrapy.Field()
        totalDeaths2Days = scrapy.Field()
        newDeaths2Days = scrapy.Field()
        totalRecovered2Days = scrapy.Field()
        newRecovered2Days = scrapy.Field()
        activeCases2Days = scrapy.Field()
        seriousCritical2Days = scrapy.Field()
        casesPerMillion2Days = scrapy.Field()
        deathsPerMillion2Days = scrapy.Field()
        totalTests2Days = scrapy.Field()
        testsPerMillion2Days = scrapy.Field()
        population2Days = scrapy.Field()

    except Exception as ex:
        print("exception --- error in class coronavirus 2 days item => {0}".format(ex))

class PopulationItem(scrapy.Item):
    try:
        country = scrapy.Field()
        population = scrapy.Field()
        yearlyChange = scrapy.Field()
        netChange = scrapy.Field()
        density = scrapy.Field()
        landArea = scrapy.Field()
        migrants = scrapy.Field()
        fertilizationRate = scrapy.Field()
        medianAge = scrapy.Field()
        urbanPopPercent = scrapy.Field()
        worldShare = scrapy.Field()

    except Exception as ex:
        print("exception --- error in class population item => {0}".format(ex))







