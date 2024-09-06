# Owner: Kirthika
# Purpose: This module will talk with Open AI to get Json response back given head_json, user_prompt, web_content

# import nltk
# import requests
# import json
# import re
# import os
# from collections import Counter
# import nltkmodule as nltkmodule
# import cleantext as ct
# import extractkeywords as extractkeywords

# nltkmodule.download_nltk_data()

# class ai_orchestrator:
#     def __init__(self, api_key, endpoint, deployment_name):
#         self.api_key = api_key
#         self.endpoint = endpoint
#         self.deployment_name = deployment_name

#     def generate_subtopics(self, header_json, user_prompt, base_url):
#         mind_map = []

#         for section in header_json:
#             section_text = " ".join(section['text'])  # Concatenate text if it's a list
#             section_text_slug = section_text.replace(' ', '-').lower()  # Generate slug for URL

#             # Constructing the prompt for GPT-4
#             prompt = (
#                 f"{user_prompt}\n\n"
#                 f"Here is a section titled '{section_text}'.\n"
#                 f"Please provide a summary and identify central topics with supporting ideas."
#             )

#             api_url = f"{self.endpoint}/openai/deployments/{self.deployment_name}/chat/completions?api-version=2023-03-15-preview"

#             # Set headers and payload
#             headers = {
#                 "Content-Type": "application/json",
#                 "Authorization": f"Bearer {self.api_key}"  # Use API key in header for authentication
#             }
#             payload = {
#                 "model": "gpt-4",
#                 "messages": [
#                     {"role": "user", "content": prompt}
#                 ],
#                 "max_tokens": 200,
#                 "temperature": 0.7
#             }

#             # Make the request with API key as a header
#             response = requests.post(api_url, headers=headers, params={'api-key': self.api_key}, json=payload)
           

#             # Print status code and response text for debugging
#             # print(f"Status Code: {response.status_code}")
#             # print(f"Response Text: {response.text}")

#             try:
#                 response_json = response.json()
#             except json.JSONDecodeError:
#                 print("Failed to decode JSON response")
#                 return

#             if response.status_code == 200:
#                 summary = response_json['choices'][0]['message']['content'].strip()
#                 summary = ct.clean_text(summary)  # Clean the summary text

#                 # Extracting the central topic and supporting ideas
#                 sentences = summary.split('.')
#                 if len(sentences) > 1:
#                     central_topic = sentences[0]
#                     supporting_ideas = sentences[1:]
#                 else:
#                     central_topic = summary
#                     supporting_ideas = []

#                 central_node = {
#                     'heading': section_text,
#                     'link': f"{base_url}#{section_text_slug}",
#                     'summary': central_topic.strip(),
#                     'children': [extractkeywords.extract_keywords(idea.strip()) for idea in supporting_ideas if idea.strip()]
#                 }

#                 mind_map.append(central_node)
#             else:
#                 print(f"Error: {response_json}")

#         # Return the result as a JSON string
#         return json.dumps(mind_map, indent=4)


# # Sample usage
# if __name__ == "__main__":
#     head_json = [
#         {"h_type": "h1", "text": ["Reliability design principles"]}, 
#         {"h_type": "h2", "text": ["Design for business requirements"]}, 
#         {"h_type": "h2", "text": ["Design for resilience"]}, 
#         {"h_type": "h2", "text": ["Design for recovery"]}, 
#         {"h_type": "h2", "text": ["Design for operations"]}, 
#         {"h_type": "h2", "text": ["Keep it simple"]}
#     ]

#     user_prompt = "I'm interested in learning about reliability design principles. Can you provide a summary of each section?"
#     base_url = "https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles"

#     api_key = ""  # Replace with your actual API key
#     endpoint = ""  # Replace with your endpoint
#     deployment_name = ""  # Your deployment name

#     ai_skill = ai_orchestrator(api_key=api_key, endpoint=endpoint, deployment_name=deployment_name)
#     subtopics = ai_skill.generate_subtopics(head_json, user_prompt, base_url)

#     print(subtopics)  # Print or handle the JSON output

# with new design given by Guru with sub topics are hardcoded


import nltk
import requests
import json
import re
import os
from collections import Counter
import nltkmodule as nltkmodule
import cleantext as ct
import extractkeywords as extractkeywords

nltkmodule.download_nltk_data()

class ai_orchestrator:
    def __init__(self, api_key, endpoint, deployment_name):
        self.api_key = api_key
        self.endpoint = endpoint
        self.deployment_name = deployment_name

    def generate_subtopics(self, header_json, user_prompt, base_url):
        mind_map = {
            "page_summary": "",
            "content": "content",
            "topics": []
        }

        full_page_summary = []

        for section in header_json:
            section_text = " ".join(section['text'])  # Concatenate text if it's a list
            section_text_slug = section_text.replace(' ', '-').lower()  # Generate slug for URL

            # Constructing the prompt for GPT-4
            prompt = (
                f"{user_prompt}\n\n"
                f"Here is a section titled '{section_text}'.\n"
                f"Please provide a summary and identify central topics with supporting ideas."
            )

            api_url = f"{self.endpoint}/openai/deployments/{self.deployment_name}/chat/completions?api-version=2023-03-15-preview"

            # Set headers and payload
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"  # Use API key in header for authentication
            }
            payload = {
                "model": "gpt-4",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 200,
                "temperature": 0.7
            }

            # Make the request with API key as a header
            response = requests.post(api_url, headers=headers, params={'api-key': self.api_key}, json=payload)

            try:
                response_json = response.json()
            except json.JSONDecodeError:
                print("Failed to decode JSON response")
                return

            if response.status_code == 200:
                summary = response_json['choices'][0]['message']['content'].strip()
                summary = ct.clean_text(summary)  # Clean the summary text

                # Extracting the central topic and supporting ideas
                sentences = summary.split('.')
                if len(sentences) > 1:
                    central_topic = sentences[0]
                    supporting_ideas = sentences[1:]
                else:
                    central_topic = summary
                    supporting_ideas = []

                # Collecting keywords dynamically for subtopics
                sub_topics = [
                    {
                        'name': f"Subtopic {index+1}",
                        'text': extractkeywords.extract_keywords(idea.strip())
                    } for index, idea in enumerate(supporting_ideas) if idea.strip()
                ]

                # Construct the central node for the mind map
                central_node = {
                    'name': section_text,
                    'sub_topics': sub_topics
                }

                # Add the central node to the topics
                mind_map["topics"].append(central_node)

                # Add the section summary to the full page summary
                full_page_summary.append(central_topic.strip())

            else:
                print(f"Error: {response_json}")

        # Combine all section summaries to create a full page summary
        mind_map["page_summary"] = " ".join(full_page_summary[:3])  # Use first 2-3 lines

        # Return the result as a JSON string
        return json.dumps(mind_map, indent=4)


# Sample usage
if __name__ == "__main__":
    head_json = [
        {"h_type": "h1", "text": ["Reliability design principles"]}, 
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

    ai_skill = ai_orchestrator(api_key=api_key, endpoint=endpoint, deployment_name=deployment_name)
    subtopics = ai_skill.generate_subtopics(head_json, user_prompt, base_url)

    print(subtopics)  # Print or handle the JSON output
