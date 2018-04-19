# -*- coding: utf-8 -*-
"""
load basic config and func
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import xml.dom.minidom
import re
import os

def trim(string):
    return re.sub(r' |\n','',string)

DOMTree = xml.dom.minidom.parse("config.xml")
collection = DOMTree.documentElement
LOG = trim((collection.getElementsByTagName("log")[0]).childNodes[0].data)

PATH_SCRIPT = sys.path[0]
PATH_LOG = os.path.join(PATH_SCRIPT,LOG) 

print PATH_LOG


def file_write(content,file_name,mode='w'):
    with open(PATH_SCRIPT+'\\'+file_name,mode) as f:
        f.write(content)
    print 'Content has been written to %s' %file_name
    

def log_step(v_step, v_log, log_name='log.txt'):
    tmp_v_log = u"<%s> #%s: %s\n" %(time.ctime(), v_step, v_log)
    print tmp_v_log
    file_write(tmp_v_log,log_name,'a')
    return  tmp_v_log







