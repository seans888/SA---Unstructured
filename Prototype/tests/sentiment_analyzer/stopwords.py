from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "This sentence demonstrates how filtering of stop words work."
stop_words = set(stopwords.words("english"))

wordtoken = word_tokenize(example)

filtered_sentence = []

for w in wordtoken:
    print (w)

for w in wordtoken:
    if w not in stop_words:
        filtered_sentence.append(w)

print (filtered_sentence)

