import sqlite3


# create a database named mydb
db = sqlite3.connect(r'db.sqlite')

# execute sql commands
cursor = db.cursor()
cursor.execute('''
    
    CREATE TABLE website(web_code INTEGER PRIMARY KEY, web_name TEXT,
                       web_url TEXT)
               ''')

cursor.execute('''  
    CREATE TABLE report(rep_code INTEGER PRIMARY KEY, rep_date TEXT)
                ''')

cursor.execute(''' 
    CREATE TABLE reviews(rev_code INTEGER PRIMARY KEY, rev_title TEXT,
                       rev_comment TEXT, rev_rating TEXT , rev_date TEXT, 
                       web_code INTEGER,
                       FOREIGN KEY(web_code) REFERENCES website(web_code)   )
                       
                ''')

cursor.execute('''
    CREATE TABLE sentiments(positive TEXT, negative TEXT,
                       rep_code INTEGER, rev_code INTEGER,
                        FOREIGN KEY(rep_code) REFERENCES report(rep_code),
                        FOREIGN KEY(rev_code) REFERENCES reviews(rev_code))
                ''')
db.commit()