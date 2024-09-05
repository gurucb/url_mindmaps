import nltk
import os

# Ensure NLTK data is downloaded to the specified directory
def download_nltk_data():
    try:
        nltk.data.path.append(os.path.expanduser('~/nltk_data'))
        nltk.download('punkt', download_dir=nltk.data.path[0])
        nltk.download('stopwords', download_dir=nltk.data.path[0])
        print("NLTK data downloaded successfully.")
    except Exception as e:
        print(f"Error downloading NLTK data: {e}")

