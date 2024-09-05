import re

def clean_text(text):
        """Clean text by removing unwanted characters."""
        text = re.sub(r'\*\*', '', text)  # Remove bold markers
        text = re.sub(r'\n+', ' ', text)  # Replace new lines with space
        text = re.sub(r'#{1,6}', '', text)  # Remove Markdown headers
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
        return text.strip()