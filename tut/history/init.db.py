
import sqlite3
import markdown as md


db_file = '/my/outside/history.db'
timeline_file = 'timeline.md'
#out_file = '/tmp/h.html'
out_file = 'htmlized.txt'

seperator = '\nseperator-py-js\n'

conn = sqlite3.connect(db_file)

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
def create_table():
    #c.execute('''CREATE TABLE IF NOT EXISTS event(
    c.execute('''CREATE TABLE event(
        what TEXT,
        story TEXT,

        theTime datetime DEFAULT null,
        floatBc REAL DEFAULT null,
        in4dSpace TEXT DEFAULT null,
        universeAge REAL DEFAULT null,

        location TEXT DEFAULT null,
        language TEXT DEFAULT null
        )''')


import re

with open(timeline_file, 'r') as text:
    s = text.read()


    es = re.split(r'\n\#', s, maxsplit=0)

    #insert_batch(es);


def insert_batch(es):
    for event in es:
        sql = """INSERT INTO event (story)
            VALUES ( '''{}''')""".format('#' + event)


        print(sql)

        c.execute(sql)
        conn.commit()




#with open('/tmp/h.html', 'w') as hh:
#    hh.write(html)




#c.execute("""INSERT INTO event
#    (what, in4dSpace, story)
#    VALUES ('Big Bang',
#    '0s, zero point of time',
#
#    '''
#    It happened, and everything comes.
#
#    据说世界的起源， 是在 137.98 亿年前开始的大爆炸。
#
#    当时的宇宙是一个奇异的点，很小的一点， 比沙粒更细小。
#    然而在这个点里，没有大与小的概念。
#    '''
#
#    )""")




# Save (commit) the changes




conn.close()



def convert(inf, outf, seperator=seperator):
    with open(inf, 'r') as text:
        s = text.read()
        pass

    es = re.split(r'\n\#', s, maxsplit=0)

    tt = []
    for t in es:
        tt.append(md.markdown(t))

    html = seperator.join(tt)

    with open(outf, 'w') as out:
        out.write(html)


convert(timeline_file, out_file)
