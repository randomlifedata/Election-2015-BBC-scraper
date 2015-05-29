# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Election2015Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class BBCPartyItem(scrapy.Item):
	constituency_code = scrapy.Field()
	turnout = scrapy.Field()
	party_candidate = scrapy.Field()
	party_name = scrapy.Field()
	party_vote = scrapy.Field()
	party_share = scrapy.Field()
	party_swing = scrapy.Field()


class BBCConstItem(scrapy.Item):
	constituency_code = scrapy.Field()
	majority = scrapy.Field()
	turnout = scrapy.Field()
	labour_candidate = scrapy.Field()
	labour_vote = scrapy.Field()
	labour_share = scrapy.Field()
	labour_swing = scrapy.Field()
	conservative_candidate = scrapy.Field()
	conservative_vote = scrapy.Field()
	conservative_share = scrapy.Field()
	conservative_swing = scrapy.Field()
	libdem_candidate = scrapy.Field()
	libdem_vote = scrapy.Field()
	libdem_share = scrapy.Field()
	libdem_swing = scrapy.Field()
	green_candidate = scrapy.Field()
	green_vote = scrapy.Field()
	green_share = scrapy.Field()
	green_swing = scrapy.Field()
	ukip_candidate = scrapy.Field()
	ukip_vote = scrapy.Field()
	ukip_share = scrapy.Field()
	ukip_swing = scrapy.Field()
	snp_candidate = scrapy.Field()
	snp_vote = scrapy.Field()
	snp_share = scrapy.Field()
	snp_swing = scrapy.Field()

