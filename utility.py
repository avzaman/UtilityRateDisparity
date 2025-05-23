import geopandas as gpd

# Load the shapefile
shapefile_path = "data/cb_2020_us_county_20m/cb_2020_us_county_20m.shp"
gdf = gpd.read_file(shapefile_path)

# Display the columns

# Specify the column for which you want to print unique values and counts
column_name = "STATEFP"

# Get unique values and their counts
unique_counts = gdf[column_name].value_counts()

# Print unique values and their counts
print("Unique values and their counts in column '{}':".format(column_name))
for value, count in unique_counts.items():
    print(f"{value}: {count}")