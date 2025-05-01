
# Visual Representations

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Load_Data import df


# BarChart
plt.figure(figsize=(15, 10))
plt.bar(df["Customer_Category"], df["Order_Number"]) 
plt.title('RFM Value Segment Distribution')
plt.xlabel("Customer_Category")
plt.ylabel("Order_Number")
plt.tight_layout()
plt.show()

#heatmap

# Calculate correlation matrix for RFM scores
corr_matrix = df[['Recency', 'Frequency', 'Monetary']].corr()
# Generate the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,           # Data to plot
    annot=True,            # Show values in cells
    fmt=".2f",            # Format values (2 decimal places)
    cmap="RdBu",          # Using same colorscale as your original ('RdBu')
    linewidths=0.5,       # Add grid lines
    vmin=-1, vmax=1,      # Scale for correlation (-1 to 1)
    square=True           # Make cells square-shaped
)

plt.title('Correlation Matrix of RFM Values')
plt.tight_layout()
plt.show()

