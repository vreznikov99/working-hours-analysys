import gspread


class SheetManager:
    def __init__(self, employee, service_account_path, sheet_key):
        self.employee = employee
        self.service_account_path = service_account_path
        self.sheet_key = sheet_key

    def extract_worksheet(self, worksheet_name):
        gc = gspread.service_account(filename=self.service_account_path)
        sheet = gc.open_by_key(self.sheet_key)
        return sheet.worksheet(worksheet_name)

    def json(self, data_input):
        res = {
            'Employee': self.employee,
            'Year': 'year',
            'Month': 'month',
            'Date': 'date',
            'Weekday': 'weekday',
            'Start': 'start',
            'Finish': 'finish',
            'Time': 'time',
            'Comments': 'comments',
        }

    def load_to_db(self):
        pass
