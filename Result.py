
# Visual Representations

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Scorer import df


# BarChart
plt.figure(figsize=(15, 10))
plt.bar(df["Customer_Category"], df["Order_Number"]) 
plt.title('RFM Value Segment Distribution')
plt.xlabel("Customer_Category")
plt.ylabel("Order_Number")
plt.tight_layout()
plt.savefig("RFM_Value.png")

plt.figure() # starting new figure

#Distribution plot for R,F,& M

plot = sns.boxplot(data=df[['Recency', 'Frequency', 'Monetary']])
plot.set_title('Distribution of RFM Scores')
plot.set_ylabel('Score')
plt.savefig("Distribution.png")

