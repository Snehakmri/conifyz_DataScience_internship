'''Task:  Geospatial Analysis
 Task 3
 Visualize the locations of restaurants on a
 map using latitude and longitude
 information.
 Analyze the distribution of restaurants
 across different cities or countries.
 Determine if there is any correlation
 between the restaurant's location and its
 rating.
'''


#Visualize the locations of restaurants on a map using latitude and longitude information.

import geopandas as gpd
import geoplot as gplt
import matplotlib.pyplot as plt
from shapely.geometry import Point
import pandas as pd


data = pd.read_csv("Dataset.csv")

# Create a GeoDataFrame from the dataset
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['Longitude'], data['Latitude']))

# Set the coordinate reference system to WGS84
gdf.set_crs(epsg=4326, inplace=True)

# Plot the restaurant locations
fig, ax = plt.subplots(figsize=(10, 10))
gplt.pointplot(gdf, ax=ax, hue='Rating color', legend=True)

plt.title('Restaurant Locations')
plt.show()

#Analyze the distribution of restaurants across different cities or countries. Determine if there is any correlation between the restaurant's location and its rating.


# Analyze the distribution of restaurants across different cities
city_distribution = data['City'].value_counts()

# Analyze the distribution of restaurants across different countries
country_distribution = data['Country Code'].value_counts()

# Display the results
print("Distribution of restaurants across different cities:")
print(city_distribution.head())

print("\nDistribution of restaurants across different countries:")
print(country_distribution.head())

#Determine if there is any correlation between the restaurant's location and its rating.
# Select relevant columns
relevant_data = data[['Latitude', 'Longitude', 'Aggregate rating']]

# Calculate correlation matrix
correlation_matrix = relevant_data.corr()

# Display the correlation matrix
print("Correlation matrix between restaurant's location and its rating:")
print(correlation_matrix)
