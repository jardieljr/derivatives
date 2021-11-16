#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:04:34 2021

@author: jardieljunior
"""

import tkinter as tk
from tkinter import font  as tkfont
from tkinter import ttk
import asian_option_pricing
import american_option_pricing 
import numpy as np


class SampleApp(tk.Tk, asian_option_pricing.AsianOption):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.title_font = tkfont.Font(family='Helvetica', size=25, weight="bold", slant="italic")
        

    def switch_frame(self, frame_class):

        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
        
        
     
class StartPage(tk.Frame):
    
    def __init__(self, master):
        
        tk.Frame.__init__(self, master)

        start_label = tk.Label(self, text="Derivatives Project - Toulouse School of Management")
        page_1_button = tk.Button(self, text="Monte Carlo Simulation",
                                  command=lambda: master.switch_frame(VariablesPage))
            
        welcome_label = tk.Label(self, text = 'Options Pricing')
#        page_2_button = tk.Button(self, text="Parametric Simulation",
#                                  command=lambda: master.switch_frame(ParametricPage))
        
        start_label.pack(side="top", fill="x", pady=10)
        welcome_label.pack(side = "top", fill = 'x', pady = 15)
        page_1_button.pack()

#        page_2_button.pack()





class VariablesPage(tk.Frame):
    
    def __init__(self, master):
        self.entry_fields = [{}, {'Stock Price': '', 'Exercise':'', 'Option Type': '', 'BVolatility': ''}]
        self.fields = [{}, {'var': 'Variable 1', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '' , 'classification' : ''}, {'var': 'Variable 2', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '', 'classification' :'' }, {'var': 'Variable 3', 'name':'', 'type': '', 'avg': '', 'std': '', 'min': '', 'max': '', 'classification': ''}]

        tk.Frame.__init__(self, master)
        page_1_label = tk.Label(self, text= "Parameters")  
        page_1_label.grid(row = 0, column = 2)
        self.start_button = tk.Button(self, text="Back", command=lambda: master.switch_frame(StartPage))

        stock_price_label = tk.Label(self, text = 'Stock Price')
        stock_price_label.grid(row = 2, column = 1)
        
        
        self.stock_price_variable = tk.Entry(self)
        self.stock_price_variable.grid(row = 2, column = 2)
        
        volatility_label = tk.Label(self, text = 'Volatility')
        volatility_label.grid(row = 3, column = 1)
        
        
        self.volatility_variable = tk.Entry(self)
        self.volatility_variable.grid(row = 3, column = 2)    
        
        # exercise_label = tk.Label(self, text = 'Exercise')
        # exercise_label.grid(row = 4, column = 1) 
        
        # self.exercise_variable = tk.Entry(self)
        # self.exercise_variable.grid(row = 4, column = 2) 
        
        
        option_side_label = tk.Label(self, text = 'Option Side')
        option_side_label.grid(row = 4, column = 1)
        
        
        OPTIONS = [
        "Call",
        "Put"
        ] 
        self.option_side_variable = tk.StringVar(self)
        self.option_side_variable.set('Call')  
        drop_menu_option_side = tk.OptionMenu(self, self.option_side_variable, *OPTIONS)     
        drop_menu_option_side.grid(row = 4, column = 2)   

        
        risk_free_rate_label = tk.Label(self, text = 'Risk Free Rate')
        risk_free_rate_label.grid(row = 5, column = 1)
        
        self.risk_free_rate_variable = tk.Entry(self)
        self.risk_free_rate_variable.grid(row = 5, column = 2)
        
        
        expected_return_label = tk.Label(self, text = 'Expected Return')
        expected_return_label.grid(row = 6, column = 1)
        
        
        self.expected_return_variable = tk.Entry(self, text = 'Expected Return')
        self.expected_return_variable.grid(row = 6, column = 2)
        
        
        dividend_rate_label = tk.Label(self, text = 'Dividend Rate')
        dividend_rate_label.grid(row=7, column = 1)
        
        self.dividend_rate_variable = tk.Entry(self)
        self.dividend_rate_variable.grid(row=7, column = 2)
        
        
        strike_label = tk.Label(self, text = 'Strike Price')
        strike_label.grid(row=8, column = 1)
        
        self.strike_variable = tk.Entry(self)
        self.strike_variable.grid(row=8, column = 2)
        
        
        time_to_maturity_label = tk.Label(self, text = 'Time to Maturity (Year Fraction)')
        time_to_maturity_label.grid(row=9, column = 1)
        
        self.time_to_maturity_variable = tk.Entry(self)
        self.time_to_maturity_variable.grid(row=9, column = 2)
        
        
         
        n_simulations_label = tk.Label(self, text = 'Number of Simulations')
        n_simulations_label.grid(row=10, column = 1)
        
        self.n_simulations_variable = tk.Entry(self)
        self.n_simulations_variable.grid(row=10, column = 2)
        
        option_type_label = tk.Label(self, text = 'Option Type')
        option_type_label.grid(row=11, column = 1)
        
        
        OPTION_TYPE = [
            'American',
            'Asian'
            ]
        
        self.option_type_variable = tk.StringVar(self)
        self.option_type_variable.set('American')  
        drop_menu_option_type = tk.OptionMenu(self, self.option_type_variable, *OPTION_TYPE)     
        drop_menu_option_type.grid(row = 11, column = 2)
        
        self.run_model_button = tk.Button(self, text = 'Run Model',
                                          command = lambda : self.runModel())
        self.run_model_button.grid(row=1, column = 1)  
        
        

        
    def runModel(self):
   
        
        if self.option_type_variable.get() == 'Asian':
            
       
            obj = asian_option_pricing.AsianOption(100,#M
                                                      float(self.strike_variable.get()), 
                                                      self.option_side_variable.get(), 
                                                      float(self.stock_price_variable.get()), 
                                                      float(self.volatility_variable.get()), 
                                                      float(self.time_to_maturity_variable.get()), 
                                                      float(self.risk_free_rate_variable.get()), 
                                                      int(self.n_simulations_variable.get()))
            
          
            price = np.round(obj.asian_option_pricing(),4)
            
        
            results_label = tk.Label(self, text = f'Option Price: {price}')
            results_label.grid(row=2, column = 3)
        
        
        elif self.option_type_variable.get() == 'American':
            
            
            obj = american_option_pricing.AmericanOption(100,#M
                                                      float(self.strike_variable.get()), 
                                                      self.option_side_variable.get(), 
                                                      float(self.stock_price_variable.get()), 
                                                      float(self.volatility_variable.get()), 
                                                      float(self.time_to_maturity_variable.get()), 
                                                      float(self.risk_free_rate_variable.get()), 
                                                      int(self.n_simulations_variable.get()))
            
          
            price = np.round(obj.american_option_pricing(),4)
            
            
            results_label = tk.Label(self, text = f'Option Price: {price}')
            results_label.grid(row=2, column = 3)
         
        

if __name__ == '__main__':
    
    app = SampleApp()   
    app.title('Derivatives Project')
#    app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(file='poli_ufrj.gif'))
    app.resizable(width=False, height=False)
    app.mainloop()
             

