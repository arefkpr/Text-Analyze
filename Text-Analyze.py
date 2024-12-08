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

  return {
        "word_count": num_words,
        "sentence_count": num_sentences,
        "most_common_words": most_common_words,
        "most_frequent_word": most_frequent_word,
        "most_frequent_count": most_frequent_count,
        "shortest_word": shortest_word,
        "longest_word": longest_word,
        "readability_score": readability_score
    }

def save_report(results, filename="text_analysis_report.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Text Analysis Report\n")
        file.write("====================\n")
        file.write(f"Total Words: {results['word_count']}\n")
        file.write(f"Total Sentences: {results['sentence_count']}\n")
        file.write("Most Common Words:\n")
        for word, count in results["most_common_words"]:
            file.write(f"  - {word}: {count} times\n")
        file.write(f"Most Frequent Word: {results['most_frequent_word']} ({results['most_frequent_count']} times)\n")
        file.write(f"Shortest Word: {results['shortest_word']}\n")
        file.write(f"Longest Word: {results['longest_word']}\n")
        file.write(f"Readability Score: {results['readability_score']:.2f}\n")
    print(f"Report saved to {filename}")
