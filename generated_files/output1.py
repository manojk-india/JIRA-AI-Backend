import pandas as pd
df = pd.read_csv("generated_files/new_custom.csv")

# Filter the DataFrame for issues in the CDF board
cdf_issues = df[df['board'] == 'CDF']

# Save the filtered DataFrame to output.csv
cdf_issues.to_csv('generated_files/output.csv', index=False)
