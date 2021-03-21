import pandas as pd
import numpy as np
import os

os.chdir(r"C:\Users\pc\Desktop\stock\Modeling\Basic")
raw1 = pd.read_csv("S&P 500 Historical Data.csv")
raw2 = pd.read_csv("S&P500.csv")

df1 =pd.DataFrame(data=raw1, columns=['Date','Price','Open','High','Low','Vol.','Change %']).set_index('Date')
df2 =pd.DataFrame(data=raw2, columns=['Date','Price','Open','High','Low','Vol.','Change %']).set_index('Date')

total = pd.concat([df1,df2])
total.to_csv("total_S&P500.csv")
