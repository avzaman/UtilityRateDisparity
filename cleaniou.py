#need to read utilities csv
#need to cut eiaid,utility_name,service_type,ownership
#don't care who provider is or what type of owner, not relevant to study
#may be interesting to compare residential to commercial rates though
#need to merge all multiple occuring zipcodes by taking average of rates
import pandas as pd

# Read the CSV file
df = pd.read_csv('data/iou_zipcodes_2020.csv')

# Specify columns to include in the mean calculation
columns_to_mean = ['comm_rate', 'ind_rate', 'res_rate']

# Split dataframe into two dataframes: one for mean columns and one for non-mean columns
df_mean = df[['zip'] + columns_to_mean]
df_non_mean = df.drop(columns=columns_to_mean)

# Group by 'zip' and calculate the average of selected rate columns
df_grouped_mean = df_mean.groupby('zip').mean()

# Group by 'zip' and get the first value for non-mean columns (assuming all values within a group are the same)
df_grouped_non_mean = df_non_mean.groupby('zip').first()

# Reset index to include 'zip' as a column
df_grouped_mean.reset_index(inplace=True)
df_grouped_non_mean.reset_index(inplace=True)

# Drop unnecessary columns from df_grouped_non_mean
columns_to_drop = ['eiaid', 'utility_name', 'service_type', 'ownership']
df_grouped_non_mean.drop(columns=columns_to_drop, inplace=True)

# Concatenate the two dataframes while ensuring order is maintained
df_combined = pd.merge(df_grouped_non_mean, df_grouped_mean, on='zip')

# Save the edited dataframe to a new CSV file
df_combined.to_csv('data/clean_iou.csv', index=False)

#verified integrity of output by manually calulating some of the rate groups