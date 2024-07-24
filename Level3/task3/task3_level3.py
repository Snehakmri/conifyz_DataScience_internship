'''
 Task 3
 Create visualizations to represent the distribution
 of ratings using different charts (histogram, bar
 plot, etc.).
 Compare the average ratings of different cuisines
 or cities using appropriate visualizations.
 Visualize the relationship between various
 features and the target variable to gain insights.
 '''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('Dataset.csv')

# Display the first few rows and column names
print(data.head())
print(data.columns)

# Drop columns that are not useful for this analysis
data_cleaned = data.drop(columns=['Restaurant ID', 'Restaurant Name', 'Country Code', 'Address',
                                  'Locality', 'Locality Verbose', 'Longitude', 'Latitude', 'Currency',
                                  'Rating color', 'Rating text', 'Has Table booking', 'Has Online delivery', 'Is delivering now', 'Switch to order menu'])

# Handle missing values
data_cleaned = data_cleaned.dropna()

# Split 'Cuisines' into separate rows for each cuisine type
data_cleaned['Cuisines'] = data_cleaned['Cuisines'].str.split(', ')
data_exploded = data_cleaned.explode('Cuisines')

# Step 2: Distribution of Ratings
plt.figure(figsize=(10, 6))
sns.histplot(data['Aggregate rating'], bins=20, kde=True)
plt.title('Distribution of Restaurant Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Step 3: Compare Average Ratings of Different Cuisines
cuisine_ratings = data_exploded.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
cuisine_ratings.head(20).plot(kind='bar')
plt.title('Top 20 Cuisines by Average Rating')
plt.xlabel('Cuisine')
plt.ylabel('Average Rating')
plt.xticks(rotation=90)
plt.show()

# Step 4: Compare Average Ratings of Different Cities
city_ratings = data.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
city_ratings.head(20).plot(kind='bar')
plt.title('Top 20 Cities by Average Rating')
plt.xlabel('City')
plt.ylabel('Average Rating')
plt.xticks(rotation=90)
plt.show()

# Step 5: Visualize Relationship Between Various Features and Ratings

# Scatter plot for Average Cost for two vs. Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Average Cost for two', y='Aggregate rating', data=data)
plt.title('Average Cost for Two vs. Rating')
plt.xlabel('Average Cost for Two')
plt.ylabel('Rating')
plt.show()

# Scatter plot for Votes vs. Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Votes', y='Aggregate rating', data=data)
plt.title('Votes vs. Rating')
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.show()

# Scatter plot for Price Range vs. Rating
plt.figure(figsize=(10, 6))
sns.boxplot(x='Price range', y='Aggregate rating', data=data)
plt.title('Price Range vs. Rating')
plt.xlabel('Price Range')
plt.ylabel('Rating')
plt.show()


