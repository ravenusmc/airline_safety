### This file will contain all the code that will get the user request and
## process the data

import numpy as np
import pandas as pd

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/airline_data.csv')

    def graphOneData(self, airline, year):
        self.data = self.data.set_index("airline", drop = False)
        #This dictionary will hold the data
        singleDataPoint = {}
        #This gets me a single row of data.
        self.data = self.data.loc[airline, :]
        if year == '85-99':
            incidents = int(self.data[2]) # This gets me the incidents_85_99 column
            fatal = int(self.data[3]) #This gets me the fatal accidents column
            fatalities = int(self.data[4]) #This gets me the fatalities column
        else:
            incidents = int(self.data[5])
            fatal = int(self.data[6])
            fatalities = int(self.data[7])
        graphOneData = [{'name':'incidents', 'count':incidents}, {'name':'fatal', 'count':fatal}, {'name':'fatalities', 'count':fatalities}]
        return graphOneData



# data = Data()
# data.graphOneData()
