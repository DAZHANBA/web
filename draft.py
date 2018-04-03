# -*- coding: utf-8 -*-
"""

"""

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re
from selenium import webdriver as wb
import urllib

url_ip = "https://ip.cn"

chrome_driver_path = r'C:\Users\1022532\Documents\python_project\chrome driver\chromedriver.exe'
d = wb.Chrome(chrome_driver_path)
d.get(url_ip)
tmp = d.page_source
d.quit()
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re
from selenium import webdriver as wb
import urllib

url_ip = "https://ip.cn"

chrome_driver_path = r'C:\Users\1022532\Documents\python_project\chrome driver\chromedriver.exe'
d=wb.Chrome(chrome_driver_path)
d.get(url_ip)
with open("page_source.html","w") as f:
    f.write(d.page_source)
"""

pat_ip = re.compile(
    ur'.*<p>您现在的 IP：<code>(?P<IP>.*)</code></p><p>所在地理位置：<code>(?P<geo>.*)</code></p><p>GeoIP:(?P<geoIP>.*)</p>.*',
    re.I)

mod = pat_ip.search(tmp)


if __name__ == '__main__':
    print tmp
    print 'mod %s' %mod
    print mod.groupdict()