Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
>>> chrome_path = r"C:/Users/acer/Desktop/chromedriver_win32/chromedriver.exe"
>>> driver = webdriver.Chrome(chrome_path)
>>> driver.get("https://www.agoda.com/taal-vista-hotel/hotel/tagaytay-ph.html?checkin=2017-08-25&los=1&adults=2&rooms=1&cid=1646626&tag=d27fecc6-7862-fb75-5044-2883fb5cb304&searchrequestid=a1f558cd-4d12-4461-b7f7-89711fb2b851")
>>> reviews = driver.find_elements_by_class_name("comment-title-text")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    reviews = driver.find_elements_by_class_name("comment-title-text")
  File "C:\Users\acer\AppData\Local\Programs\Python\Python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 486, in find_elements_by_class_name
    return self.find_elements(by=By.CLASS_NAME, value=name)
  File "C:\Users\acer\AppData\Local\Programs\Python\Python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 858, in find_elements
    'value': value})['value']
  File "C:\Users\acer\AppData\Local\Programs\Python\Python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 297, in execute
    self.error_handler.check_response(response)
  File "C:\Users\acer\AppData\Local\Programs\Python\Python36\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: disconnected: received Inspector.detached event
  (Session info: chrome=60.0.3112.90)
  (Driver info: chromedriver=2.31.488763 (092de99f48a300323ecf8c2a4e2e7cab51de5ba8),platform=Windows NT 10.0.15063 x86_64)

>>> reviews = driver.find_elements_by_class_name("comment-title-text")
>>> posts = driver.find_elements_by_class_name("comment-title-text")
>>> for post in posts:
	print(post.text)

	
No longer the same.”
Good old hotel that still have it's charm”
Old”
Nice Getaway”
Good Location”
Facilities need upgrading especially at the mounta”
Very good”
Excellent”
Excellent”
quality service”
>>> posts = driver.find_elements_by_class_name("comment-text")
>>> for post in posts:
	print(post.text)

	
Been a Taal Vista regular for years now. However, last visit was disappointing. Made arrangements for a simple birthday surprise as I did before, but it seems like they no longer care, unlike previous years. Add to that, upon checking in our room - not the usual impressed and wow feeling...no bed runner, no throw pillows, Welcome note and goodies (usually fruits or pastries) the bathroom still had splatters on the glass, grout on the bathroom floors are visibly dirty, and into night - the aircon had a leak. Still gave it a shot for dinner, went to try the dinner buffet, but the selection was quite limited. I love Taal Vista - proposed to my wife there, also stayed there for our wedding, but maintenance and upkeep of the place has to step up. It's in the details, I guess. A great hotel experience goes down to the smallest of details. Time to explore the new options in Tagaytay. To the Management, please save Taal Vista, too many memories :(
Buffet breakfast selection was great, so many choices. Great staff from front desk to room attendants. Will definitely book again here!
We stayed at the old bldg. Yes, it's old.
It had a nice getaway at Taal Vista with a spacious and comfortable room. The view was awesome! I booked the Premiere Lake View room. It was really nice that I can stay in my room the whole day.
The hotel had a good location. Very near attractions and restaurants and also some parts were just newly renovated. I hope they could also renovate the rooms bec it's starting to look and feel old. The sliding door to the washroom doesn't work properly. The rooms at the mountain side needs renovation.
Food looks good but taste is mediocre.
good hotel, but still have room for improvement.
excellent view of the lake. good buffet selection during breakfast. mountain wing feels old though
We stayed on the lake wing, premier king. The room is clean, thee bed is comfortable, the best part of staying here is the view from our room is superb. Their is a garden right below the veranda of the room, that when you open the door what you can here is the peaceful sound of the birds. We stayed here before on a weekend, and our recent stay was on a midweek. You can enjoy more the place during midweek because they have less guest, I mean, you can enjoy more roaming around and use their pool more, check in or out more faster. But, if you'll be staying here on a weekend, their breakfast has wider selection than what they do offer during midweek. Parking is free, another thumbs up. The only downside I got same as my previous stay was their bathroom has no bidet. They even just have the shower head on the top of the bath tub , they don't have the movable shower. I rated 3* 4* their cleanliness and facilities because the sofa inside our room has stains and a little ruin, probably because of its beige color, I even had a doubt at first if will seat or not. lol Overall, our stay was pleasant.
Although we had issues during check in and there was no view from our room, our stay became memorable. It was a great venue for celebrating a wedding and at the same time family reunion. I appreciated the room attendant who cleaned our room, the guard who watched over us in the pool. and people serving at the buffet breakfast.
>>> posts = driver.find_elements_by_class_name("comment-score")
>>> for post in posts:
	print(post.text)

	
6.0
8.4
7.2
8.8
8.0
8.8
8.0
8.8
8.4
5.2
>>> 
