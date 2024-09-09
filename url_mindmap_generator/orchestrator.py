# Owner: Guru
# Purpose: Connect all modules.

import web_scrapper as ws
import ai_plugin as ai
import mind_maps as mp
import ai_orchestrator_guru as og

class Orchestrator():

    #content_json = {}
    content_json="{\"page_summary\":\"FullPageSummaryofthegivenURL\",\"content\":\"content\",\"topics\":[{\"name\":\"firsttopic\",\"sub_topics\":[{\"name\":\"firstsubtopic\",\"text\":\"Firstcsubtopictext\"},{\"name\":\"firstsubtopic\",\"text\":\"Firstcsubtopictext\"},{\"name\":\"firstsubtopic\",\"text\":\"Firstcsubtopictext\"}]},{\"name\":\"Secondtopic\",\"sub_topics\":[{\"name\":\"SecondFirstsubtopic\",\"text\":\"SecondFirstcsubtopictext\"},{\"name\":\"Secondsecondsubtopic\",\"text\":\"Secondsecondtopictext\"},{\"name\":\"SecondThirdsubtopic\",\"text\":\"SecondThirdtopictext\"}]}],\"URLS\":[\"www.Microsoft.com\",\"www.Google.com\",\"www.AWS.com\"]}"

    anchor_json = {}
    url_json = {}
    content = None
    def generate_mindmap(self,url, user_prompt):
        scrapper_object = ws.web_scrapper()
        head_json,url_json, content  = scrapper_object.scrape_website(url)
        aiog = og.AI_Orchestrator("gpt35")
        self.content_json = aiog.generate_content_JSON(heading_json=head_json,links_json=url_json,content=content)
        # ai_skills = ai.create_content(head_json, user_prompt, web_content)
        # ai_skills.generate_subtopics(head_json, user_prompt)
        return self.content_json

if __name__ == "__main__":
    orchestrator_object =Orchestrator()
    orchestrator_object.generate_mindmap("https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles","test")
    # orchestrator_object.generate_mindmap("https://en.wikipedia.org/wiki/Microsoft","tst")
    # 'http://www.nytimes.com/2009/12/21/us/21storm.html'