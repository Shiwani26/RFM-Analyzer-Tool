
import pandas as pd 
import datetime
from Load_Data import df

df["R"] = (pd.Timestamp.now() - pd.to_datetime(df["Date"])).dt.days
print(df.head())