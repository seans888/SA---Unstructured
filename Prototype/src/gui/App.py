import time
import sqlite3


try:
    conn = sqlite3.connect('../../db/example.db')
    c = conn.cursor()
except Exception as e:
    print(e)


def view_analysis():

    # Agoda
    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = 1 AND website.name = :website_name", {"sentiment": "positive","website_name": "agoda" })
    agoda_positive_count = c.fetchone()[0]

    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = 1 AND website.name = :website_name",
              {"sentiment": "negative", "website_name": "agoda"})
    agoda_negative_count = c.fetchone()[0]

    # TripAdvisor
    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = 1 AND website.name = :website_name",
              {"sentiment": "positive", "website_name": "tripadvisor"})
    tripadvisor_positive_count = c.fetchone()[0]

    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = 1 AND website.name = :website_name",
              {"sentiment": "negative", "website_name": "tripadvisor"})
    tripadvisor_negative_count = c.fetchone()[0]

    # Booking
    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = 1 AND website.name = :website_name",
              {"sentiment": "positive", "website_name": "booking"})
    booking_positive_count = c.fetchone()[0]

    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = 1 AND website.name = :website_name",
              {"sentiment": "negative", "website_name": "booking"})
    booking_negative_count = c.fetchone()[0]

    # Overall
    c.execute("SELECT COUNT(sentiment) FROM sentiment where sentiment = :sentiment", {"sentiment": "positive"})
    overall_positive_count = c.fetchone()[0]

    c.execute("SELECT COUNT(sentiment) FROM sentiment where sentiment = :sentiment", {"sentiment": "negative"})
    overall_negative_count = c.fetchone()[0]


    report_id = 1

    print("Report Number: "+ str(report_id) +"\n"+
          "Agoda:\n    Positive: "+ str(agoda_positive_count) +"\n"+
          "    Negative: " + str(agoda_negative_count) + "\n" +
          "TripAdvisor:\n    Positive: "+ str(tripadvisor_positive_count) +"\n"+
          "    Negative: " + str(tripadvisor_negative_count) + "\n" +
          "Booking:\n    Positive: "+ str(booking_positive_count) +"\n"+
          "    Negative: " + str(booking_negative_count) + "\n" +
          "Overall Positive: "+ str(overall_positive_count) +"\n"+
          "Overall Negative: " + str(overall_negative_count))


def start_app():
    print("Performing Web Data Extraction...")
    time.sleep(3)
    exec(open('../web_scraper/Selenium.py').read())
    print("Performing Sentiment Analysis...")
    time.sleep(3)
    exec(open('../sentiment_analyzer/sentiment_analyzer.py').read())
    print("=================== ANALYSIS Result ===================")
    view_analysis()

if __name__ == "__main__":
    print("Sentiment Analysis App")

    try:
        user_input = input("Enter 'Start' to start or 'View' to view report: ")
        if user_input.lower() == "start":
            start_app()
        elif user_input.lower() == "view" :
            view_analysis()
    except Exception as e:
        pass
