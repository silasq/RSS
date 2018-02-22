# -*- coding: utf-8 -*-

from RssSpider import RssSpider

if __name__ == '__main__':
    rssSpider = RssSpider(title='煎蛋',
                          link=r'http://jandan.net/',
                          xmlpath=r'/var/www/html/jiandan_new.xml',
                          baseurl=r"http://jandan.net/")
    rssSpider.search_soup('div', {'id': 'content'})
    rssSpider.get_links('div', {'class': 'thumbs_b'}, 'a')
    rssSpider.enterpage('div', {'id': 'content'})
    rssSpider.replace('data-original="','src="http:')
    rssSpider.SaveRssFile()
