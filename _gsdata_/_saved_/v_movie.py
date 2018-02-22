# -*- coding: utf-8 -*-

from RssSpider import RssSpider

if __name__ == '__main__':
    rssSpider = RssSpider(title='v电影',
                          link=r'http://www.vmovier.com/',
                          xmlpath=r'/var/www/html/v_movie.xml',
                          baseurl=r"http://www.vmovier.com/")
    rssSpider.search_soup('div', {'class': 'index-main'})
    rssSpider.get_links('li', search_text='', link_type='a')
    rssSpider.add_link_head('http://www.vmovier.com')
    rssSpider.enterpage('div',{'id': 'main-container'})
    rssSpider.SaveRssFile()