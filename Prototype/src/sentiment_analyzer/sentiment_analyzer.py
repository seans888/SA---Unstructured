from nltk.tokenize import word_tokenize
import sqlite3
import time

from time import strftime

try:
    conn = sqlite3.connect('../../db/example.db')
    c = conn.cursor()

    dic_conn = sqlite3.connect('../../db/dictionary.db')
    dict_c = dic_conn.cursor()

except Exception as e:
    print(e)


def create_report():
    current_date = strftime("%m/%d/%Y %H:%M:%S")

    c.execute("INSERT INTO report (report_date) "
              "VALUES (:report_date)"
              , {"report_date": current_date})

    conn.commit()
    c.execute("SELECT report.id FROM report WHERE report_date = :current_date", {"current_date": current_date})
    rep_id = c.fetchone()[0]
    return rep_id


def insert_to_db(report_id, review_id, sentiment):

    c.execute("INSERT INTO sentiment (report_id, review_id, sentiment) "
              "VALUES (:report_id, :review_id, :sentiment)"
              ,{"report_id": report_id, "review_id": review_id, "sentiment": sentiment})
    conn.commit()
    print("DATA INSERTED")


def extract_sentiments(report_id):

    # Reviews
    reviews = c.execute("SELECT review.id, review.comment FROM review")
    hotel_review_ids = []
    hotel_reviews = []
    for row in reviews.fetchall():
        hotel_review_ids.append(list(row)[0])
        hotel_reviews.append(list(row)[1])

    # List of positive words
    pos_words = dict_c.execute("SELECT words FROM positive_dictionary")
    pos_dictionary = []
    for row in pos_words.fetchall():
        pos_dictionary.append(list(row)[0])


    # List of negative words
    neg_words = dict_c.execute("SELECT words FROM negative_dictionary")
    neg_dictionary = []
    for row in neg_words.fetchall():
        neg_dictionary.append(list(row)[0])

    pos_counter = 0
    neg_counter = 0

    for idx in range(len(hotel_reviews)):
        review_token = word_tokenize(hotel_reviews[idx])

        for token in review_token:
            if token.lower() in pos_dictionary:
                pos_counter += 1

            if token.lower() in neg_dictionary:
                neg_counter += 1

        if pos_counter > neg_counter:
            sentiment = "positive"

        elif pos_counter < neg_counter:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        print("======================" + "\n"+
              "Comment: " + hotel_reviews[idx] + "\n"+
              "Pos count: " + str(pos_counter) + "\n"+
              "Neg count: " + str(neg_counter)+ "\n"+
              "Sentiment: "+ sentiment+ "\n"+
              "Report #: " + str(report_id))

        insert_to_db(report_id, hotel_review_ids[idx], sentiment)

        pos_counter = 0
        neg_counter = 0


if __name__ == "__main__":
    report_id = create_report()
    print("Performing Sentiment Analysis for Report Number: " + str(report_id))
    time.sleep(5)
    extract_sentiments(report_id)
    conn.close()




