# -*- coding: utf-8 -*-

from RssSpider import RssSpider

if __name__ == '__main__':
    rssSpider = RssSpider(title='第一财经',
                          link=r'http://www.yicai.com/',
                          xmlpath=r'/var/www/html/diyicaijing.xml',
                          baseurl=r"http://www.yicai.com/news/")
    rssSpider.search_soup('div', {'id': 'news_List'})
    rssSpider.get_links('dt',search_text='',link_type='a')
    rssSpider.enterpage('div', {'class': 'm-text'})
    rssSpider.replace('alt=""', '')
    rssSpider.SaveRssFile()
