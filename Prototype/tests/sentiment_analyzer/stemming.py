from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

sbs = SnowballStemmer("english")

stem_words = ["Pushed","Defending","Wrecker","Doing","Scanner","Fortified","Winning"]

for s in stem_words:
    print(sbs.stem(s))

stem_sent = "Team Liquid are doing it. They have pushed through the midlane and Newbee are struggling at defending their own base with their fortification disabled."

stem_token = word_tokenize(stem_sent)

for t in stem_token:
    print(sbs.stem(t))
