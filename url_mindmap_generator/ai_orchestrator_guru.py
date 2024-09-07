import json
from ai_cleanup_guru import DataCleanup as dc
from cleantext import clean

class AI_Orchstrator:
    heading_json = None
    links_json = None
    content = None
    def __init__(self,heading_json,links_json,content) -> None:
        self.heading_json = heading_json
        self.links_json = links_json
        self.content = content
        content = clean(content,extra_spaces=True,lowercase=True,numbers=True)
        with open("content.txt","a") as f:
            f.write(self.content)
            f.write("\n\n")
            f.write(content)
    def parse_content(self) -> json:
        data_cleanup = dc.DataCleanup(content=self.content)

    def generate_page_summary(self):
        pass

    def generate_topics_with_summary(self):
        pass

    def generate_subtopics_with_summary(self):
        pass
    
    def generate_response_json(self):
        pass
