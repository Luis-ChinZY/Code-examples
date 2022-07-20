# A tool to select a date data from a gsheet using gspread (in google colab)
import pandas as pd
import gspread 
from google.auth import default
creds, _ = default()

gc = gspread.authorize(creds)

sheetname = 'sh' # sheetname is the name at top left
worksheetname = 'ws'

sheet1 = gc.open(sheetname).worksheet(worksheetname)   #open a worksheet
list1 = sheet1.get_all_values() #get all data in sheet as list
df1 = pd.DataFrame.from_records(list1)

# Get yesterday data as example
df1['date'] = pd.to_datetime(df1['date']), format = '%m/%d/%Y')
today = date.today()
yesterday = today - timedelta(1)
yesterday = str(yesterday)

df2 = df1.copy()
df2 = df2[df2['date'] == yesterday] # change date here (d/m/year)

