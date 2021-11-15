import xlwings as ws
import asian_option_pricing as asp

#Open a new excel

#app = ws.App(visible=False)
#book = app.books.open('Derivatives_Project_2.xlsm')
book = ws.Book('Derivatives_Project_2.xlsm')
sheet = book.sheets['Current Market Data']

K= sheet['D5'].value

price = asp.asian_option_pricing(K, option='put')

sheet = book.sheets['MC']

sheet['E2'].value = price

book.save()
book.close()
