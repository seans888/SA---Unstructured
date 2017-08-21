#import nltk
#nltk.download

from nltk.tokenize import sent_tokenize, word_tokenize

sentiment_sentence = "Sentiment Analysis seems to be an interesting subject to me. I hope this project will turn out to be a success after a couple more terms. Everything I said above is a lie. I'm just kidding LMAO. Please don't give me an R in the Finals."

print (sent_tokenize(sentiment_sentence))
print (word_tokenize(sentiment_sentence))

for s in (sent_tokenize(sentiment_sentence)):
	print (s)
	
for a in (word_tokenize(sentiment_sentence)):
	print (a)