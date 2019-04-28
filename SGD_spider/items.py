# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GeneItem(scrapy.Item):
    # define the fields for your item here like:
    StandardName = scrapy.Field()
    SysName = scrapy.Field()
    SGD_ID = scrapy.Field()
    FeatureType = scrapy.Field()
    Description = scrapy.Field()
    #Chr_loc = scrapy.Field()
    NameDesc = scrapy.Field()
    MolFunc = scrapy.Field()
    BioProc = scrapy.Field()
    CellComp = scrapy.Field()

    # Interactions
    # Regulators
