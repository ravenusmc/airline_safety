## This file will take care of support methods that I'll need to build
## this application.

import numpy as np
import pandas as pd

class Support():

    def __init__(self):
        self.data = pd.read_csv('./data/airline_data.csv')

    def test(self):
        print(self.data.head())
        
obj = Support()
obj.test()
