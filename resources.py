import gspread
import pandas as pd

class SheetManager:
    def __init__(self, employee, service_account_path, sheet_key):
        self.employee = employee
        self.service_account_path = service_account_path
        self.sheet_key = sheet_key
        self.list_of_dicts = []

    @staticmethod
    def is_data_row(row):
        return (
                row[0] != '' and
                not row[0].startswith("Date") and
                not row[3].startswith("Total")
        )

    def extract_worksheet(self, worksheet_name):
        gc = gspread.service_account(filename=self.service_account_path)
        sheet = gc.open_by_key(self.sheet_key)
        return sheet.worksheet(worksheet_name)

    def add_to_list_of_dicts(self, row):
        res = {
            'Employee': self.employee,
            'Date': row[0],
            'Month': row[5],
            'Weekday': row[1],
            'Start': row[2],
            'Finish': row[3],
            'Time': row[4],
            'Comments': row[6],
        }
        self.list_of_dicts.append(res)

    def create_data_frame(self):
        return pd.DataFrame(self.list_of_dicts)

    def load_to_db(self, data_frame, db_connection):
        df = data_frame
        db_connection.sql('''
            DROP TABLE IF EXISTS staging;
            CREATE TABLE staging AS
                SELECT *
                FROM df;
           
            ''')
 # INSERT INTO staging SELECT * FROM df;
