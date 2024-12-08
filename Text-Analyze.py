import re
from collections import Counter
from textstat import flesch_reading_ease
def analyze_text(text):
    # Count words and sentences
    words = re.findall(r'\b\w+\b', text)
    sentences = re.split(r'[.!?]', text)
    num_words = len(words)
    num_sentences = len([s for s in sentences if s.strip()])
    
    # Find most common words
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(5)  # Top 5 most common words
    
    # Find the most frequent word
    most_frequent_word, most_frequent_count = word_counts.most_common(1)[0]
    
    # Find the shortest and longest words
    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)
    
    # Calculate readability score
    readability_score = flesch_reading_ease(text)
