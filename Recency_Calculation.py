import pandas as pd 
from Recency_Calculation import df

df["R"] = (pd.Timestamp.now() - pd.to_datetime(df["Date"])).dt.days
print(df.head())