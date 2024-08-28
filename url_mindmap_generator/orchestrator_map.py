import web_scrapper as ws
import ai_plugin as ai
import mind_maps as mp

class Orchestrator():
    def generate_mindmap(self,url):
        scrapper_object = ws.web_scrapper()
        scrapper_object.scrape_website(url)

if __name__ == "__main__":
    orchestrator_object =Orchestrator()
    orchestrator_object.generate_mindmap("abc")