from selenium import webdriver
chrome_path = r"C:/Users/acer/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.agoda.com/taal-vista-hotel/hotel/tagaytay-ph.html?checkin=2017-08-25&los=1&adults=2&rooms=1&cid=1646626&tag=d27fecc6-7862-fb75-5044-2883fb5cb304&searchrequestid=a1f558cd-4d12-4461-b7f7-89711fb2b851")
reviews = driver.find_elements_by_class_name("comment-title-text")
posts = driver.find_elements_by_class_name("comment-title-text")
	for post in posts:
	print(post.text)
posts = driver.find_elements_by_class_name("comment-text")
	for post in posts:
	print(post.text)
posts = driver.find_elements_by_class_name("comment-score")
	for post in posts:
	print(post.text)