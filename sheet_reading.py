import os.path
import gspread
from credentials import sheets_details

# Service Account Credentials
cred_folder = 'credentials'
cred_file = 'service_account_creds.json'
cred_path = os.path.join(cred_folder, cred_file)

gc = gspread.service_account(filename=cred_path)
sh = gc.open_by_key(sheets_details.HOURS_SHEET_ID)
worksheet = sh.worksheet('IsraPorts')

values = worksheet.get_all_values()
detailed_hours = values[14:] # Detailed Hours
header = detailed_hours[0] # Table Header

print(detailed_hours)
print(header)
