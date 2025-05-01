
# Visual Representations

import pandas as pd
import matplotlib.pyplot as plt
from Load_Data import df


plt.figure(figsize=(15, 10))
plt.bar(df["Customer_Category"], df["Order_Number"]) 
plt.title('RFM Value Segment Distribution')
plt.xlabel("Customer_Category")
plt.ylabel("Order_Number")
plt.tight_layout()
plt.show()

