'''
Task 2
 Task: Customer Preference Analysis
 Analyze the relationship between the type of
 cuisine and the restaurant's rating.
 Identify the most popular cuisines among
 customers based on the number of votes.
 Determine if there are any specific cuisines
 that tend to receive higher ratings.

'''
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Dataset.csv')

# Display the first few rows and column names
print(data.head())
print(data.columns)

# Drop columns that are not useful for this analysis
data_cleaned = data.drop(columns=['Restaurant ID', 'Restaurant Name', 'Country Code', 'City', 'Address',
                                  'Locality', 'Locality Verbose', 'Longitude', 'Latitude', 'Currency',
                                  'Rating color', 'Rating text', 'Has Table booking', 'Has Online delivery', 'Is delivering now', 'Switch to order menu'])

# Handle missing values
data_cleaned = data_cleaned.dropna()

# Split 'Cuisines' into separate rows for each cuisine type
data_cleaned['Cuisines'] = data_cleaned['Cuisines'].str.split(', ')
data_exploded = data_cleaned.explode('Cuisines')

# Group by 'Cuisines' and calculate the average rating
cuisine_ratings = data_exploded.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)

# Plot the average ratings for different cuisines
plt.figure(figsize=(12, 8))
cuisine_ratings.plot(kind='bar')
plt.title('Average Rating by Cuisine Type')
plt.xlabel('Cuisine')
plt.ylabel('Average Rating')
plt.xticks(rotation=90)
plt.show()

# Group by 'Cuisines' and sum the votes
cuisine_votes = data_exploded.groupby('Cuisines')['Votes'].sum().sort_values(ascending=False)

# Plot the top cuisines based on votes
plt.figure(figsize=(12, 8))
cuisine_votes.head(20).plot(kind='bar')
plt.title('Top 20 Most Popular Cuisines Based on Votes')
plt.xlabel('Cuisine')
plt.ylabel('Total Votes')
plt.xticks(rotation=90)
plt.show()

#-------------------------------------------------------------
cuisine_ratings = data_exploded.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)


# Plot the average ratings for different cuisines
plt.figure(figsize=(12, 8))
cuisine_ratings.plot(kind='bar')
plt.title('Average Rating by Cuisine Type')
plt.xlabel('Cuisine')
plt.ylabel('Average Rating')
plt.xticks(rotation=90)
plt.show()

# Display cuisines with the highest average ratings
cuisine_ratings.head(20)

