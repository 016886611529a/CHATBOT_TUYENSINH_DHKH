import sqlite3
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

#conn = sqlite3.connect('Vaccine.db')

#c = conn.cursor()

#c.execute("""CREATE TABLE vaccine(
#        vaccine text,
#        week text
#    )""")
#c.execute("INSERT INTO Vaccine VALUES ('pfizer','3 week')")
#c.execute("INSERT INTO Vaccine VALUES ('astrazeneca','6 week')")
#c.execute("INSERT INTO Vaccine VALUES ('verc','4 week')")
#c.execute("INSERT INTO Vaccine VALUES ('dfg','4 week')")
#c.execute("INSERT INTO Vaccine VALUES ('dfe','8 week')")
#c.execute("SELECT * FROM Vaccine")
#print(c.fetchall())
#conn.commit()
#conn.close()

def get_info_vaccine(value):
        conn = sqlite3.connect('diem2021.db')
        c = conn.cursor()
        #sqlite_select_query = '''select week from vaccine
        #          where vaccine = 'pfizer' '''
        #c.execute(sqlite_select_query)
        c.execute('PRAGMA encoding="UTF-8"')
        c.execute(f'''select * from diem2021 
                  where Nganh="{value}"''')
        conn.commit()
        record = c.fetchall()
        if len(list(record)) < 1:
                text="Khong tim thay"
        else:
        #return records
                for result in record:
                        id = result[0]
                        Nganh = result[1]
                        text="Doi voi  {} thi tiem mui 2 cach {} ạ".format(
                                result[0],result[1])
        return text

val = input()

print(get_info_vaccine(val))

val = input()

print(get_info_vaccine(val))

val = input()

print(get_info_vaccine(val))