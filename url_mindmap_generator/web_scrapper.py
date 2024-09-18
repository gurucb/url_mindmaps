# Owner:  Guru
# Purpose: Scrape Web Page (given a URL and extract)
# 1. Headers as JSON
# 2. Anchors as JSON

from bs4 import BeautifulSoup, ResultSet
from bs4.element import Comment
import requests
import urllib
import json
import os

class web_scrapper():
    soup = None
    content = None
    headings_json = {}
    page_links = []
    def scrape_website(self,url):
        # Check if it is valid URL
        assert(len(url) > 0)
        assert(str(url).__contains__("http"))

        self.response = requests.get(url=url)
        self.soup = BeautifulSoup(self.response.content,"html.parser")
        self.soup.builder = "lxml"
        self.headings_json = self.extract_headers()
        self.page_links = self.extract_anchors(url)
        self.clean_headers()
        self.content = self.extract_all_content(url)
        self.content = self.content.replace(" "," ")
        return self.headings_json, self.page_links, self.content

    def extract_headers(self ):
        headers = {}
        h1 = []
        h2 = []
        h1s = self.soup.find_all("h1",recursive=True)
        for item in h1s:
            heading_1 = {}
            heading_1['h_type']  = item.name
            heading_1['id'] = item.id
            heading_1['text'] = item.contents
            h1.append(heading_1)
            heading_1=None
        headers['h1'] = h1
        h2s = self.soup.find_all("h2",recursive=True)
        for item in h2s:
            heading_2 = {}
            heading_2['h_type'] =  item.name
            heading_2['id'] = item.id 
            heading_2['text'] = item.contents             
            h2.append(heading_2)
            heading_2 = None
        headers["h2"] = h2
        return headers
    def extract_anchors(self,url):
        anchors = []
        links = self.soup.find_all('a',recursive=True)
        for  link in links:
            anchor =  {}
            anchor["name"] = link.name
            anchor["text"] = link.get_text()
            if link.get('href') != None:
                if 'https://' in link.get('href'):
                    anchor["href"] = link.get_text()
                else:
                    anchor["href"] = "None"
            anchor['attrs'] = link.attrs

            anchors.append(anchor)
            anchor = None
        return anchors
    def is_noise_anchor(self,url) -> bool:
        is_noise_anchor = False
    def clean_anchors(self,url):
        pass
    def tag_visible(self,element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True
    def extract_all_content(self,url):
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        texts = soup.findAll(text=True)
        # Filter out unwanted tags
        visible_texts = filter(self.tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)
    def clean_response(self,url):
        pass

    # TODO: Need better implementation 
    # Cleanup further like remove Tags
    # using Word2Vec
    def clean_headers(self):
        json_cleaned = {}
        h1s = list(self.headings_json['h1'])
        h1s_orig = h1s
        h2s = list(self.headings_json['h2'])
        h2s_orig = h2s
        stop_words = ['article','feedback','next','resources','see','references','external','notes']
        for word in stop_words:
            # for h1 in h1s_orig:
            #     if str.lower(h1['text'][0]).find(str.lower(word)) != -1:
            #         h1s.remove(h1)
            for h2 in h2s_orig:
                if str.lower(h2['text'][0]).find(str.lower(word)) != -1:
                    h2s.remove(h2)
        
        self.headings_json['h1'] = h1s
        self.headings_json['h2'] = h2s
        
