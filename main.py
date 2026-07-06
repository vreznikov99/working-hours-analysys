import os.path
import gspread
import pprint
import duckdb
import pandas as pd

from resources import SheetManager
from credentials import sheets_details

# Service Account Credentials
cred_folder = 'credentials'
cred_file = 'service_account_creds.json'
cred_path = os.path.join(cred_folder, cred_file)


duck_db_path = os.path.join('db', 'duck.db')

con = duckdb.connect(duck_db_path)

if __name__ == '__main__':
    sh_manager_val = SheetManager('vreznikov', cred_path, sheets_details.HOURS_SHEET_ID)
    worksheet_val = sh_manager_val.extract_worksheet('IsraPorts')

    values = worksheet_val.get_all_values()
    detailed_hours = values[14:]  # Detailed Hours

    # list of dicts
    for row in detailed_hours:
        if SheetManager.is_data_row(row):
            sh_manager_val.add_to_list_of_dicts(row)

    df = sh_manager_val.create_data_frame()
    sh_manager_val.load_to_db(df, con)

    print(con.sql("SELECT COUNT(*) FROM staging").df())


