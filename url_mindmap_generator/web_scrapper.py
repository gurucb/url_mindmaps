# Owner: Anil / Guru
# Purpose: Scrape Web Page (given a URL and extract)
# 1. Headers as JSON
# 2. Anchors as JSON

from bs4 import BeautifulSoup, ResultSet
import requests
import json

class web_scrapper():
    soup = None
    BeautifulSoup
    def scrape_website(self,url):
        # Check if it is valid URL
        assert(len(url) > 0)
        assert(str(url).__contains__("http"))

        self.response = requests.get(url=url)
        self.soup = BeautifulSoup(self.response.content,"html.parser")
        self.soup.builder = "lxml"
        head_json = self.extract_headers()
        anchors_json = self.extract_anchors(url)
        
        
        return head_json, anchors_json

    def extract_headers(self ):
        headers = []
        self.h1 = self.soup.h1
        h1 = {}
        h1["h_type"]  = self.h1.name
        h1["text"] = self.h1.contents
        headers.append(h1)
        self.h2 = self.soup.find_all("h2",recursive=True)
        for h in self.h2:
            h2 = {}
            h2["h_type"] =  h.name 
            h2["text"] = h.contents             
            headers.append(h2)
            h2 = None
        head_json = json.dumps(headers)
        return head_json
    def extract_anchors(self,url):
        anchors = {}
        return anchors
    def clean_anchors(self,url):
        pass
    def extract_all_content(self, url):
        pass
    def clean_response(self,url):
        pass

    def clean_headers():
        pass