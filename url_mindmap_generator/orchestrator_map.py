# Owner: Guru
# Purpose: Connect all modules.

import web_scrapper as ws
import ai_plugin as ai
import mind_maps as mp

class Orchestrator():

    content_json = {}
    anchor_json = {}
    def generate_mindmap(self,url, user_prompt):
        scrapper_object = ws.web_scrapper()
        head_json,anchor_json  = scrapper_object.scrape_website(url)

        ai_skills = ai.AISkill()
        ai_skills.generate_subtopics(head_json, user_prompt)
        return self.content_json, self.anchor_json

if __name__ == "__main__":
    orchestrator_object =Orchestrator()
    orchestrator_object.generate_mindmap("https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles","test")