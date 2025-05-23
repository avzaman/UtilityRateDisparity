import pandas as pd
import matplotlib.pyplot as plt

# Read clean_iou.csv
iou_df = pd.read_csv("data/clean_iou.csv")

# Read clean_income.csv
income_df = pd.read_csv("data/clean_income.csv")

# Merge the dataframes on 'zip'
merged_df = pd.merge(iou_df, income_df, on='zip', how='inner')

scaling_factor = 100

# Define colormap
cmap = plt.cm.get_cmap('coolwarm')

# Scatterplot 1: Zip code vs. Median Income vs. Res Rate
plt.figure(figsize=(10, 6))
plt.scatter(merged_df['zip'], merged_df['median_income'], s=merged_df['res_rate'] * scaling_factor, c=merged_df['res_rate'], cmap=cmap, alpha=0.5)
plt.title('Zip Code vs. Median Income vs. Res Rate')
plt.xlabel('Zip Code')
plt.ylabel('Median Income')
plt.colorbar(label='Res Rate')
plt.grid(True)
# Invert the x-axis
plt.gca().invert_xaxis()
plt.savefig('plots/scatterplot_zip_income_res_rate.jpeg')
plt.close()

# Scatterplot 2: Income under 20 Pop vs. Median Income vs. Res Rate
plt.figure(figsize=(10, 6))
plt.scatter(merged_df['income_under_20_pop'], merged_df['median_income'], s=merged_df['res_rate'] * scaling_factor, c=merged_df['res_rate'], cmap=cmap, alpha=0.5)
plt.title('Income Under 20 Pop vs. Median Income vs. Res Rate')
plt.xlabel('Income Under 20 Pop')
plt.ylabel('Median Income')
plt.colorbar(label='Res Rate')
plt.grid(True)
plt.savefig('plots/scatterplot_income_under_20_pop_income_res_rate.jpeg')
plt.close()

# Scatterplot 3: Income over 20 Pop vs. Median Income vs. Res Rate
plt.figure(figsize=(10, 6))
plt.scatter(merged_df['income_over_20_pop'], merged_df['median_income'], s=merged_df['res_rate'] * scaling_factor, c=merged_df['res_rate'], cmap=cmap, alpha=0.5)
plt.title('Income Over 20 Pop vs. Median Income vs. Res Rate')
plt.xlabel('Income Over 20 Pop')
plt.ylabel('Median Income')
plt.colorbar(label='Res Rate')
plt.grid(True)
plt.savefig('plots/scatterplot_income_over_20_pop_income_res_rate.jpeg')
plt.close()

print("Scatterplots saved as JPEG files.")