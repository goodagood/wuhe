
import sqlite3

conn = sqlite3.connect('history.db')

c = conn.cursor()

# Create table of 'event'
# what : a short name, or title
# theTime : time might be keyword, name the column as 'theTime'.
#   data type should be compatible SQL DateTime.
# floatBc : type of REAL, unit is year, 
#   0.0 is for event of Christ birthday, 
#   it has enough range for all time, -1E38 -> 1E38
#   easy to overpass limit of calendar.
#   300.33 means about 300.33BC
# in4dSpace : It's text, when and where in 4 dimension space
c.execute('''CREATE TABLE IF NOT EXISTS event(
    what TEXT,
    story TEXT,

    theTime datetime DEFAULT null,
    floatBc REAL DEFAULT null,
    in4dSpace TEXT DEFAULT null,
    universeAge REAL DEFAULT null,

    location TEXT DEFAULT null,
    language TEXT DEFAULT null
    )''')


#with open('./his.md', 'r') as text:
    #text.readlines()
    #pass


c.execute("""INSERT INTO event
    (what, in4dSpace, story)
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
