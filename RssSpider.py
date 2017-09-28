# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import datetime
import PyRSS2Gen
import re


class RssSpider:
    def __init__(self, title, link, xmlpath, baseurl):
        self.myrss = PyRSS2Gen.RSS2(title=title,
                                    link=link,
                                    description=str(datetime.date.today()),
                                    pubDate=datetime.datetime.now(),
                                    lastBuildDate=datetime.datetime.now(),
                                    items=[])
        self.xmlpath=xmlpath
        self.baseurl=baseurl
        self.soup = BeautifulSoup(self.useragent(self.baseurl))
        self.itemlinks = []

    def useragent(self,url):
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", \
    "Referer": 'http://baidu.com/'}
        req = urllib2.Request(url, headers=i_headers)
        html = urllib2.urlopen(req).read()
        return html

    def enterpage(self, search_type, search_text):
        for url in self.itemlinks:
            print datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + " : " + url
            link_soup=BeautifulSoup(self.useragent(url))
            timespan=link_soup.find('div',{'class':'BlogStat'})
            timespan=str(timespan).strip().replace('\n','').decode('utf-8')
            match=re.search(r'\d{4}\S\d{2}\S\d{2}\s\d{2}\S\d{2}',timespan)
            timestr=str(datetime.date.today())
            if match:
                timestr=match.group()
            ititle=link_soup.title.string
            div=link_soup.find(search_type, search_text)
            rss=PyRSS2Gen.RSSItem(
                                  title=ititle,
                                  link=url,
                                  description=str(div),
                                  pubDate=timestr
                                  )

            self.myrss.items.append(rss)

    def search_soup(self, search_type, search_text):
        self.soup = self.soup.find(search_type, search_text)

    def get_links(self, search_type, search_text, link_type):
        for li in self.soup.find_all(search_type, search_text):
            alink = li.find(link_type)
            if alink is not None:
                link=alink.get('href')
                self.itemlinks.append(link)

    def SaveRssFile(self):
        finallxml=self.myrss.to_xml(encoding='utf-8')
        file=open(self.xmlpath,'w')
        file.writelines(finallxml)
        file.close()
