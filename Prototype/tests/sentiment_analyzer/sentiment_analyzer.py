from nltk.tokenize import word_tokenize


#Open text files needed
pos_words = open("pos_dict.txt","r").read()
neg_words = open("neg_dict.txt","r").read()
guest_rating = open("hotel_reviews.txt","r").read()


#List of positive words
pos_dictionary = []
for word in pos_words.split('\n'):
    pos_dictionary.append(word)

#List of negative words
neg_dictionary = []
for word in neg_words.split('\n'):
    neg_dictionary.append(word)

hotel_reviews = []
for review in guest_rating.split('\n'):
    hotel_reviews.append(review)


p1_counter = 0
n1_counter = 0

for review in hotel_reviews:
    review_token = word_tokenize(review)

    for p in review_token:
        if p in pos_dictionary:
            p1_counter += 1

        if p in neg_dictionary:
            n1_counter += 1

    if p1_counter > n1_counter:
        print ("Comment: "+review)
        print("Pos count: "+str(p1_counter) +"\n" + "Neg count: " + str(n1_counter))
        print ("Verdict: +Positive \n")
    else:
        print ("Comment: "+ review)
        print("Pos count: "+str(p1_counter) +"\n" + "Neg count: " + str(n1_counter))
        print ("Verdict: -Negative \n")
    
    
    p1_counter = 0
    n1_counter = 0







