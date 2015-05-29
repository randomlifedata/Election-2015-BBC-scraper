# -*- coding: utf-8 -*-
# DATA.GOV.HK Datasets Scraper
# Sammy Fung <sammy@sammy.hk>
import scrapy
import csv
from election2015.items import BBCPartyItem

class BBCSpider(scrapy.Spider):
  name = "bbcparty"
  allowed_domains = ["bbc.co.uk"]
  start_urls = list()

  with open('constituencies.csv', 'rU') as csvfile:
    conreader = csv.reader(csvfile, delimiter=',')
    for row in conreader:
      start_urls.append('http://www.bbc.com/news/politics/constituencies/'+row[1])


  def parse(self, response):
    constituency_code = response.xpath("//a[contains(@data-target-url, 'http://www.bbc.com/news/politics/constituencies/')]/@data-target-url").extract()
    constituency_code = constituency_code[0].replace('http://www.bbc.com/news/politics/constituencies/','')

    turnout = response.xpath("//div[contains(@class,'results-turnout__percentage')]/span[contains(@class,'results-turnout__value results-turnout__value--right')]/text()").extract()[0].replace('%','')

    parties = response.xpath("//div[re:test(@class, 'parties')]")
    party = parties.xpath("div[contains(@class, 'party')]")

    for index, p in enumerate(party):
      item = BBCPartyItem()
      item['constituency_code'] = constituency_code
      item['turnout'] = turnout
      item['party_name'] = p.xpath("div/div[contains(@class,'party__name--long')]/text()").extract()[0]
      item['party_candidate'] = p.xpath("div/div[contains(@class, 'party__result--candidate')]/text()").extract()[0]
      item['party_vote'] = p.xpath("ul/li[contains(@class,'party__result--votes essential')]/text()").extract()[0].replace(',','')
      item['party_share'] = p.xpath("ul/li[contains(@class,'party__result--votesshare essential')]/text()").extract()[0]
      item['party_swing'] = p.xpath("ul/li[contains(@class,'party__result--votesnet essential')]/span[not(contains(@class,'off-screen'))]/text()").extract()[0].replace('+','')

      yield item

