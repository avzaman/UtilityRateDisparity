import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Read CSV files
income_df = pd.read_csv('data/clean_income.csv')
iou_df = pd.read_csv('data/clean_iou.csv')

# Join dataframes on ZIP code
merged_df = pd.merge(income_df, iou_df, on='zip', how='inner')

# Ensure 'county' column from merged_df is string length 5
merged_df['county'] = merged_df['county'].astype(str).str[:5].str.zfill(5)

# Concatenate STATEFP and COUNTYFP columns to match the county column
shapefile = gpd.read_file('data/cb_2022_us_county_20m/cb_2022_us_county_20m.shp')
shapefile['county'] = shapefile['STATEFP'] + shapefile['COUNTYFP']

# Ensure 'county' column from shapefile is string length 5
shapefile['county'] = shapefile['county'].astype(str).str[:5].str.zfill(5)

# Convert join columns to strings
merged_df['county'] = merged_df['county'].astype(str)

# Group by county and calculate the mean of res_rate and median_income
grouped_df = merged_df.groupby('county').agg({'res_rate': 'mean', 'median_income': 'mean'}).reset_index()

# Merge with shapefile
merged_shapefile = shapefile.merge(grouped_df, on='county', how='inner')

# Plot res_rate
fig, ax = plt.subplots(1, 1, figsize=(20, 15), dpi=600)
merged_shapefile.plot(column='res_rate', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=False)
plt.title('Residential Electric Rate in USD/kwh by County')
plt.axis('off')

# Create color bar legend
cax = fig.add_axes([0.1, 0.05, 0.8, 0.02])  # [left, bottom, width, height]
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=merged_shapefile['res_rate'].min(), vmax=merged_shapefile['res_rate'].max()))
sm._A = []
cbar = fig.colorbar(sm, cax=cax, orientation='horizontal')
cbar.set_label('Residential Rate')

plt.savefig('res_rate_plot.jpg', dpi=600)

# Plot median_income
fig, ax = plt.subplots(1, 1, figsize=(20, 15), dpi=600)
merged_shapefile.plot(column='median_income', cmap='Greens', linewidth=0.8, ax=ax, edgecolor='0.8', legend=False)
plt.title('Median Income in USD by County')
plt.axis('off')

# Create color bar legend
cax = fig.add_axes([0.1, 0.05, 0.8, 0.02])  # [left, bottom, width, height]
sm = plt.cm.ScalarMappable(cmap='Greens', norm=plt.Normalize(vmin=merged_shapefile['median_income'].min(), vmax=merged_shapefile['median_income'].max()))
sm._A = []
cbar = fig.colorbar(sm, cax=cax, orientation='horizontal')
cbar.set_label('Median Income')

plt.savefig('median_income_plot.jpg', dpi=600)