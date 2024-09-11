# Owner: Kumud 
# Purpose:
# 1. Build Jazzy web page that connects to Web API
# 2. Web API takes dependency on Orchestrator

from orchestrator import Orchestrator
import flask
from flask_cors import CORS

class web_api():
    def __init__(self):
        self.app = flask.Flask(__name__)
        CORS(self.app) 
        self.setup_routes()
        self.app.run(port=5001)

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
        orch = Orchestrator()
        content_json= orch.generate_mindmap(
                                url=self.url,
                                user_prompt=self.user_prompt
                            )
        # Post Processing if required using both JSON
        # Create a response object JSON
        response = self.create_response(content_json)
        return response
    
    def post_processing(self):
        pass

    def create_response(self, content_json):
        return content_json

api_instance = web_api()
