# -*- coding: utf-8 -*-
"""
TODO: all config in xml
"""

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re
from selenium import webdriver as wb
import urllib2
import StringIO
import gzip

header = {'User-Agent': r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0',
            'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': r'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': r'gzip, deflate',
            'Referer': r'https://www.baidu.com'
        }
"""
headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
"""
opener = urllib2.build_opener() # urllib.request.build_opener()
opener.addheaders = header.items() # opener.addheaders(list)

urllib2.install_opener(opener) # urllib.request.install_opener(opener)


url_ip = "https://ip.cn"

file = urllib2.urlopen(url_ip)
data = str(file.read())


"""
import StringIO, gzip
def decode(content):
    stream = StringIO.StringIO(content)
    with gzip.GzipFile(fileobj = stream) as f:
        fdata = f.read()
    return fdata

req = urllib2.Request(url, None, header)
albumpage = decode(urllib2.urlopen(req, None, req_timeout).read())

chrome_driver_path = r'/Users/24BC/Documents/python_project/webdriver/chromedriver'

d = wb.Chrome(chrome_driver_path)
d.get(url_ip)
tmp = d.page_source
d.quit()
"""
def decode(content):
    stream = StringIO.StringIO(content)
    with gzip.GzipFile(fileobj = stream) as f:
        fdata = f.read()
    return fdata


pat_ip = re.compile(
    r'<p>您现在的 IP：<code>(?P<IP>.*)</code></p><p>所在地理位置：<code>(?P<geo>.*)</code></p><p>GeoIP:(?P<geoIP>.*)</p>',
    re.I)
"""
for driver.page_source 
pat_ip = re.compile(
    ur'<p>您现在的 IP：<code>(?P<IP>.*)</code></p><p>所在地理位置：<code>(?P<geo>.*)</code></p><p>GeoIP:(?P<geoIP>.*)</p>',
    re.I)
only for self-defined decode func, use r''
TODO: try to figure it out why
"""


mod = pat_ip.search(decode(data))

if __name__ == '__main__':
    print 'mod %s' %mod
    try:
        print mod.groupdict()
    except:
        print data





