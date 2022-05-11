import sqlite3
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

conn = sqlite3.connect('diem2021.db')

c = conn.cursor()

#c.execute("""CREATE TABLE vaccine(
#        vaccine text,
#        week text
#    )""")
#c.execute("INSERT INTO Vaccine VALUES ('pfizer','3 week')")
#c.execute("INSERT INTO Vaccine VALUES ('astrazeneca','6 week')")
#c.execute("INSERT INTO Vaccine VALUES ('verc','4 week')")
#c.execute("INSERT INTO Vaccine VALUES ('dfg','4 week')")
#c.execute("INSERT INTO Vaccine VALUES ('dfe','8 week')")
c.execute('PRAGMA encoding="UTF-8"')
c.execute('SELECT * FROM diem2021 where Nganh= "han nom"')
print(c.fetchall())
conn.commit()
conn.close()