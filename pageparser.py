#!/usr/bin/env python
#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
import downloader
import time
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_jobs(html):
    main_url = 'https://www.cacareerzone.org'

    jobs_url_list = []
    soup = BeautifulSoup(html, "html.parser")
    jobs_even = soup.select('tr[class="list-item even"]')
    for x in jobs_even:
        jobs_url_list.append(main_url + x.select('td[class="list-cell"]')[1].a.get('href'))

    jobs_odd = soup.select('tr[class="list-item odd"]')
    for x in jobs_odd:
        jobs_url_list.append(main_url + x.select('td[class="list-cell"]')[1].a.get('href'))

    return jobs_url_list


def get_jobs_detail(html):
    training_list =[]
    soup = BeautifulSoup(html, "html.parser")
    pagetitle = soup.select('h2[id="pagetitle"]')[0].text.strip()

    program_profile_section = soup.select('div[class="section program-profile-section"]')

    if not program_profile_section == []:
        for x in program_profile_section[0].select('span[class="media-heading"]'):
            training_list.append(x.text)
        training  = ','.join([x for x in training_list])

    else:
        training =''



    return pagetitle,training



