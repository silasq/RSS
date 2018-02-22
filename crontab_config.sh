#!/bin/sh


if ! pip show bs4|grep -q "^Version" ;then
    pip install bs4
fi

if ! pip show PyRSS2Gen|grep -q "^Version" ;then
    pip install PyRSS2Gen
fi


# 配置全局utf-8编码
if ! grep -q "^import sys" /usr/lib/python2.7/site-packages/sitecustomize.py ;then
    echo "import sys" >> /usr/lib/python2.7/site-packages/sitecustomize.py
fi
if ! grep -q "^sys.setdefaultencoding('utf-8')" /usr/lib/python2.7/site-packages/sitecustomize.py ;then
    echo "sys.setdefaultencoding('utf-8')" >> /usr/lib/python2.7/site-packages/sitecustomize.py
fi

# 配置rss crontab
sed -i "/python \/root\/RSS\/.*.py/d" /var/spool/cron/root 

# 每小时
echo "0 * * * * python /root/RSS/jiemian.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "2 * * * * python /root/RSS/oschina.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "4 * * * * python /root/RSS/bbtnews.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "6 * * * * python /root/RSS/pengpai.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "8 * * * * python /root/RSS/diyicaijing.py >> /var/log/rss_cron.log" >> /var/spool/cron/root

# 每天
echo "0 0 * * * python /root/RSS/liangcang.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "5 0 * * * python /root/RSS/v_movie.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "10 0 * * * python /root/RSS/jiandan_new.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "15 0 * * * python /root/RSS/blogchina_top.py >> /var/log/rss_cron.log" >> /var/spool/cron/root
echo "20 0 * * * python /root/RSS/blogchina_focus.py >> /var/log/rss_cron.log" >> /var/spool/cron/root



#echo "*/10 * * * * python /root/RSS/tianya_gupiao.py >> /var/log/rss_cron.log" >> /var/spool/cron/root

crontab -u root /var/spool/cron/root

# 安装apache
if ! rpm -q --quiet httpd;then
    yum -y install httpd
fi
