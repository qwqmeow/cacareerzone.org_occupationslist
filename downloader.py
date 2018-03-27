#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests

headers = {
    'User-Agent	' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0', 
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',


}

def get_html(url, Referer_url=None):
    '''get_html(url),download and return html'''
    if Referer_url:
        headers['Referer'] = Referer_url
    req = requests.get(url, headers=None)
    return req.text
