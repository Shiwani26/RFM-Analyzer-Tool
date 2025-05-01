import pandas as pd 
import datetime
from Load_Data import df

df["R"] = (pd.Timestamp.now() - pd.to_datetime(df["Date"])).dt.days  # calculating the Recency

def calculate_score(df, column_name="R"):
    # Calculate percentiles (using PERCENTILE.EXC equivalent)
    percentiles = df[column_name].quantile([0.2, 0.4, 0.6, 0.8], interpolation='higher')
    
    def get_score(x):
        if x > percentiles[0.8]: return 5
        elif x > percentiles[0.6]: return 4
        elif x > percentiles[0.4]: return 3
        elif x > percentiles[0.2]: return 2
        else: return 1
    
    return df[column_name].apply(get_score)

df['Recency'] = calculate_score(df, "R")
df['Recency']

# calculating the Frequency (F): Represents how often a customer has made purchases.
df["F"] = df["Order_Number"]

# Calculating percentile for Frequency
def calculate_score(df, column_name="F"):
    # Calculate percentiles (using PERCENTILE.EXC equivalent)
    percentiles = df[column_name].quantile([0.2, 0.4, 0.6, 0.8], interpolation='higher')
    
    def get_score(x):
        if x > percentiles[0.8]: return 5
        elif x > percentiles[0.6]: return 4
        elif x > percentiles[0.4]: return 3
        elif x > percentiles[0.2]: return 2
        else: return 1
    
    return df[column_name].apply(get_score)


df['Frequency'] = calculate_score(df, "F")
df['Frequency']

# calculating Monetary ((the amount spent on purchases))
df["M"] = df["Amount"]

# calculating the percentile for Monetary
def calculate_score(df, column_name="M"):
    # Calculate percentiles (using PERCENTILE.EXC equivalent)
    percentiles = df[column_name].quantile([0.2, 0.4, 0.6, 0.8], interpolation='higher')
    
    def get_score(x):
        if x > percentiles[0.8]: return 5
        elif x > percentiles[0.6]: return 4
        elif x > percentiles[0.4]: return 3
        elif x > percentiles[0.2]: return 2
        else: return 1
    
    return df[column_name].apply(get_score)


df['Monetary'] = calculate_score(df, "M")
df['Monetary']

# Assuming your DataFrame is called df and has columns 'Recency', 'Frequency', and 'Monetary'
df['RFM_Score'] = df['Recency'].astype(str) + df['Frequency'].astype(str) + df['Monetary'].astype(str)
df["RFM_Score"]

#Classification of RFM Scores

def categorize_customers(row):
    if row['Recency'] == 5 and row['Frequency'] >= 4 and row['Monetary'] >= 4:
        return "Best Customers"
    elif 3 <= row['Recency'] <= 4 and row['Frequency'] >= 4 and row['Monetary'] >= 3:
        return "Loyal Customers"
    elif 3 <= row['Recency'] <= 4 and row['Frequency'] >= 2 and row['Monetary'] >= 2:
        return "Potential Loyal Customers"
    elif 2 <= row['Recency'] <= 3 and row['Frequency'] >= 3 and row['Monetary'] >= 3:
        return "At-Risk Customers"
    elif row['Recency'] == 1 and row['Frequency'] <= 2 and row['Monetary'] <= 2:
        return "Lost Customers"
    else:
        return "Unclassified"

# Usage:
df['Customer_Category'] = df.apply(categorize_customers, axis= 1)

# Counting the values
df["Customer_Category"].value_counts()
df["Customer_Category"]


