import sqlite3

db = sqlite3.connect(r'test.sqlite')


# variable values------------------------------------------------------------------------

# for insert report
cursor = db.cursor()
rep_Code = '001'
rep_Date = '01-01-2017'

# for insert review
rev_Code = '0010'
rev_Title = 'crappy bedroom'
rev_Comment = 'the beds made my back hurt'
rev_Rating = '4'
rev_Date = '12-30-2016'


# for insert sentiments
positive = '1'
negative = '2'


# for insert Website
web_Code = '0100'
web_Name = 'Agoda'
web_Url  = 'Agoda.com'
# insert commands--------------------------------------------------------------------------

# Insert report
cursor.execute('''INSERT INTO Report(rep_Code, rep_Date)
                  VALUES(?,?)''', (rep_Code, rep_Date))
print('report values inserted')


# Insert review
cursor.execute('''INSERT INTO Review(rev_Code, rev_title, rev_Comment, rev_Rating, rev_Date, Website_web_Code)
                  VALUES(?,?,?,?,?,?)''', (rev_Code, rev_Title, rev_Comment, rev_Rating, rev_Date, web_Code ))
print('review values inserted')

# Insert sentiments
cursor.execute('''INSERT INTO Sentiments(positive, negative, rep_Code, rev_Code)
                  VALUES(?,?,?,?)''', (positive, negative, rep_Code, rev_Code))
print('sentiment values inserted')

# Insert website
cursor.execute('''INSERT INTO Website(web_Code, web_Name, web_Url)
                  VALUES(?,?,?)''', (web_Code, web_Name, web_Url))
print('website values inserted')

db.commit()