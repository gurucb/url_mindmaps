import json
import ai_cleanup as dc 
import ai_llm_ops as llm
import uuid

class AI_Orchestrator:
    heading_json = None
    links_json = None
    content = None
    data_cleanup = None
    llm = None

    content_JSON = {}
    def __init__(self,llm_engine) -> None:
        self.data_cleanup = dc.DataCleanup()
        self.llm = llm.LLMOps(llm_engine=llm_engine)

        
    ##FileName: Take Session ID and Create the filename with SessionId and URL_Finale.
    ##This will enable to create AI Search and also build graph based systems.
    def store_raw_content(self,session_id=None,file_name=None):
        if session_id == None:
                session_id = uuid.uuid4()
        if file_name == None:
            file_name = "raw_web_contet"
        file_name = file_name+"_"+str(session_id)+".txt"
        with open(file = file_name,mode = "a") as f:
            f.write(self.content)
            f.write("\nHeadings from Web Parser for Propmts:\n")
            f.write(json.dumps(self.heading_json))

    def generate_content_JSON(self,heading_json,links_json,content,user_prompt) -> json:

        # initialize clean content
        self.heading_json = heading_json
        self.links_json = links_json
        self.content = content
        self.user_prompt = user_prompt
        
        # Clean Content
        self.content = self.data_cleanup.cleanup(content = self.content)

        # Store Cleaned / Raw Content (more content needs to be removed)
        self.store_raw_content()

        ##Generate Page Summary
        page_summary = self.generate_page_summary()

        # 0 shot call to LLM
        self.content_JSON = self.generate_topics_with_summary()
        self.content_JSON = self.parse_response(self.content_JSON)
        self.content_JSON["page_summary"] = page_summary
        
        self.content_JSON = json.dumps(self.content_JSON, indent=4)        
        # # 1 shot call to LLM
        self.content_JSON2=self.llm.generate_topics_2(self.content,self.content_JSON,self.user_prompt)
        self.content_JSON2=json.dumps(self.content_JSON2, indent=4)
        # print(self.content_JSON2)
        return self.content_JSON2

    def generate_page_summary(self):
        page_summary = self.llm.generate_summary(self.content,self.user_prompt)
        return page_summary


    def generate_topics_with_summary(self):
        topic_summary = self.llm.generate_topics(self.content,self.heading_json,"English")
        return topic_summary
    def parse_response(self, topic_response):
        """
        This method parses the topic_response and converts it into the desired JSON structure.
        
        :param topic_response: Parsed JSON response (Python dict) from the LLM.
        :return: A JSON structure in the format you need.
        """
        result = {
            "page_summary": "",  
            "name": "Page Summary",          # Leaving it blank for now
            "text": "",          # Leaving it blank for now
            "sub_topics": []
        }

    # Iterate through the topic_response and build the structure
        for topic, details in topic_response.items():
            sub_topic = {
                "name": topic,
                "text": details.get("description", ""),  # Assign the topic description here
                "sub_topics": []
            }

            subtopics = details.get("subtopics", {})
            # Check if subtopics is a dictionary
            if isinstance(subtopics, dict):
                for sub_name, sub_text in subtopics.items():
                    sub_topic["sub_topics"].append({
                        "name": sub_name,
                        "text": sub_text  # Assigning the subtopic description
                    })
            # Check if subtopics is a list
            elif isinstance(subtopics, list):
                for subtopic in subtopics:
                    # Handle case where subtopic is a dictionary
                    if isinstance(subtopic, dict):
                        sub_topic["sub_topics"].append({
                            "name": subtopic.get("name", ""),
                            "text": subtopic.get("text", "")
                        })
                    # Handle case where subtopic is a string
                    elif isinstance(subtopic, str):
                        sub_topic["sub_topics"].append({
                            "name": subtopic,
                            "text": ""  # No additional text for string subtopics
                        })
            # Handle case where subtopics is a string (edge case)
            elif isinstance(subtopics, str):
                sub_topic["sub_topics"].append({
                    "name": subtopics,
                    "text": ""
                })

            result["sub_topics"].append(sub_topic)

        return result


        