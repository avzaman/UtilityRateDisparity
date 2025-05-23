import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Read clean_iou.csv
iou_df = pd.read_csv("data/clean_iou.csv")

# Standardize the 'res_rate' column
scaler = StandardScaler()
iou_df['res_rate_standardized'] = scaler.fit_transform(iou_df[['res_rate']])

# Read clean_income.csv
income_df = pd.read_csv("data/clean_income.csv")

# Standardize the 'median_income' column
income_df['median_income_standardized'] = scaler.fit_transform(income_df[['median_income']])

# Create a single histogram for both standardized distributions
plt.figure(figsize=(10, 6))
plt.hist(iou_df['res_rate_standardized'], bins='auto', color='red', alpha=0.5, label='Residential Rates (Standardized)', edgecolor='black')
plt.hist(income_df['median_income_standardized'], bins='auto', color='lightgreen', alpha=0.5, label='Median Income (Standardized)', edgecolor='black')
plt.title('Histogram of Standardized Residential Rates and Median Income')
plt.xlabel('Standardized Values')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.savefig('plots/standardized_histogram.jpeg')
plt.close()

print("Histogram of standardized distributions saved as JPEG file.")
