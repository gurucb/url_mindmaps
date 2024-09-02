# Owner: Kirthika and Anil
# Purpose: Generate JSON that captures 
# 1. Subtopics and summarization 
# 2. Leveraging User, module and system prompts.
# 3. Need to make this module more modular.

# class AISkill():
#     def generate_subtopics(self,header_json,user_prompt):
#         pass


# import requests
# import json

# class AzureAISkill:
#     def __init__(self, api_key, endpoint, deployment_name):
#         self.api_key = api_key
#         self.endpoint = endpoint
#         self.deployment_name = deployment_name

#     def generate_subtopics(self, header_json, user_prompt, base_url):
#         subtopics = []
        
#         for section in header_json:
#             header_type = section['h_type']
#             section_text = " ".join(section['text'])  # Concatenate text if it's a list
#             section_text_slug = section_text.replace(' ', '-').lower()  # Generate slug for URL

#             # Constructing the prompt for GPT-4
#             prompt = (
#                 f"{user_prompt}\n\n"
#                 f"Here is a section titled '{section_text}', categorized under '{header_type}'.\n"
#                 f"Please summarize the content expected under this section in 2 lines maximum, providing a brief and clear description."
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
#                 "max_tokens": 150,
#                 "temperature": 0.7
#             }

#             # Make the request with API key as a header
#             response = requests.post(api_url, headers=headers, params={'api-key': self.api_key}, json=payload)
#             response_json = response.json()

#             if response.status_code == 200:
#                 summary = response_json['choices'][0]['message']['content'].strip()
#                 # Ensure summary is 2 lines max
#                 summary_lines = summary.split('\n')
#                 if len(summary_lines) > 2:
#                     summary = '\n'.join(summary_lines[:2])

#                 subtopics.append({
#                     'heading': section_text,
#                     'link': f"{base_url}#{section_text_slug}",  # Generate link with slug
#                     'summary': summary
#                 })
#             else:
#                 print(f"Error: {response_json}")

#         # Return the result as a JSON string
#         return json.dumps(subtopics, indent=4)

# # Sample usage
# if __name__ == "__main__":
#     header_json = [
#         {"h_type": "h1", "text": ["Reliability design principles"]}, 
#         {"h_type": "h2", "text": ["In this article"]}, 
#         {"h_type": "h2", "text": ["Design for business requirements"]}, 
#         {"h_type": "h2", "text": ["Design for resilience"]}, 
#         {"h_type": "h2", "text": ["Design for recovery"]}, 
#         {"h_type": "h2", "text": ["Design for operations"]}, 
#         {"h_type": "h2", "text": ["Keep it simple"]} 
#     ]

#     user_prompt = "I'm interested in learning about reliability design principles. Can you provide a summary of each section?"
#     base_url = "https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles"

#     api_key = "6f28b6515c5440938b6c3a7d9a5dadc6"  # Replace with your actual API key
#     endpoint = "https://langchainopenaiguru.openai.azure.com"  # Replace with your endpoint
#     deployment_name = "gpt-4o-mini"  # Your deployment name

#     ai_skill = AzureAISkill(api_key=api_key, endpoint=endpoint, deployment_name=deployment_name)
#     subtopics = ai_skill.generate_subtopics(header_json, user_prompt, base_url)

#     print(subtopics)  # Print or handle the JSON output

# import requests
# import json

# class AzureAISkill:
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
#             response_json = response.json()

#             if response.status_code == 200:
#                 summary = response_json['choices'][0]['message']['content'].strip()

#                 # Extracting the central topic and supporting ideas
#                 central_topic = summary.split('.')[0]  # Assuming the first sentence is the central topic
#                 supporting_ideas = summary.split('.')[1:]  # The rest are supporting ideas

#                 central_node = {
#                     'heading': section_text,
#                     'link': f"{base_url}#{section_text_slug}",
#                     'summary': central_topic.strip(),
#                     'children': []
#                 }

#                 for idea in supporting_ideas:
#                     idea_text = idea.strip()
#                     if idea_text:
#                         # Create a child node for each supporting idea
#                         central_node['children'].append({
#                             'heading': idea_text
#                         })

#                 mind_map.append(central_node)
#             else:
#                 print(f"Error: {response_json}")

#         # Return the result as a JSON string
#         return json.dumps(mind_map, indent=4)

# # Sample usage
# if __name__ == "__main__":
#     header_json = [
#         {"h_type": "h1", "text": ["Reliability design principles"]}, 
#         {"h_type": "h2", "text": ["Design for business requirements"]}, 
#         {"h_type": "h2", "text": ["Design for resilience"]}, 
#         {"h_type": "h2", "text": ["Design for recovery"]}, 
#         {"h_type": "h2", "text": ["Design for operations"]}, 
#         {"h_type": "h2", "text": ["Keep it simple"]}
#     ]

#     user_prompt = "I'm interested in learning about reliability design principles. Can you provide a summary of each section?"
#     base_url = "https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles"

#     api_key = "6f28b6515c5440938b6c3a7d9a5dadc6"  # Replace with your actual API key
#     endpoint = "https://langchainopenaiguru.openai.azure.com"  # Replace with your endpoint
#     deployment_name = "gpt-4o-mini"  # Your deployment name

#     ai_skill = AzureAISkill(api_key=api_key, endpoint=endpoint, deployment_name=deployment_name)
#     subtopics = ai_skill.generate_subtopics(header_json, user_prompt, base_url)

#     print(subtopics)  # Print or handle the JSON output


# sub topics with children and headings


# import requests
# import json
# import re

# class AzureAISkill:
#     def __init__(self, api_key, endpoint, deployment_name):
#         self.api_key = api_key
#         self.endpoint = endpoint
#         self.deployment_name = deployment_name

#     def clean_text(self, text):
#         """Clean text by removing unwanted characters."""
#         # Remove special characters like **, \n, ##, etc.
#         text = re.sub(r'\*\*', '', text)  # Remove bold markers
#         text = re.sub(r'\n+', ' ', text)  # Replace new lines with space
#         text = re.sub(r'#{1,6}', '', text)  # Remove Markdown headers
#         text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
#         return text.strip()

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
#             response_json = response.json()

#             if response.status_code == 200:
#                 summary = response_json['choices'][0]['message']['content'].strip()
#                 summary = self.clean_text(summary)  # Clean the summary text

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
#                     'children': []
#                 }

#                 for idea in supporting_ideas:
#                     idea_text = idea.strip()
#                     if idea_text:
#                         # Create a child node for each supporting idea
#                         central_node['children'].append({
#                             'heading': idea_text
#                         })

#                 mind_map.append(central_node)
#             else:
#                 print(f"Error: {response_json}")

#         # Return the result as a JSON string
#         return json.dumps(mind_map, indent=4)

# # Sample usage
# if __name__ == "__main__":
#     header_json = [
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

#     ai_skill = AzureAISkill(api_key=api_key, endpoint=endpoint, deployment_name=deployment_name)
#     subtopics = ai_skill.generate_subtopics(header_json, user_prompt, base_url)

#     print(subtopics)  # Print or handle the JSON output

#subtopics with children without headings but children is a list of strings

# import requests
# import json
# import re

# class AzureAISkill:
#     def __init__(self, api_key, endpoint, deployment_name):
#         self.api_key = api_key
#         self.endpoint = endpoint
#         self.deployment_name = deployment_name

#     def clean_text(self, text):
#         """Clean text by removing unwanted characters."""
#         text = re.sub(r'\*\*', '', text)  # Remove bold markers
#         text = re.sub(r'\n+', ' ', text)  # Replace new lines with space
#         text = re.sub(r'#{1,6}', '', text)  # Remove Markdown headers
#         text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
#         return text.strip()

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
#             response_json = response.json()

#             if response.status_code == 200:
#                 summary = response_json['choices'][0]['message']['content'].strip()
#                 summary = self.clean_text(summary)  # Clean the summary text

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
#                     'children': [idea.strip() for idea in supporting_ideas if idea.strip()]
#                 }

#                 mind_map.append(central_node)
#             else:
#                 print(f"Error: {response_json}")

#         # Return the result as a JSON string
#         return json.dumps(mind_map, indent=4)

# # Sample usage
# if __name__ == "__main__":
#     header_json = [
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

#     ai_skill = AzureAISkill(api_key=api_key, endpoint=endpoint, deployment_name=deployment_name)
#     subtopics = ai_skill.generate_subtopics(header_json, user_prompt, base_url)

#     print(subtopics)  # Print or handle the JSON output


# subtopics with children without headings but children is precise summary

import nltk
import requests
import json
import re
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Ensure NLTK data is downloaded to the specified directory
def download_nltk_data():
    try:
        nltk.data.path.append(os.path.expanduser('~/nltk_data'))
        nltk.download('punkt', download_dir=nltk.data.path[0])
        nltk.download('stopwords', download_dir=nltk.data.path[0])
        print("NLTK data downloaded successfully.")
    except Exception as e:
        print(f"Error downloading NLTK data: {e}")

# Download necessary NLTK data
download_nltk_data()

class AzureAISkill:
    def __init__(self, api_key, endpoint, deployment_name):
        self.api_key = api_key
        self.endpoint = endpoint
        self.deployment_name = deployment_name

    def clean_text(self, text):
        """Clean text by removing unwanted characters."""
        text = re.sub(r'\*\*', '', text)  # Remove bold markers
        text = re.sub(r'\n+', ' ', text)  # Replace new lines with space
        text = re.sub(r'#{1,6}', '', text)  # Remove Markdown headers
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
        return text.strip()

    def extract_keywords(self, text, num_keywords=2):
        """Extract key phrases or words from the text."""
        # Tokenize text and remove stopwords
        words = word_tokenize(text.lower())
        words = [word for word in words if word.isalnum()]
        filtered_words = [word for word in words if word not in stopwords.words('english')]
        
        # Find the most common words/phrases
        word_counts = Counter(filtered_words)
        common_words = [word for word, _ in word_counts.most_common(num_keywords)]
        
        return ' '.join(common_words).title()

    def generate_subtopics(self, header_json, user_prompt, base_url):
        mind_map = []

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
            response_json = response.json()

            if response.status_code == 200:
                summary = response_json['choices'][0]['message']['content'].strip()
                summary = self.clean_text(summary)  # Clean the summary text

                # Extracting the central topic and supporting ideas
                sentences = summary.split('.')
                if len(sentences) > 1:
                    central_topic = sentences[0]
                    supporting_ideas = sentences[1:]
                else:
                    central_topic = summary
                    supporting_ideas = []

                central_node = {
                    'heading': section_text,
                    'link': f"{base_url}#{section_text_slug}",
                    'summary': central_topic.strip(),
                    'children': [self.extract_keywords(idea.strip()) for idea in supporting_ideas if idea.strip()]
                }

                mind_map.append(central_node)
            else:
                print(f"Error: {response_json}")

        # Return the result as a JSON string
        return json.dumps(mind_map, indent=4)

# Sample usage
if __name__ == "__main__":
    header_json = [
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

    ai_skill = AzureAISkill(api_key=api_key, endpoint=endpoint, deployment_name=deployment_name)
    subtopics = ai_skill.generate_subtopics(header_json, user_prompt, base_url)

    print(subtopics)  # Print or handle the JSON output
