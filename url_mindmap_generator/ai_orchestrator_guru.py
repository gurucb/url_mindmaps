import json
import ai_cleanup_guru as dc 
import ai_llm_ops_guru as llm

class AI_Orchestrator:
    heading_json = None
    links_json = None
    content = None
    data_cleanup = None
    llm = None

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
        content_JSON = {}
        content_JSON["name"] = "CONTENT"
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
        content_JSON["summary"] = page_summary

        return content_JSON    

    def generate_page_summary(self):
        page_summary = self.llm.generate_llm_summary(self.content)
        return page_summary


    def generate_topics_with_summary(self):
        page_summary = self.llm

    def generate_subtopics_with_summary(self):
        pass
    
    def generate_response_json(self):
        pass

