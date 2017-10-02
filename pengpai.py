# -*- coding: utf-8 -*-

from RssSpider import RssSpider

if __name__ == '__main__':
    rssSpider = RssSpider(title='澎湃新闻',
                          link=r'http://www.thepaper.cn/',
                          xmlpath=r'/var/www/html/pengpai.xml',
                          baseurl=r"http://www.thepaper.cn/")
    rssSpider.search_soup('div', {'id': 'listContent'})
    rssSpider.get_links('div', {'class': 'news_li'}, 'a')
    rssSpider.add_link_head('http://www.thepaper.cn/')
    rssSpider.enterpage('div', {'class': 'newscontent'})
    rssSpider.replace('alt=""', '')
    rssSpider.SaveRssFile()
