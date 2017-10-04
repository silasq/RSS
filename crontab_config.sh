#!/bin/sh

sed -i "/python \/root\/RSS\/.*.py/d" /var/spool/cron/crontabs/root

echo "*/10 * * * * python /root/RSS/jiemian.py >> /var/log/rss_cron.log" >> /var/spool/cron/crontabs/root
echo "*/10 * * * * python /root/RSS/oschina.py >> /var/log/rss_cron.log" >> /var/spool/cron/crontabs/root
echo "*/10 * * * * python /root/RSS/bbtnews.py >> /var/log/rss_cron.log" >> /var/spool/cron/crontabs/root
echo "*/10 * * * * python /root/RSS/jiandan_new.py >> /var/log/rss_cron.log" >> /var/spool/cron/crontabs/root
echo "*/10 * * * * python /root/RSS/tianya_gupiao.py >> /var/log/rss_cron.log" >> /var/spool/cron/crontabs/root
echo "0 * * * * python /root/RSS/liangcang.py >> /var/log/rss_cron.log" >> /var/spool/cron/crontabs/root
echo "1 * * * * python /root/RSS/v_movie.py >> /var/log/rss_cron.log" >> /var/spool/cron/crontabs/root
echo "*/10 * * * * python /root/RSS/blogchina_top.py >> /var/log/rss_cron.log" >> /var/spool/cron/crontabs/root
echo "*/10 * * * * python /root/RSS/blogchina_focus.py >> /var/log/rss_cron.log" >> /var/spool/cron/crontabs/root
echo "*/10 * * * * python /root/RSS/pengpai.py >> /var/log/rss_cron.log" >> /var/spool/cron/crontabs/root

crontab -u root /var/spool/cron/crontabs/root