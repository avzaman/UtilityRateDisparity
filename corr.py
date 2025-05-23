#This script is going to be used to find various statistical calculations

#starting with correlation between res_rate and median income

import pandas as pd
iou_df = pd.read_csv("data/clean_iou.csv")
income_df = pd.read_csv("data/clean_income.csv")
merged_df = pd.merge(iou_df, income_df, on='zip', how='inner')
correlation = merged_df['res_rate'].corr(merged_df['median_income'])

print("Correlation between res_rate and median_income in whole US:", correlation)

# Calculate correlations by state
correlations_by_state = merged_df.groupby('state')[['res_rate', 'median_income']].corr().iloc[0::2,-1]

# Drop NaN values, small states with few zips have too few points to run corr on
correlations_by_state.dropna(inplace=True)

# Sort correlations by absolute value in descending order
sorted_correlations = correlations_by_state.abs().sort_values(ascending=False)

# Display the top 5 highest correlated and top 5 lowest correlated states
top_5_highest_corr = sorted_correlations.head(5)
top_5_lowest_corr = sorted_correlations.tail(5)

print("Top 5 highest correlated states:")
print(top_5_highest_corr)
print("\nTop 5 lowest correlated states:")
print(top_5_lowest_corr)