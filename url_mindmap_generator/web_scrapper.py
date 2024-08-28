# Owner: Anil / Guru
# Purpose: Scrape Web Page (given a URL and extract)
# 1. Headers as JSON
# 2. Anchors as JSON

class web_scrapper():
    def scrape_website(self,url):
        head_json = self.extract_headers(url)
        anchors_json = self.extract_anchors(url)
        return head_json, anchors_json

    def extract_headers(self, url):
        headers = {}
        return headers
    def extract_anchors(self,url):
        anchors = {}
        return anchors
    def clean_anchors(self,url):
        pass

    def clean_response(self,url):
        pass

    def clean_headers():
        pass