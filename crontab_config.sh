#!/bin/sh

pip install bs4
pip install PyRSS2Gen

echo "import sys" >> /usr/lib/python2.7/site-packages/sitecustomize.py
echo "sys.setdefaultencoding('utf-8')" >> /usr/lib/python2.7/site-packages/sitecustomize.py

sed -i "/python \/root\/RSS\/.*.py/d" /var/spool/cron/root 

echo "*/10 * * * * python /root/RSS/jiemian.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "*/10 * * * * python /root/RSS/oschina.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "*/10 * * * * python /root/RSS/bbtnews.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "*/10 * * * * python /root/RSS/jiandan_new.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "*/10 * * * * python /root/RSS/tianya_gupiao.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "0 * * * * python /root/RSS/liangcang.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "1 * * * * python /root/RSS/v_movie.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "*/10 * * * * python /root/RSS/blogchina_top.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "*/10 * * * * python /root/RSS/blogchina_focus.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "*/10 * * * * python /root/RSS/pengpai.py >> /var/log/rss_cron.log" >> /var/spool/cron/root

crontab -u root /var/spool/cron/root


yum -y install httpd
