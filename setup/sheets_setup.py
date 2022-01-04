import gspread
from oauth2client.service_account import ServiceAccountCredentials

# SHEET SETUP
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('../static/key/api.json', scope)
client = gspread.authorize(credentials)
sheet = client.open_by_key("1jGMF0OBt8x20C8eLX9u6Qx8sADyy870kLyxE0HO_U2g").sheet1
