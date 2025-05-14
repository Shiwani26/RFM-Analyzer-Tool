import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns


def simple_rfm_analysis(filepath="CUSID_Amts.xlsx"):
    """
        filepath (str): Path to Excel file containing transaction data
    """
    # Load and preprocess data
    df = pd.read_excel(filepath)
    df["Date"] = pd.to_datetime(df["Date"])
    
    # Aggregate by customer
    df = df.groupby("Customer_ID").agg({
        "Amount": "sum",
        "Date": "max",
        "Customer_ID": "count"
    }).rename(columns={"Customer_ID": "Order_Number"}).reset_index()

    # Calculate RFM metrics
    df["R"] = (pd.Timestamp.now() - df["Date"]).dt.days  # Recency
    df["F"] = df["Order_Number"]  # Frequency
    df["M"] = df["Amount"]  # Monetary

    # Scoring function (reused for R/F/M)
    def calculate_score(series, ascending=False):
        percentiles = series.quantile([0.2, 0.4, 0.6, 0.8], interpolation='higher')
        def get_score(x):
            if x > percentiles[0.8]: return 5
            elif x > percentiles[0.6]: return 4
            elif x > percentiles[0.4]: return 3
            elif x > percentiles[0.2]: return 2
            else: return 1
        return series.apply(get_score)

    # Apply scoring
    df['Recency'] = calculate_score(df["R"], ascending=True)
    df['Frequency'] = calculate_score(df["F"])
    df['Monetary'] = calculate_score(df["M"])

    # Combine scores and categorize
    df['RFM_Score'] = df['Recency'].astype(str) + df['Frequency'].astype(str) + df['Monetary'].astype(str)
    
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
        return "Unclassified"
    
    df['Customer_Category'] = df.apply(categorize_customers, axis=1)

    # Generate visualizations
    plt.figure(figsize=(15, 10))
    plt.bar(df["Customer_Category"], df["Order_Number"]) 
    plt.title('RFM Value Segment Distribution')
    plt.xlabel("Customer Category")
    plt.ylabel("Order Count")
    plt.tight_layout()
    plt.savefig("RFM_Value.png")
    plt.close()
    
    plt.figure()
    sns.boxplot(data=df[['Recency', 'Frequency', 'Monetary']])
    plt.title('Distribution of RFM Scores')
    plt.ylabel('Score')
    plt.savefig("Distribution.png")
    plt.close()

    return df

# Example usage:
# results = simple_rfm_analysis("your_data.xlsx")
# print(results.head())