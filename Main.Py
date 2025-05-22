import sys
from RFM_Module import simple_rfm_analysis


# Check if file path is provided via command line
if len(sys.argv) < 2:
    sys.exit()

# Get the file path
file_path = sys.argv[1]

# Run the RFM analysis
result_df = simple_rfm_analysis(file_path)

# Show first few rows
print(result_df.head())