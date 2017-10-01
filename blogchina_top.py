# -*- coding: utf-8 -*-

from RssSpider import RssSpider

if __name__ == '__main__':
    rssSpider = RssSpider(title='博客中国-头条',
                          link=r'http://www.blogchina.com/',
                          xmlpath=r'/var/www/html/blogchina_top.xml',
                          baseurl=r"http://tuijian.blogchina.com/list/index/flag/2/channel/1")
    rssSpider.search_soup('div', {'class': 'news_toplist_left'})
    rssSpider.get_links('li', {'class': 'tit_a'}, 'a')
    rssSpider.enterpage('div',{'class': 'article'})
    rssSpider.replace('alt=""','')
    rssSpider.SaveRssFile()