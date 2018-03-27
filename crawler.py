#!/usr/bin/env python
#-*-coding:utf-8-*-

import controler
import downloader
import pageparser
import time
import sqlite3
import string
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')






def main(entrance):
    
    print "entrance:{}".format(entrance)

    entrance_html = downloader.get_html(entrance)
    jobs_url_list = pageparser.get_jobs(entrance_html)

    for jobs_url in jobs_url_list:
        
        print 'jobs_url:{}'.format(jobs_url)
        jobs_html = downloader.get_html(jobs_url)
        pagetitle,training = pageparser.get_jobs_detail(jobs_html)

        controler.write_data(pagetitle,training)
            # print 'pagetitle:{},training:{}'.format(pagetitle, training)



if __name__ == '__main__':
    main('https://www.cacareerzone.org/occupations/list')
