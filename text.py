from typing import Text, List, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
from sqlite3 import Error







def get_info_vaccine(c):


        c.execute(f"select Nganh,Diem from diem2021")
        records = c.fetchall()
        return  records






def chay_code():
    conn = sqlite3.connect('diem2021.db')
    c = conn.cursor()


    return str(get_info_vaccine(c))
get_info_vaccine()







