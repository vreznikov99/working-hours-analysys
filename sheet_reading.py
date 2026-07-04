import os.path
import gspread

# Service Account Credentials
cred_folder = 'credentials'
cred_file = 'service_account_creds.json'
cred_path = os.path.join(cred_folder, cred_file)

gc = gspread.service_account(filename=cred_path)
sh = gc.open_by_key('1DqAWS05a6M3EHx5jz6TpQK9hDBbIHCnrDEJ61j4oyrM')
worksheet = sh.worksheet('IsraPorts')

values = worksheet.get_all_values()
print(values[14:])
records = worksheet.get_all_records()
print(records[0])
