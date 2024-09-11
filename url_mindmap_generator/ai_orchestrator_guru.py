import json
import ai_cleanup_guru as dc 
import ai_llm_ops_guru as llm

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
    def store_raw_content(self,session_id = "123",file_name="test"):
        file_name = file_name+"_"+session_id+".txt"
        with open(file = file_name,mode = "a") as f:
            f.write(self.content)
            f.write("\nHeadings from Web Parser for Propmts:\n")
            f.write(json.dumps(self.heading_json))

    def generate_content_JSON(self,heading_json,links_json,content) -> json:

        
        # initialize clean content
        self.heading_json = heading_json
        self.links_json = links_json
        self.content = content
        
        # Clean Content
        self.content = self.data_cleanup.cleanup(content = self.content)

        # Store Cleaned / Raw Content (more content needs to be removed)
        self.store_raw_content()

        ##Generate Page Summary
        page_summary = self.generate_page_summary()
        topic_summary = self.generate_topics_with_summary()
        self.content_JSON=self.parse_response(topic_summary)
        self.content_JSON["page_summary"] = page_summary

        self.content_JSON = json.dumps(self.content_JSON, indent=4)
        print(self.content_JSON)

        return self.content_JSON    

    def generate_page_summary(self):
        page_summary = self.llm.generate_summary(self.content)
        return page_summary


    def generate_topics_with_summary(self):
        topic_summary = self.llm.generate_topics(self.content,self.heading_json)
        return topic_summary

    # def parse_response(self, topic_response):
    #     """
    #     This method parses the topic_response and converts it into the desired JSON structure.
        
    #     :param topic_response: Parsed JSON response (Python dict) from the LLM.
    #     :return: A JSON structure in the format you need.
    #     """
    #     result = {
    #         "page_summary": "",  
    #         "name": "",          # Leaving it blank for now
    #         "text": "",          # Leaving it blank for now
    #         "sub_topics": []
    #     }

    #     # Iterate through the topic_response and build the structure
    #     for topic, details in topic_response.items():
    #         sub_topic = {
    #             "name": topic,
    #             "text": details.get("description", ""),  
    #             "sub_topics": []
    #         }

    #         for sub, sub_desc in details.get("subtopics", {}).items():
    #             sub_topic["sub_topics"].append({
    #                 "name": sub,
    #                 "text": sub_desc  # Assigning the subtopic description from the LLM response
    #             })

    #         result["sub_topics"].append(sub_topic)

    #     return result
    

    def parse_response(self, topic_response):
        """
        This method parses the topic_response and converts it into the desired JSON structure.
        
        :param topic_response: Parsed JSON response (Python dict) from the LLM.
        :return: A JSON structure in the format you need.
        """
        result = {
            "page_summary": "",  
            "name": "",          # Leaving it blank for now
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
            
            # Check if subtopics is a dictionary or list and handle appropriately
            if isinstance(subtopics, dict):
                # Iterate through subtopics if it's a dictionary
                for sub_name, sub_text in subtopics.items():
                    sub_topic["sub_topics"].append({
                        "name": sub_name,
                        "text": sub_text  # Assigning the subtopic description
                    })
            elif isinstance(subtopics, list):
                # If subtopics is a list, iterate over the list
                for subtopic in subtopics:
                    sub_topic["sub_topics"].append({
                        "name": subtopic.get("name", ""),
                        "text": subtopic.get("text", "")
                    })
            
            result["sub_topics"].append(sub_topic)

        return result
