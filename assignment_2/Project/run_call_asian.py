import xlwings as ws
import asian_option_pricing as asp

#Open a new excel

book = ws.Workbook('../Derivatives_Project_2.xlsm')

sheet = book.sheets['Current Market Data']

K= sheet['D5'].value

price = asp.asian_option_pricing(K, option='call')

sheet = book.sheets['MC']

sheet['E2'].value = price
