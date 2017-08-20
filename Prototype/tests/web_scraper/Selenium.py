from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## get the Firefox profile object
firefoxProfile = FirefoxProfile()

# 1=enabled, 2=disabled ; True=enabled, False=disabled
## CSS
firefoxProfile.set_preference('permissions.default.stylesheet', 2)

## images
firefoxProfile.set_preference('permissions.default.image', 2)

## JavaScript
firefoxProfile.set_preference('javascript.enabled', True)

## Flash
firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','False')

## Use the driver
browser = webdriver.Firefox(firefoxProfile, executable_path="../../driver/geckodriver.exe")
browser.set_window_size(200,400)



class Review:
    def __init__(self, title, comment, score, review_date):
        self.review_title = title
        self.review_comment = comment
        self.review_score = score
        self.review_date = review_date


def parse_reviews():
    review_titles = browser.find_elements_by_class_name("comment-title-text")
    review_comments = browser.find_elements_by_class_name("comment-text")
    review_scores = browser.find_elements_by_class_name("comment-score")
    review_dates = browser.find_elements_by_name('reviewdate')

    review_list = []

    for idx in range(len(review_titles)):
        review_list.append(idx)

    for idx in range(len(review_list)):
        review_list[idx] = Review(review_titles[idx], review_comments[idx], review_scores[idx], review_dates[idx])

        print("Review: "+ str(idx + 1)
              + "\n    Title: " + review_list[idx].review_title.text
              + "\n    Comment: " + review_list[idx].review_comment.text
              + "\n    Score: " + review_list[idx].review_score.text
              + "\n    Date: " + review_list[idx].review_date.text)


def main():
    browser.get("https://www.agoda.com/taal-vista-hotel/hotel/tagaytay-ph.html")
    browser_wait = WebDriverWait(browser, 10000)
    page_number = 0
    while page_number < 3:
        try:
            page_number += 1
            print("===================PAGE NUMBER: " + str(page_number))
            browser_wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "individual-review-item")))
            next_button = browser.find_element_by_css_selector("a[data-page='" + str(page_number) + "']")
            next_button.click()
            parse_reviews()
        except Exception as e:
            print(e)

    browser.close()


if __name__ == "__main__":
    main()





