import xlwings as ws
import asian_option_pricing as asp

#Open a new excel

book = ws.Workbook('../Derivatives_Project.xlsm')

sheet = book.sheets['Current Market Data']

K= sheet['D5'].value

asp.asian_option_pricing(K, option='call')
