# -*- coding: utf-8 -*-

from RssSpider import RssSpider

if __name__ == '__main__':
    rssSpider = RssSpider(title='良仓',
                          link=r'http://www.iliangcang.com/',
                          xmlpath=r'/var/www.html/liangcang.xml',
                          baseurl=r"http://iliangcang.com/i/topic/")
    rssSpider.search_soup('div', {'id': 'main'})
    rssSpider.get_links('div', {'class': 'imgCon'}, 'a')
    rssSpider.enterpage('div',{'class': 'topic_cont'})
    rssSpider.SaveRssFile()