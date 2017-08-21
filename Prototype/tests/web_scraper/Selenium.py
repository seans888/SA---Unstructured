from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time

## get the Firefox profile object
firefoxProfile = FirefoxProfile()

# 1=enabled, 2=disabled ; True=enabled, False=disabled
## CSS
firefoxProfile.set_preference('permissions.default.stylesheet', 1)

## images
firefoxProfile.set_preference('permissions.default.image', 2)

## JavaScript
firefoxProfile.set_preference('javascript.enabled', True)

## Flash
firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','False')

## Use the driver
browser = webdriver.Firefox(firefoxProfile, executable_path="../../driver/geckodriver.exe")
#browser.set_window_size(200,400)
browser_wait = WebDriverWait(browser, 120)

agoda_revtitle_element = ".comment-title-text"
agoda_revcomment_element = "div[data-selenium='reviews-comments']"
agoda_revscore_element = ".comment-score span"
agoda_revdate_element = "span[name='reviewdate']"

tripad_revtitle_element = ".noQuotes"
tripad_revcomment_element = ".wrap > .prw_rup .partial_entry"
tripad_revscore_element = ".review-container span.ui_bubble_rating"
tripad_revdate_element = ".ratingDate"

booking_revtitle_element = ".sliding-panel-widget-content .review_item_header_content"
booking_revcomment_element = ".sliding-panel-widget-content .review_item_review_content p"
booking_revscore_element = ".sliding-panel-widget-content .review-score-badge"
booking_revdate_element = ".sliding-panel-widget-content .review_item_date"


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

    if website_name == "agoda" or website_name == "booking":
        for idx in range(len(review_list)):
            review_list[idx] = Review(website_name, review_titles[idx], review_comments[idx], review_scores[idx], review_dates[idx])

        for idx in range(len(review_list)):
            print("Review: "+ str(idx + 1)
                    + "\n    Title: " + review_list[idx].review_title.text
                    + "\n    Comment: " + review_list[idx].review_comment.text
                    + "\n    Score: " + review_list[idx].review_score.text
                    + "\n    Date: " + review_list[idx].review_date.text
                    + "\n    Website: " + review_list[idx].review_site)

    elif website_name == "tripadvisor":
        trip_scores = []
        for idx in review_scores:
            trip_scores.append(idx)
        review_scores.clear()
        for idx in trip_scores:
            bubble_score = idx.get_attribute("class")
            if bubble_score == "ui_bubble_rating bubble_50":
                review_scores.append("5")
            elif bubble_score == "ui_bubble_rating bubble_40":
                review_scores.append("4")
            elif bubble_score == "ui_bubble_rating bubble_30":
                review_scores.append("3")
            elif bubble_score == "ui_bubble_rating bubble_20":
                review_scores.append("2")
            else:
                review_scores.append("1")

        trip_dates = []
        for idx in review_dates:
            trip_dates.append(idx)
        review_dates.clear()
        for idx in trip_dates:
            review_dates.append(idx.get_attribute("title"))

        for idx in range(len(review_list)):
            review_list[idx] = Review(website_name, review_titles[idx], review_comments[idx], review_scores[idx], review_dates[idx])

        for idx in range(len(review_list)):
            print("Review: " + str(idx + 1)
                  + "\n    Title: " + review_list[idx].review_title.text
                  + "\n    Comment: " + review_list[idx].review_comment.text
                  + "\n    Score: " + review_list[idx].review_score
                  + "\n    Date: " + review_list[idx].review_date
                  + "\n    Website: " + review_list[idx].review_site)


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
            parse_reviews(site_title, agoda_revtitle_element, agoda_revcomment_element, agoda_revscore_element, agoda_revdate_element)
        except Exception as e:
            print(e)


def parse_tripadvisor():
    site_title = "tripadvisor"
    browser.get(
    "https://www.tripadvisor.com.ph/Hotel_Review-g317121-d320846-Reviews-Taal_Vista_Hotel-Tagaytay_Cavite_Province_Calabarzon_Region_Luzon.html")

    page_number = 0
    while page_number < 5:
        try:
            page_number += 1
            print("===================TRIPADVISOR PAGE NUMBER: " + str(page_number))
            if page_number > 1:
                if browser_wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "pageNum"))):
                    next_button = browser.find_element_by_css_selector("span[data-page-number='" + str(page_number) + "']")
                    next_button.click()

            browser_wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, tripad_revtitle_element)))
            if browser_wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "span.taLnk.ulBlueLinks"))):
                more_button = browser.find_element_by_css_selector("span.taLnk.ulBlueLinks")
                more_button.click()
            browser_wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, tripad_revtitle_element)))
            browser_wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, tripad_revcomment_element)))
            browser_wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, tripad_revscore_element)))
            browser_wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, tripad_revdate_element)))
            parse_reviews(site_title, tripad_revtitle_element, tripad_revcomment_element, tripad_revscore_element, tripad_revdate_element)
        except Exception as e:
            print(e)


def parse_booking():
    site_title = "booking"
    browser.get("https://www.booking.com/hotel/ph/taal-vista.html#tab-reviews")
    page_number = 0
    while page_number < 5:
        try:
            page_number += 1
            print("===================BOOKING PAGE NUMBER: " + str(page_number))
            if page_number > 1:
                browser_wait.until(EC.visibility_of_element_located((By.ID, "review_next_page_link")))
                next_button = browser.find_element_by_css_selector("a#review_next_page_link")
                next_button.click()

            browser_wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".sliding-panel-widget-content .review_item")))
            time.sleep(5)
            parse_reviews(site_title, booking_revtitle_element, booking_revcomment_element, booking_revscore_element, booking_revdate_element)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    parse_agoda()
    parse_tripadvisor()
    parse_booking()





