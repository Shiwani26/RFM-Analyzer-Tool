from Load_Data import df
import pandas as pd


df["Date"] = pd.to_datetime(df["Date"])
df = df.groupby("Customer_ID").agg({"Amount":"sum", "Date": "max", "Customer_ID" : "count"}).rename(columns={"Customer_ID":"Order_Number"}).reset_index()
print(df.head())