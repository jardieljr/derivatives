import xlwings as ws

#Open a new excel

book = ws.Workbook(../)

sheet = book.sheets[Current Market Data]

sheet['D5'].value = K

asian_option_pricing(K, option='call')
