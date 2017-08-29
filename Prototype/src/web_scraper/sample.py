from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import sqlite3

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

try:
    conn = sqlite3.connect('../../db/example.db')
    c = conn.cursor()
except Exception as e:
    print(e)


def insert_to_db(review_site, title, comment, score, review_date):

    if review_site == "agoda":
        review_site = 1
    elif review_site == "tripadvisor":
        review_site = 2
    else:
        review_site = 3

    c.execute("INSERT INTO review (title, comment, score, review_date, website_id) "
              "VALUES (:title, :comment, :score, :review_date, :website_id)"
              ,{"title": title, "comment": comment, "score": score, "review_date": review_date,"website_id": review_site})

    conn.commit()

    print("DATA INSERTED")




## Use the driver
#browser = webdriver.Firefox(firefoxProfile, executable_path="../../driver/geckodriver.exe")
#browser.set_window_size(200,400)
#browser_wait = WebDriverWait(browser, 120)


service = webdriver.chrome.service.Service(os.path.abspath("../../driver/chromedriver.exe"))
service.start()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application"


browser = webdriver.Remote(service.service_url,   desired_capabilities=chrome_options.to_capabilities())

agoda_revtitle_element = ".comment-title-text"
agoda_revcomment_element = "div[data-selenium='reviews-comments']"
agoda_revscore_element = ".comment-score span"
agoda_revdate_element = "span[name='reviewdate']"

class Review:
    def __init__(self, review_site, title, comment, score, review_date):
        self.review_site = review_site
        self.review_title = title
        self.review_comment = comment
        self.review_score = score
        self.review_date = review_date


def parse_reviews(website_name,review_title_element, review_comment_element, review_score_element, review_date_element):

    review_titles = browser.find_elements_by_css_selector(review_title_element)
    review_comments = browser.find_elements_by_css_selector(review_comment_element)
    review_scores = browser.find_elements_by_css_selector(review_score_element)
    review_dates = browser.find_elements_by_css_selector(review_date_element)

    review_list = []
    for idx in range(len(review_titles)):
        review_list.append(idx)

    if website_name == "agoda":

        agoda_dates = []
        for idx in review_dates:
            agoda_dates.append(idx.text[9:])

        review_dates.clear()

        for idx in agoda_dates:
            review_dates.append(idx)


        for idx in range(len(review_list)):
            review_list[idx] = Review(website_name, review_titles[idx], review_comments[idx], review_scores[idx],
                                      review_dates[idx])

        for idx in range(len(review_list)):
            print("Review: " + str(idx + 1)
                  + "\n    Title: " + review_list[idx].review_title.text
                  + "\n    Comment: " + review_list[idx].review_comment.text
                  + "\n    Score: " + review_list[idx].review_score.text
                  + "\n    Date: " + review_list[idx].review_date
                  + "\n    Website: " + review_list[idx].review_site)



            #insert_to_db(review_list[idx].review_site, review_list[idx].review_title.text,
            #            review_list[idx].review_comment.text, float(review_list[idx].review_score.text),
            #            review_list[idx].review_date.text)


def parse_agoda():
    site_title = "agoda"
    browser.get("https://www.agoda.com/taal-vista-hotel/hotel/tagaytay-ph.html")
    page_number = 0

    try:
        browser.find_element_by_css_selector(".cancel").click()
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_css_selector("#promoinbox-popup-close-icon").click()
    except NoSuchElementException:
        pass

    while page_number < 5:
        try:
            page_number += 1
            print("===================AGODA PAGE NUMBER: " + str(page_number))
            if page_number > 1:
                next_button = browser.find_element_by_css_selector("a[data-page='" + str(page_number) + "']")
                next_button.click()
            browser_wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "individual-review-item")))
            if page_number > 1:
                next_button = browser.find_element_by_css_selector("a[data-page='" + str(page_number) + "']")
                next_button.click()
            browser_wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "individual-review-item")))
            parse_reviews(site_title, agoda_revtitle_element, agoda_revcomment_element, agoda_revscore_element, agoda_revdate_element)
        except Exception as e:
            print(e)






if __name__ == "__main__":
    parse_agoda()


    browser.close()
    conn.close()





