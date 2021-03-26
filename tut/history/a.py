

import sqlite3
import re

db_file = '/my/outside/history.db'
timeline_file = 'timeline.md'


with open(timeline_file, 'r') as text:
    s = text.read()
    es = re.split(r'\n\#', s, maxsplit=0)



    for event in es:
        sql = """INSERT INTO event (story)
            VALUES ( '''{}''')""".format('#' + event)

        print(sql)


print(len(es))
