
# Owner: Kumud 
# Purpose:
# 1. Build Jazzy web page that connects to Web API
# 2. Web API takes dependency on Orchestrator

from orchestrator_map import Orchestrator
import flask

class web_api():
    def __init__(self):
        self.app = flask.Flask(__name__)
        self.setup_routes()
        self.app.run()

    def setup_routes(self):
        @self.app.route('/get_mindmap_data', methods=['POST'])
        def get_mindmap_data_api():
            data = flask.request.json
            url = data.get('url')
            user_prompt = data.get('user_prompt')
            
            if not url or not user_prompt:
                return flask.jsonify({"error": "Missing url or user_prompt"}), 400
            
            return flask.jsonify(self.generate_mindmap_api(url, user_prompt))

    def generate_mindmap_api(self, url, user_prompt):
        self.url = url
        self.user_prompt = user_prompt
        return self.create_mindmap_result()

    def create_mindmap_result(self):
        # orch = Orchestrator()
        # content_json, anchor_json = orch.generate_mindmap(
        #                         user_prompt=self.url,
        #                         user_prompt = self.user_prompt
        #                     )
        # Post Processing if required using both JSON
        # Create a response object JSON
        response = self.create_response()
        return response
    
    def post_processing(self):
        pass

    def create_response(self):
        return {"response": "Success"}



api_instance = web_api()
