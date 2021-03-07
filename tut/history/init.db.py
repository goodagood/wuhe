
import sqlite3

conn = sqlite3.connect('history.db')

c = conn.cursor()

# Create table of 'event'
# what : a short name, or title
# theTime : time might be keyword, name the column as 'theTime'.
#   data type should be compatible SQL DateTime.
# floatTime : type of REAL, unit is year,
#   it has enough range for all time, -1E38 -> 1E38
#   easy to overpass limit of calendar.
#   0.0 is for event of Christ birthday, 
#   300.33 means about 300.33BC
# bigBangTime : It's text, tell time from the big bang. 
c.execute('''CREATE TABLE IF NOT EXISTS event(
    what TEXT,
    story TEXT,

    theTime datetime DEFAULT null,
    floatTime REAL DEFAULT null,
    bigBangTime TEXT DEFAULT null,

    location TEXT DEFAULT null,
    language TEXT DEFAULT null
    )''')


#with open('./his.md', 'r') as text:
    #text.readlines()
    #pass


c.execute("""INSERT INTO event
    (what, bigBangTime, story)
    VALUES ('Big Bang',
    '0s, zero point of time',

    '''
    It happened, and everything comes.

    据说世界的起源， 是在 137.98 亿年前开始的大爆炸。

    当时的宇宙是一个奇异的点，很小的一点， 比沙粒更细小。
    然而在这个点里，没有大与小的概念。
    '''

    )""")




# Save (commit) the changes
conn.commit()

conn.close()
