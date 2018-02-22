# -*- coding: utf-8 -*-

from RssSpider import RssSpider

if __name__ == '__main__':
    rssSpider = RssSpider(title='OSChina',
                          link=r'http://my.oschina.net/',
                          xmlpath=r'/var/www/html/oschina_new.xml',
                          baseurl=r"http://www.oschina.net/blog/")
    rssSpider.search_soup('div', {'id': 'listContent'})
    rssSpider.get_links('div', {'class': 'news_li'}, 'a')
    rssSpider.add_link_head('http://www.thepaper.cn/')
    rssSpider.enterpage('div', {'class': 'news_txt'})
    rssSpider.replace('alt=""', '')
    rssSpider.SaveRssFile()
