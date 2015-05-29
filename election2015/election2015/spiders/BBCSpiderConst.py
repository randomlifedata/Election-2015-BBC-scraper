# -*- coding: utf-8 -*-
# DATA.GOV.HK Datasets Scraper
# Sammy Fung <sammy@sammy.hk>
import scrapy
import csv
from election2015.items import BBCConstItem

class BBCSpiderConst(scrapy.Spider):
  name = "bbcconst"
  allowed_domains = ["bbc.co.uk"]
  start_urls = list()

  with open('constituencies.csv', 'rU') as csvfile:
    conreader = csv.reader(csvfile, delimiter=',')
    for row in conreader:
      start_urls.append('http://www.bbc.com/news/politics/constituencies/'+row[1])


  def parse(self, response):


    item =BBCConstItem()

    constituency_code = response.xpath("//a[contains(@data-target-url, 'http://www.bbc.com/news/politics/constituencies/')]/@data-target-url").extract()
    constituency_code = constituency_code[0].replace('http://www.bbc.com/news/politics/constituencies/','')

    item['constituency_code'] = constituency_code

    majority = response.xpath("//div[contains(@class,'results-turnout__majority')]/span[contains(@class,'results-turnout__label')]/text()").extract()
    item['majority'] = majority[0].replace(' majority:','')

    turnout = response.xpath("//div[contains(@class,'results-turnout__percentage')]/span[contains(@class,'results-turnout__value results-turnout__value--right')]/text()").extract()
    turnout = turnout[0].replace('%','')
    item['turnout'] = turnout

    item['labour_candidate'] = None
    item['labour_vote'] = None
    item['labour_share'] = None
    item['labour_swing'] = None

    item['conservative_candidate'] = None
    item['conservative_vote'] = None
    item['conservative_share'] = None
    item['conservative_swing'] = None

    item['libdem_candidate'] = None
    item['libdem_vote'] = None
    item['libdem_share'] = None
    item['libdem_swing'] = None

    item['ukip_candidate'] = None
    item['ukip_vote'] = None
    item['ukip_share'] = None
    item['ukip_swing'] = None

    item['green_candidate'] =None 
    item['green_vote'] = None
    item['green_share'] = None
    item['green_swing'] = None

    item['snp_candidate'] = None
    item['snp_vote'] = None
    item['snp_share'] = None
    item['snp_swing'] = None

    parties = response.xpath("//div[re:test(@class, 'parties')]")
    party = parties.xpath("div[contains(@class, 'party')]")

    for index, p in enumerate(party):     
      party_name = p.xpath("div/div[contains(@class,'party__name--long')]/text()").extract()
      party_name = party_name[0]

      if party_name == "Labour":
        item['labour_candidate'] = p.xpath("div/div[contains(@class, 'party__result--candidate')]/text()").extract()[0]
        vote = p.xpath("ul/li[contains(@class,'party__result--votes essential')]/text()").extract()
        item['labour_vote'] = vote[0].replace(',','')
        item['labour_share'] = p.xpath("ul/li[contains(@class,'party__result--votesshare essential')]/text()").extract()[0]
        item['labour_swing'] = p.xpath("ul/li[contains(@class,'party__result--votesnet essential')]/span[not(contains(@class,'off-screen'))]/text()").extract()[0].replace('+','')
      elif party_name =="Conservative":
        item['conservative_candidate'] = p.xpath("div/div[contains(@class, 'party__result--candidate')]/text()").extract()[0]
        vote = p.xpath("ul/li[contains(@class,'party__result--votes essential')]/text()").extract()
        item['conservative_vote'] = vote[0].replace(',','')
        item['conservative_share'] = p.xpath("ul/li[contains(@class,'party__result--votesshare essential')]/text()").extract()[0]
        item['conservative_swing'] = p.xpath("ul/li[contains(@class,'party__result--votesnet essential')]/span[not(contains(@class,'off-screen'))]/text()").extract()[0].replace('+','')
      elif party_name =="Liberal Democrat":
        item['libdem_candidate'] = p.xpath("div/div[contains(@class, 'party__result--candidate')]/text()").extract()[0]
        vote = p.xpath("ul/li[contains(@class,'party__result--votes essential')]/text()").extract()
        item['libdem_vote'] = vote[0].replace(',','')
        item['libdem_share'] = p.xpath("ul/li[contains(@class,'party__result--votesshare essential')]/text()").extract()[0]
        item['libdem_swing'] = p.xpath("ul/li[contains(@class,'party__result--votesnet essential')]/span[not(contains(@class,'off-screen'))]/text()").extract()[0].replace('+','')
      elif party_name =="UKIP":
        item['ukip_candidate'] = p.xpath("div/div[contains(@class, 'party__result--candidate')]/text()").extract()[0]
        vote = p.xpath("ul/li[contains(@class,'party__result--votes essential')]/text()").extract()
        item['ukip_vote'] = vote[0].replace(',','')
        item['ukip_share'] = p.xpath("ul/li[contains(@class,'party__result--votesshare essential')]/text()").extract()[0]
        item['ukip_swing'] = p.xpath("ul/li[contains(@class,'party__result--votesnet essential')]/span[not(contains(@class,'off-screen'))]/text()").extract()[0].replace('+','')
      elif party_name=="Green Party":
        item['green_candidate'] = p.xpath("div/div[contains(@class, 'party__result--candidate')]/text()").extract()[0]
        vote = p.xpath("ul/li[contains(@class,'party__result--votes essential')]/text()").extract()
        item['green_vote'] = vote[0].replace(',','')
        item['green_share'] = p.xpath("ul/li[contains(@class,'party__result--votesshare essential')]/text()").extract()[0]
        item['green_swing'] = p.xpath("ul/li[contains(@class,'party__result--votesnet essential')]/span[not(contains(@class,'off-screen'))]/text()").extract()[0].replace('+','')
      elif party_name=="Scottish National Party":
        item['snp_candidate'] = p.xpath("div/div[contains(@class, 'party__result--candidate')]/text()").extract()[0]
        vote = p.xpath("ul/li[contains(@class,'party__result--votes essential')]/text()").extract()
        item['snp_vote'] = vote[0].replace(',','')
        item['snp_share'] = p.xpath("ul/li[contains(@class,'party__result--votesshare essential')]/text()").extract()[0]
        item['snp_swing'] = p.xpath("ul/li[contains(@class,'party__result--votesnet essential')]/span[not(contains(@class,'off-screen'))]/text()").extract()[0].replace('+','')
    yield item

