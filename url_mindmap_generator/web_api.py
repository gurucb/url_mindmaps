
# Owner: Kumud 
# Purpose:
# 1. Build Jazzy web page that connects to Web API
# 2. Web API takes dependency on Orchestrator

from orchestrator_map import Orchestrator

class web_api():
    def generate_mindmap_api(self, url, user_prompt):
        self.url = url
        self.user_prompt = user_prompt
        self.create_mindmap_result()

    def create_mindmap_result(self):
        orch = Orchestrator()
        content_json, anchor_json = orch.generate_mindmap(
                                user_prompt=self.url,
                                user_prompt = self.user_prompt
                            )
        # Post Processing if required using both JSON
        # Create a response object JSON
        response = self.create_response()
        return response
    
    def post_processing(self):
        pass

    def create_response(self):
        pass