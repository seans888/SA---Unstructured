import time
import sqlite3

try:
    conn = sqlite3.connect('../../db/example.db')
    c = conn.cursor()
except Exception as e:
    print(e)

from subprocess import call


def view_analysis(id):

    report_id = id

    # Agoda
    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = :report AND website.name = :website_name",
              {"sentiment": "positive","website_name": "agoda", "report": report_id})
    agoda_positive_count = c.fetchone()[0]

    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = :report AND website.name = :website_name",
              {"sentiment": "negative", "website_name": "agoda", "report": report_id})
    agoda_negative_count = c.fetchone()[0]

    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = :report AND website.name = :website_name",
              {"sentiment": "neutral", "website_name": "agoda", "report": report_id})
    agoda_neutral_count = c.fetchone()[0]

    # TripAdvisor
    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = :report AND website.name = :website_name",
              {"sentiment": "positive", "website_name": "tripadvisor", "report": report_id})
    tripadvisor_positive_count = c.fetchone()[0]

    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = :report AND website.name = :website_name",
              {"sentiment": "negative", "website_name": "tripadvisor", "report": report_id})
    tripadvisor_negative_count = c.fetchone()[0]

    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = :report AND website.name = :website_name",
              {"sentiment": "neutral", "website_name": "tripadvisor", "report": report_id})
    tripadvisor_neutral_count = c.fetchone()[0]

    # Booking
    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = :report AND website.name = :website_name",
              {"sentiment": "positive", "website_name": "booking", "report": report_id})
    booking_positive_count = c.fetchone()[0]

    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = :report AND website.name = :website_name",
              {"sentiment": "negative", "website_name": "booking", "report": report_id})
    booking_negative_count = c.fetchone()[0]

    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN review ON review.id = sentiment.review_id "
              "INNER JOIN report ON report.id = sentiment.report_id "
              "INNER JOIN website ON website.id = review.website_id "
              "WHERE sentiment = :sentiment AND report.id = :report AND website.name = :website_name",
              {"sentiment": "neutral", "website_name": "booking", "report": report_id})
    booking_neutral_count = c.fetchone()[0]


    # Overall
    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN report ON report.id = sentiment.report_id "
              "where sentiment = :sentiment and sentiment.report_id = :report", {"sentiment": "positive", "report": report_id})
    overall_positive_count = c.fetchone()[0]

    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN report ON report.id = sentiment.report_id "
              "where sentiment = :sentiment and sentiment.report_id = :report", {"sentiment": "negative", "report": report_id})
    overall_negative_count = c.fetchone()[0]

    c.execute("SELECT COUNT(sentiment) FROM sentiment INNER JOIN report ON report.id = sentiment.report_id "
              "where sentiment = :sentiment and sentiment.report_id = :report", {"sentiment": "neutral", "report": report_id})
    overall_neutral_count = c.fetchone()[0]




    print("Report Number: "+ str(report_id) +"\n"+
          "Agoda:\n    Positive: "+ str(agoda_positive_count) +"\n"+
          "    Negative: " + str(agoda_negative_count) + "\n" +
          "    Neutral: " + str(agoda_neutral_count) + "\n" +
          "TripAdvisor:\n    Positive: "+ str(tripadvisor_positive_count) +"\n"+
          "    Negative: " + str(tripadvisor_negative_count) + "\n" +
          "    Neutral: " + str(tripadvisor_neutral_count) + "\n" +
          "Booking:\n    Positive: "+ str(booking_positive_count) +"\n"+
          "    Negative: " + str(booking_negative_count) + "\n" +
          "    Neutral: " + str(booking_neutral_count) + "\n" +
          "Overall Positive: "+ str(overall_positive_count) +"\n"+
          "Overall Negative: " + str(overall_negative_count) +"\n"+
          "Overall Neutral: " + str(overall_neutral_count))


def start_app():
    print("Performing Web Data Extraction...")

    call('python ../web_scraper/Selenium.py', shell=True)

    print("Performing Sentiment Analysis...")
    time.sleep(3)

    call('python ../sentiment_analyzer/sentiment_analyzer.py', shell=True)

    print("=================== ANALYSIS Complete ===================")


if __name__ == "__main__":
    print("Sentiment Analysis App")

    try:
        user_input = input("Enter 'Start' to start or 'View' to view report: ")
        if user_input.lower() == "start":
            start_app()
        elif user_input.lower() == "view" :
            input_id = int(input("Enter report number: "))
            view_analysis(input_id)
    except Exception as e:
        pass
