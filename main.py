import os.path
import gspread
import pprint
import duckdb
import pandas as pd

from resources import SheetManager
from credentials import sheets_details

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Service Account Credentials
cred_folder = 'credentials'
cred_file = 'service_account_creds.json'
cred_path = os.path.join(BASE_DIR, cred_folder, cred_file)

duck_db_path = os.path.join(BASE_DIR, 'db', 'duck.db')

con = duckdb.connect(duck_db_path)

if __name__ == '__main__':
    sh_manager_val = SheetManager('vreznikov', cred_path, sheets_details.HOURS_SHEET_ID)

    worksheet_hani_val = sh_manager_val.extract_worksheet('IsraPorts')
    hani_values = worksheet_hani_val.get_all_values()
    hani_detailed_hours = hani_values[14:]  # Detailed Hours

    # HANI - list of dicts
    for row in hani_detailed_hours:
        if SheetManager.is_data_row(row):
            sh_manager_val.add_to_list_of_dicts(row, 'HANI')

    worksheet_rivulis_val = sh_manager_val.extract_worksheet('Rivulis')
    rivulis_values = worksheet_rivulis_val.get_all_values()
    rivulis_detailed_hours = rivulis_values[14:]

    # Rivulis - list of dicts
    for row in rivulis_detailed_hours:
        if SheetManager.is_data_row(row):
            sh_manager_val.add_to_list_of_dicts(row, 'Rivulis')

    worksheet_other_projects_val = sh_manager_val.extract_worksheet('Other Projects')
    other_proj_values = worksheet_other_projects_val.get_all_values()
    other_proj_detailed_hours = other_proj_values[14:]

    # Other Projects - list of dicts
    for row in other_proj_detailed_hours:
        if SheetManager.is_data_row(row):
            sh_manager_val.add_to_list_of_dicts(row, 'Other Projects')

    df = sh_manager_val.create_data_frame()
    sh_manager_val.load_to_db(df, con)
    print(duck_db_path)
    print(cred_path)

    print(con.sql("SELECT COUNT(*) FROM raw_data").df())
