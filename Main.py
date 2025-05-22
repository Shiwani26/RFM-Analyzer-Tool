import sys
import os
from RFM_Module import simple_rfm_analysis

# Check if file path is provided via command line
if len(sys.argv) < 2:
    print("Usage: python your_script.py <input_file>")
    sys.exit()

# Get the file path
file_path = sys.argv[1]

# Run the RFM analysis
result_df = simple_rfm_analysis(file_path)

# Save the result to an Excel file
output_path = "rfm_output.xlsx"
print("Saving output to:", os.path.abspath(output_path))
result_df.to_excel(output_path, index=False)

# Print first few rows
print(result_df.head())
