from selenium import webdriver


chrome_driver_path = "../../driver/chromedriver.exe"

browser = webdriver.Chrome(chrome_driver_path)

browser.get("https://www.agoda.com/taal-vista-hotel/hotel/tagaytay-ph.html?checkin=2017-08-25&los=1&adults=2&rooms=1&cid=1646626&tag=d27fecc6-7862-fb75-5044-2883fb5cb304&searchrequestid=a1f558cd-4d12-4461-b7f7-89711fb2b851")

review_titles = browser.find_elements_by_class_name("comment-title-text")
for post in review_titles:
    print(post.text)

review_comments = browser.find_elements_by_class_name("comment-text")

for post in review_comments:
    print(post.text)

review_scores = browser.find_elements_by_class_name("comment-score")

for post in review_scores:
    print(post.text)


