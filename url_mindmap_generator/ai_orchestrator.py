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


# import nltk
# import requests
# import json
# import re
# import os
# from collections import Counter
# import nltkmodule as nltkmodule
# import cleantext as ct
# import extractkeywords as extractkeywords
# import generatedynamicuserpromptmodule as userprompt

# nltkmodule.download_nltk_data()

# class ai_orchestrator:
#     def __init__(self, api_key, endpoint, deployment_name):
#         self.api_key = api_key
#         self.endpoint = endpoint
#         self.deployment_name = deployment_name

#     def generate_subtopics(self, header_json, base_url):
#         mind_map = {
#             "page_summary": "",
#             "content": "content",
#             "topics": []
#         }

#         user_prompt = userprompt.generate_dynamic_user_prompt(base_url)
#         full_page_summary = []

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

#                 # Collecting keywords dynamically for subtopics
#                 sub_topics = [
#                     {
#                         'name': f"Subtopic {index+1}",
#                         'text': extractkeywords.extract_keywords(idea.strip())
#                     } for index, idea in enumerate(supporting_ideas) if idea.strip()
#                 ]

#                 # Construct the central node for the mind map
#                 central_node = {
#                     'name': section_text,
#                     'sub_topics': sub_topics
#                 }

#                 # Add the central node to the topics
#                 mind_map["topics"].append(central_node)

#                 # Add the section summary to the full page summary
#                 full_page_summary.append(central_topic.strip())

#             else:
#                 print(f"Error: {response_json}")

#         # Combine all section summaries to create a full page summary
#         mind_map["page_summary"] = " ".join(full_page_summary[:3])  # Use first 2-3 lines

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

#    # user_prompt = "I'm interested in learning about reliability design principles. Can you provide a summary of each section?"
#     base_url = "https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles"

#     api_key = ""  # Replace with your actual API key
#     endpoint = ""  # Replace with your endpoint
#     deployment_name = ""  # Your deployment name

#     ai_skill = ai_orchestrator(api_key=api_key, endpoint=endpoint, deployment_name=deployment_name)
#     subtopics = ai_skill.generate_subtopics(head_json,base_url)

#     print(subtopics)  # Print or handle the JSON output


# import requests
# import json
# import cleantext as ct
# import extractkeywords as extractkeywords
# import generatedynamicuserpromptmodule as userprompt

# class ai_orchestrator:
#     def __init__(self, api_key, endpoint, deployment_name):
#         self.api_key = api_key
#         self.endpoint = endpoint
#         self.deployment_name = deployment_name

#     def generate_subtopics(self, header_json, base_url):
#         mind_map = {
#             "page_summary": "",
#             "content": "content",
#             "topics": []
#         }

#         user_prompt = userprompt.generate_dynamic_user_prompt(base_url)
#         full_page_summary = []

#         for section in header_json:
#             section_text = " ".join(section['text'])  # Concatenate text if it's a list
#             section_text_slug = section_text.replace(' ', '-').lower()  # Generate slug for URL
#             section_url = f"{base_url}#{section_text_slug}"  # Create URL for the section

#             # Refined prompt for better, shorter summaries (2-line summary)
#             prompt = (
#                 f"{user_prompt}\n\n"
#                 f"Section Title: '{section_text}'.\n\n"
#                 f"Please provide a concise summary of this section in **no more than 2 lines**. "
#                 f"Keep it brief but informative, focusing on the main point and key takeaway."
#             )

#             api_url = f"{self.endpoint}/openai/deployments/{self.deployment_name}/chat/completions?api-version=2023-03-15-preview"

#             # Set headers and payload
#             headers = {
#                 "Content-Type": "application/json",
#                 "Authorization": f"Bearer {self.api_key}"
#             }
#             payload = {
#                 "model": "gpt-4",
#                 "messages": [
#                     {"role": "user", "content": prompt}
#                 ],
#                 "max_tokens": 150,  # Reduced max tokens to enforce conciseness
#                 "temperature": 0.7
#             }

#             # Make the request with API key as a header
#             response = requests.post(api_url, headers=headers, params={'api-key': self.api_key}, json=payload)

#             try:
#                 response_json = response.json()
#             except json.JSONDecodeError:
#                 print("Failed to decode JSON response")
#                 return

#             if response.status_code == 200:
#                 summary = response_json['choices'][0]['message']['content'].strip()
#                 summary = ct.clean_text(summary)  # Clean the summary text

#                 # Limit the summary to 2 lines
#                 summary_sentences = summary.split('. ')  # Split into sentences
#                 trimmed_summary = '. '.join(summary_sentences[:2]) + '.'  # Take the first 2 sentences

#                 # Collecting keywords dynamically for subtopics
#                 sub_topics = [
#                     {
#                         'name': f"Subtopic {index+1}",
#                         'text': extractkeywords.extract_keywords(idea.strip())
#                     } for index, idea in enumerate(summary_sentences) if idea.strip()
#                 ]

#                 # Construct the central node for the mind map with concise summary and URL
#                 central_node = {
#                     'name': section_text,
#                     'text': trimmed_summary,  # Use the concise 2-line summary
#                     'url': section_url,
#                     'sub_topics': sub_topics
#                 }

#                 # Add the central node to the topics
#                 mind_map["topics"].append(central_node)

#                 # Add the section summary to the full page summary
#                 full_page_summary.append(trimmed_summary)

#             else:
#                 print(f"Error: {response_json}")

#         # Combine all section summaries to create a full page summary
#         mind_map["page_summary"] = " ".join(full_page_summary[:3])  # Use first 2-3 summaries

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

#     base_url = "https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles"

#     api_key = "3e328fb1d0a3439990774cb1543bae17"  # Replace with your actual API key
#     endpoint = "https://kirthikarajaganeshcognitive.openai.azure.com"  # Replace with your endpoint
#     deployment_name = "gpt-4o-mini"  # Your deployment name

#     ai_skill = ai_orchestrator(api_key=api_key, endpoint=endpoint, deployment_name=deployment_name)
#     subtopics = ai_skill.generate_subtopics(head_json, base_url)

#     print(subtopics)  # Print or handle the JSON output

import requests
import json
import cleantext as ct
import extractkeywords as extractkeywords
import generatedynamicuserpromptmodule as userprompt

class ai_orchestrator:
    def __init__(self, api_key, endpoint, deployment_name):
        self.api_key = api_key
        self.endpoint = endpoint
        self.deployment_name = deployment_name

    def generate_subtopics(self, header_json, base_url):
        mind_map = {
            "page_summary": "",
            "content": "content",
            "topics": []
        }

        user_prompt = userprompt.generate_dynamic_user_prompt(base_url)
        full_page_summary = []

        for section in header_json:
            section_text = " ".join(section['text'])  # Concatenate text if it's a list
            section_text_slug = section_text.replace(' ', '-').lower()  # Generate slug for URL
            section_url = f"{base_url}#{section_text_slug}"  # Create URL for the section

            # Refined prompt for better, shorter summaries (2-line summary)
            prompt = (
                f"{user_prompt}\n\n"
                f"Section Title: '{section_text}'.\n\n"
                f"Please provide a concise summary of this section in **no more than 2 lines**. "
                f"Keep it brief but informative, focusing on the main point and key takeaway."
            )

            api_url = f"{self.endpoint}/openai/deployments/{self.deployment_name}/chat/completions?api-version=2023-03-15-preview"

            # Set headers and payload
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            payload = {
                "model": "gpt-4",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 150,  # Reduced max tokens to enforce conciseness
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

                # Limit the summary to 2 lines
                summary_sentences = summary.split('. ')  # Split into sentences
                trimmed_summary = '. '.join(summary_sentences[:2]) + '.'  # Take the first 2 sentences

                # Construct 3 subtopics based on the parent section's key points (same summarization logic)
                sub_topics = []
                for i in range(3):
                    sub_topic_name = f"Supporting Idea {i+1}"  # Uniform names for subtopics
                    sub_topic_text = trimmed_summary  # Use the parent summary logic for subtopics
                    sub_topics.append({
                        'name': sub_topic_name,
                        'text': sub_topic_text
                    })

                # Construct the central node for the mind map with concise summary and URL
                central_node = {
                    'name': section_text,
                    'text': trimmed_summary,  # Use the concise 2-line summary
                    'url': section_url,
                    'sub_topics': sub_topics  # Attach exactly 3 subtopics
                }

                # Add the central node to the topics
                mind_map["topics"].append(central_node)

                # Add the section summary to the full page summary
                full_page_summary.append(trimmed_summary)

            else:
                print(f"Error: {response_json}")

        # Combine all section summaries to create a full page summary
        mind_map["page_summary"] = " ".join(full_page_summary[:3])  # Use first 2-3 summaries

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

    base_url = "https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles"

    api_key = "3e328fb1d0a3439990774cb1543bae17"  # Replace with your actual API key
    endpoint = "https://kirthikarajaganeshcognitive.openai.azure.com"  # Replace with your endpoint
    deployment_name = "gpt-4o-mini"  # Your deployment name

    ai_skill = ai_orchestrator(api_key=api_key, endpoint=endpoint, deployment_name=deployment_name)
    subtopics = ai_skill.generate_subtopics(head_json, base_url)

    print(subtopics)  # Print or handle the JSON output
