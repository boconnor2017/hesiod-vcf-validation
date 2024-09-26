import pandas as pd

# Read Excel and select a single cell (and make it a header for a column)
filename = "vcf-papw-test2.xlsx"
data = pd.read_excel(filename, 'Deployment Options', index_col=None, usecols = "H", header = 10, nrows=11)
print(data.columns.values[0])