import gspread
from oauth2client.service_account import ServiceAccountCredentials

# SHEET SETUP
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('setup/key/api.json', scope)
client = gspread.authorize(credentials)
spreadsheet = client.open_by_key("10DJkzKNhzFGMmTujEvG9uHw3lxe-W7RD1A39BMTZTjU")
