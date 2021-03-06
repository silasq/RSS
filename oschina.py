# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import urllib2

import datetime
import time
import PyRSS2Gen
from email.Utils import formatdate
import re
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')




class RssSpider():
    def __init__(self):
        self.myrss = PyRSS2Gen.RSS2(title='OSChina',
                                    link='http://my.oschina.net',
                                    description=str(datetime.date.today()),
                                    pubDate=datetime.datetime.now(),
                                    lastBuildDate = datetime.datetime.now(),
                                    items=[]
                                    )
        self.xmlpath=r'/var/www/html/oschina.xml'

        self.baseurl="http://www.oschina.net/blog"
        #if os.path.isfile(self.xmlpath):
            #os.remove(self.xmlpath)
    def useragent(self,url):
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", \
    "Referer": 'http://baidu.com/'}
        req = urllib2.Request(url, headers=i_headers)
        html = urllib2.urlopen(req).read()
        return html
    def enterpage(self,url):
        pattern = re.compile(r'\d{4}\S\d{2}\S\d{2}\s\d{2}\S\d{2}')
        rsp=self.useragent(url)
        soup=BeautifulSoup(rsp)
        timespan=soup.find('div',{'class':'BlogStat'})
        timespan=str(timespan).strip().replace('\n','').decode('utf-8')
        match=re.search(r'\d{4}\S\d{2}\S\d{2}\s\d{2}\S\d{2}',timespan)
        timestr=str(datetime.date.today())
        if match:
            timestr=match.group()
            #print timestr
        ititle=soup.title.string
        div=soup.find('div',{'class':'blog-body'})
        rss=PyRSS2Gen.RSSItem(
                              title=ititle,
                              link=url,
                              description = str(div),
                              pubDate = timestr
                              )

        return rss
    def getcontent(self):
        rsp=self.useragent(self.baseurl)
        soup=BeautifulSoup(rsp)
        ul=soup.find('div',{'id':'topsOfRecommend'})
        #for li in ul.findAll('box-aw'):
        for li in ul.findAll('div',{'class':'box-aw'}):
            alink=li.find('a')
            if alink is not None:
                link=alink.get('href')
                print datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + " : " + link
                html=self.enterpage(link)
                self.myrss.items.append(html)
    def SaveRssFile(self,filename):
        finallxml=self.myrss.to_xml(encoding='utf-8')
        file=open(self.xmlpath,'w')
        file.writelines(finallxml)
        file.close()



if __name__=='__main__':
    rssSpider=RssSpider()
    rssSpider.getcontent()
    rssSpider.SaveRssFile('oschina.xml')