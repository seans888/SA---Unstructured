import sqlite3

# create a database named mydb
db = sqlite3.connect(r'test.sqlite')

# execute sql commands
cursor = db.cursor()
cursor.execute('''

    CREATE TABLE "Report"(
  "rep_Code" INTEGER PRIMARY KEY NOT NULL,
  "rep_Date" DATE,
  CONSTRAINT "rep_Code_UNIQUE"
    UNIQUE("rep_Code"))
               ''')

cursor.execute('''
    CREATE TABLE "Website"(
  "web_Code" INTEGER PRIMARY KEY NOT NULL,
  "web_Name" VARCHAR(45),
  "web_Url" VARCHAR(45)
)
                ''')

cursor.execute('''
    CREATE TABLE "Review"(
  "rev_Code" INTEGER PRIMARY KEY NOT NULL,
  "rev_Title" VARCHAR(45),
  "rev_Comment" VARCHAR(45),
  "rev_Rating" VARCHAR(45),
  "rev_Date" DATE,
  "Website_web_Code" INTEGER NOT NULL,
  CONSTRAINT "rev_Code_UNIQUE"
    UNIQUE("rev_Code"),
  CONSTRAINT "fk_Review_Website1"
    FOREIGN KEY("Website_web_Code")
    REFERENCES "Website"("web_Code")
)

                ''')

cursor.execute('''
    CREATE INDEX "Review.fk_Review_Website1_idx" ON "Review" ("Website_web_Code");
''')

cursor.execute('''
               
CREATE TABLE "Sentiments"(
  "positive" BINARY,
  "negative" BINARY,
  "rep_Code" INTEGER NOT NULL,
  "rev_Code" INTEGER NOT NULL,
  CONSTRAINT "rep_Code"
    FOREIGN KEY("rep_Code")
    REFERENCES "Report"("rep_Code"),
  CONSTRAINT "rev_Code"
    FOREIGN KEY("rev_Code")
    REFERENCES "Review"("rev_Code")
)
                ''')

cursor.execute('''
    CREATE INDEX "Sentiments.rep_Code_idx" ON "Sentiments" ("rep_Code")
                ''')

cursor.execute('''
    CREATE INDEX "Sentiments.rev_Code_idx" ON "Sentiments" ("rev_Code")
                ''')
db.commit()
