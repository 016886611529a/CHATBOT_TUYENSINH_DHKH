from typing import Text, List, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
from sqlite3 import Error

class ActionRecommend(Action):

    def name(self) -> Text:
        return "action_vaccine_week"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = DbQueryingMethods.create_connection(db_file="InfoVaccine.db")
        values = tracker.get_slot("vaccine")
        vaccine = "vaccine"

        get_query_results = DbQueryingMethods.get_info_vaccine(conn=conn,vaccine=vaccine,value=values)
        return_text = DbQueryingMethods.rows_info_as_text(get_query_results)
        dispatcher.utter_message(text=str(return_text))

        return

class DbQueryingMethods:

    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    def get_info_vaccine(conn,vaccine,value):
        c = conn.cursor()
        c.execute(f'''select * from vaccine 
                  where {vaccine}="{value}"''')
        records = c.fetchall()
        return records

    def rows_info_as_text(records):
        if len(list(records)) < 1:
            return f"Không có thông tin về loại vaccine này"
        else:
            for result in records:
                vaccine = result[0].lower()
                week = result[1]
                return f"Đối với vaccine {(result[0]).lower()} thì tiêm mũi 2 cách {result[1]} tuần ạ."
