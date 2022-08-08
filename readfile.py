# Importing the required tools for traversing in excel and accessing date
import openpyxl
import datetime
import time

# Configuring the path of the source file and loading it in a data frame
path = ("birthdayList.xlsx")
wb = openpyxl.load_workbook(path)
sheet = wb.active

# Converting the name and birthdays into a tuple and initialising an empty dictionary
bday_dict = {}
cells = sheet['D3' : 'E82']

# Converting string format of the date into datetime format for easy comparison
def convert(date):
   format = '%m/%d/%Y'
   date_str = datetime.datetime.strptime(date, format).strftime('%m-%d')
   return date_str

for name, bday in cells : bday_dict[name.value] = convert(bday.value)

# Checking through the dictionary and creating the list of people whose birthday is present
def check_bday(dict, date): return {k for k, v in dict.items() if v == date}

# Checking
today = time.strftime('%m-%d')

print(check_bday(bday_dict, today))