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


def parse_reviews():
    review_titles = browser.find_elements_by_class_name("comment-title-text")
    review_comments = browser.find_elements_by_class_name("comment-text")
    review_scores = browser.find_elements_by_class_name("comment-score")
    review_dates = browser.find_elements_by_name('reviewdate')

    for review_title in review_titles:
        print(review_title.text)

    for review_comment in review_comments:
        print(review_comment.text)

    for review_score in review_scores:
        print(review_score.text)

    for review_date in review_dates:
        print(review_date.text)


def main():
    browser.get("https://www.agoda.com/taal-vista-hotel/hotel/tagaytay-ph.html")
    browser_wait = WebDriverWait(browser, 30)
    page_number = 0
    while page_number <= 4:
        try:
            page_number += 1
            print("===================PAGE NUMBER: " + str(page_number))
            browser_wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "individual-review-item")))
            next_button = browser.find_element_by_css_selector("a[data-page='" + str(page_number) + "']")
            next_button.click()
            parse_reviews()
        except:
            print('An error occured.')

    browser.close()


if __name__ == "__main__":
    main()





