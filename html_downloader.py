'''
Created on 2016-4-15

@author: hys mac
'''
#coding：utf8
#import urllib2
import urllib.request
import urllib
import http



class HtmlDownloader(object):

    def downloader(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None
        return response.read()

