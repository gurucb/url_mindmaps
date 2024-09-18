# Owner: Guru
# Purpose: Connect all modules.

import web_scrapper as ws
import ai_plugin as ai
import mind_maps as mp
import ai_orchestrator as og

class Orchestrator():

    anchor_json = {}
    url_json = {}
    content = None
    def generate_mindmap(self,url, user_prompt):
        scrapper_object = ws.web_scrapper()
        head_json,url_json, content  = scrapper_object.scrape_website(url)
        aiog = og.AI_Orchestrator("gpt35")
        self.content_json = aiog.generate_content_JSON(heading_json=head_json,links_json=url_json,content=content,user_prompt=user_prompt)
        # ai_skills = ai.create_content(head_json, user_prompt, web_content)
        # ai_skills.generate_subtopics(head_json, user_prompt)
        return self.content_json

if __name__ == "__main__":
    orchestrator_object =Orchestrator()
    orchestrator_object.generate_mindmap("https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles","French")
    # orchestrator_object.generate_mindmap("https://en.wikipedia.org/wiki/Microsoft","tst")
    # 'http://www.nytimes.com/2009/12/21/us/21storm.html'