# Owner: Guru
# Purpose: Connect all modules.

import web_scrapper as ws
import ai_plugin as ai
import mind_maps as mp

class Orchestrator():
    def generate_mindmap(self,url, user_prompt):
        scrapper_object = ws.web_scrapper()
        head_json,anchor_json  = ws.scrape_website(url)

        ai_skills = ai.AISkill()
        ai_skills.generate_subtopics(head_json, user_prompt)


if __name__ == "__main__":
    orchestrator_object =Orchestrator()
    orchestrator_object.generate_mindmap("abc")