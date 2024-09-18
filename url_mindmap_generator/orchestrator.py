# Owner: Guru
# Purpose: Connect all modules.

import web_scrapper as ws
import ai_plugin as ai
import mind_maps as mp
import ai_orchestrator as og
import json

class Orchestrator():

    anchor_json = {}
    url_json = {}
    content = None
    def generate_mindmap(self,url, user_prompt):
        scrapper_object = ws.web_scrapper()
        head_json,url_json, content  = scrapper_object.scrape_website(url)
        aiog = og.AI_Orchestrator("gpt35")
        self.content_json = aiog.generate_content_JSON(heading_json=head_json,links_json=url_json,content=content,user_prompt=user_prompt)
        self.content_json = str(self.content_json).encode("ascii","ignore")
        self.content_json = self.content_json.decode()
        print("IN.................................")
        print(self.content_json)
        return self.content_json

if __name__ == "__main__":
    orchestrator_object =Orchestrator()
    links = [
        "https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing?tabs=web",
        "https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles",
        # "https://en.wikipedia.org/wiki/Microsoft",
        # "http://www.nytimes.com/2009/12/21/us/21storm.html"
        "https://openai.com/index/learning-to-reason-with-llms/",
        "https://medium.com/@heyshrutimishra/10-nvidia-ai-courses-that-you-cannot-afford-to-miss-in-2024-968882f767d3",
        "https://azure.microsoft.com/en-us/blog/introducing-o1-openais-new-reasoning-model-series-for-developers-and-enterprises-on-azure/"
    ]
    orchestrator_object.generate_mindmap(links[1],"Spanish")

    # orchestrator_object.generate_mindmap(,"English")
    # ''