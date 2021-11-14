import xlwings as ws
import asian_option_pricing

#Open a new excel

book = ws.Workbook('../Derivatives_Project.xlsm')

sheet = book.sheets['Current Market Data']

K= sheet['D5'].value

asian_option_pricing(K, option='call')
