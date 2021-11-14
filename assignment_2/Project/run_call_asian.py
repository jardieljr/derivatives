import xlwings as ws
import asian_option_pricing as asp

import numpy as np

#Open a new excel

app = xw.App()
app.books['../Derivatives_Project_2.xlsm']
sheet = book.sheets['Current Market Data']

K= sheet['D5'].value

price = asp.asian_option_pricing(K, option='call')

sheet = book.sheets['MC']

sheet['E2'].value = price
