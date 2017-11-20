from scrapy import cmdline
# cmdline.execute('scrapy crawl meizi'.split())

import os
os.chdir('meizitu/spiders')
cmdline.execute('scrapy runspider meizi_redis.py'.split())