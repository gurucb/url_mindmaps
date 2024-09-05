import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

def extract_keywords(text, num_keywords=2):
        """Extract key phrases or words from the text."""
        # Tokenize text and remove stopwords
        words = word_tokenize(text.lower())
        words = [word for word in words if word.isalnum()]
        filtered_words = [word for word in words if word not in stopwords.words('english')]
        
        # Find the most common words/phrases
        word_counts = Counter(filtered_words)
        common_words = [word for word, _ in word_counts.most_common(num_keywords)]
        return ' '.join(common_words).title()


