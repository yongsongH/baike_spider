'''
Created on 2016-4-15

@author: hys mac
'''
#coding：utf8
# coding=utf-8
#import re
#import urlparse

#from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import re
import urllib.request

import urllib.parse

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):

        new_urls = set()
        # 词条url
        links = soup.find_all("a", href=re.compile(r"/view/\d+\.htm"))

        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title">

        title_node = soup.find('dd', class_ = "lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">

        summary_node = soup.find("div", class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cout):
        if page_url is None or html_cout is None:
            return

        soup = BeautifulSoup(html_cout, 'html.parser', from_encoding='utf-8')

        new_data = self._get_new_data(page_url, soup)

        new_urls = self._get_new_urls(page_url, soup)

        return new_urls, new_data
   
 
#response=urllib.request.urlopen(url)    #返回文件对象
#page=response.read()  





