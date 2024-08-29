# Owner: Kirthika and Anil
# Purpose: Generate JSON that captures 
# 1. Subtopics and summarization 
# 2. Leveraging User, module and system prompts.
# 3. Need to make this module more modular.

# class AISkill():
#     def generate_subtopics(self,header_json,user_prompt):
#         pass


import requests
import json

class AzureAISkill:
    def __init__(self, api_key, endpoint, deployment_name):
        self.api_key = api_key
        self.endpoint = endpoint
        self.deployment_name = deployment_name

    def generate_subtopics(self, header_json, user_prompt, base_url):
        subtopics = []
        
        for section in header_json:
            header_type = section['h_type']
            section_text = " ".join(section['text']) 
            section_text_slug = section_text.replace(' ', '-').lower()  

            # Constructing the prompt for GPT-4
            prompt = (
                f"{user_prompt}\n\n"
                f"Here is a section titled '{section_text}', categorized under '{header_type}'.\n"
                f"Please summarize the content expected under this section in 2 lines maximum, providing a brief and clear description."
            )

            api_url = f"{self.endpoint}/openai/deployments/{self.deployment_name}/chat/completions?api-version=2023-03-15-preview"

           
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"  
            }
            payload = {
                "model": "gpt-4",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 150,
                "temperature": 0.7
            }

            response = requests.post(api_url, headers=headers, params={'api-key': self.api_key}, json=payload)
            response_json = response.json()

            if response.status_code == 200:
                summary = response_json['choices'][0]['message']['content'].strip()
                # Ensure summary is 2 lines max
                summary_lines = summary.split('\n')
                if len(summary_lines) > 2:
                    summary = '\n'.join(summary_lines[:2])

                subtopics.append({
                    'heading': section_text,
                    'link': f"{base_url}#{section_text_slug}", 
                    'summary': summary
                })
            else:
                print(f"Error: {response_json}")

        # Return the result as a JSON string
        return json.dumps(subtopics, indent=4)

# Sample usage
if __name__ == "__main__":
    header_json = [
        {"h_type": "h1", "text": ["Reliability design principles"]}, 
        {"h_type": "h2", "text": ["In this article"]}, 
        {"h_type": "h2", "text": ["Design for business requirements"]}, 
        {"h_type": "h2", "text": ["Design for resilience"]}, 
        {"h_type": "h2", "text": ["Design for recovery"]}, 
        {"h_type": "h2", "text": ["Design for operations"]}, 
        {"h_type": "h2", "text": ["Keep it simple"]} 
    ]

    user_prompt = "I'm interested in learning about reliability design principles. Can you provide a summary of each section?"
    base_url = "https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles"

    api_key = ""  # Replace with your actual API key
    endpoint = ""  # Replace with your endpoint
    deployment_name = ""  # Your deployment name

    ai_skill = AzureAISkill(api_key=api_key, endpoint=endpoint, deployment_name=deployment_name)
    subtopics = ai_skill.generate_subtopics(header_json, user_prompt, base_url)

    print(subtopics)  