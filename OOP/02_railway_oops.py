# pandas is not needed, its just for test...
import pandas as pd
pd.DataFrame()

class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysApplication = RailwayForm()
harrysApplication.name = "Harry"
harrysApplication.train = "Rajdhani Express"
harrysApplication.printData()

'''
>>>pip install pandas
Note -> Successfully installed numpy-1.24.1 pandas-1.5.3 python-dateutil-2.8.2 pytz-2022.7.1 six-1.16.0
'''