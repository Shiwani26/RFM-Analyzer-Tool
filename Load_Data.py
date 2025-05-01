import pandas as pd
import numpy as np
import datetime



df = pd.read_excel("CUSID_Amts.xlsx") # loading the dataset

df["Date"] = pd.to_datetime(df["Date"])
df = df.groupby("Customer_ID").agg({"Amount":"sum", "Date": "max", "Customer_ID" : "count"}).rename(columns={"Customer_ID":"Order_Number"}).reset_index()  # Data processin


print(df.head())


