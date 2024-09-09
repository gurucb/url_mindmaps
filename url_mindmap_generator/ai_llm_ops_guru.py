import json
from openai import AzureOpenAI
  
class LLMOps:
    llm_engine = None
    client = None
    llm_config = {}
    def __init__(self,llm_engine) -> None:
        self.llm_engine = llm_engine
    
    def __init_llm_engine(self,llm_engine):
        
        file_path = "url_mindmap_generator\\ai_llm_engines_config.json"
        with open(file_path,"r") as f:
            temp = f.read()
            self.llm_config = json.loads(temp)
        self.llm_config = self.llm_config[llm_engine]
        self.client = AzureOpenAI(
            azure_endpoint = self.llm_config["endpoint_url"],
            api_key = self.llm_config["key"],
            api_version = self.llm_config["version"]
        )

    def __parse_prompts(self,task):
        file_path = "url_mindmap_generator\\ai_prompts_guru.json"
        with open(file_path,"r") as f:
            temp = f.read()
            self.prompts = json.loads(temp)
        prompt = self.prompts[task]
        system = str(prompt["system"])
        user = str(prompt["user"])
        instructions = list(prompt["instructions"])
        ins_set = ""
        for ins in instructions:
            ins_set = ins_set + str(ins)

        prompt_text = system + user + str(ins_set)
        return prompt_text
    def generate_llm_summary(self,data="",user_prompt="",example=""):
        self.__init_llm_engine(self.llm_engine)
        prompts = self.__parse_prompts("summarization")
        completion = self.client.chat.completions.create(
            model=self.llm_config["deployment_name"],
            messages=[]
            )
        response = completion.to_json()


    def __create_system_prompts():
        pass

    def __generate_response(self,llm_engine,data,user_prompt,example=""):
        pass