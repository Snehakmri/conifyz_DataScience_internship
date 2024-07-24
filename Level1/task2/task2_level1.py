'''
Task 2
 Task:  Descriptive Analysis
 Calculate basic statistical measures (mean,
 median, standard deviation, etc.) for numerical
 columns.
 Explore the distribution of categorical
 variables like "Country Code," "City," and
 "Cuisines."
 Identify the top cuisines and cities with the
 highest number of restaurants.
 '''

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file

df = pd.read_csv("Dataset.csv")

#Calculate basic statistical measures (mean,median, standard deviation, etc.) for numerical columns.

# Select the numerical columns
numerical_columns = ['Longitude', 'Latitude', 'Price range', 'Aggregate rating', 'Votes']

# Calculate mean, median, and standard deviation
means = df[numerical_columns].mean()
medians = df[numerical_columns].median()
std_devs = df[numerical_columns].std()

# Combine the results into a single DataFrame
statistics = pd.DataFrame({
    'mean': means,
    'median': medians,
    'std_dev': std_devs
})

print(statistics)

# Explore the distribution of categorical variables like "Country Code," "City," and "Cuisines."

# Function to plot the distribution of a categorical variable
def plot_category_distribution(column_name):
    plt.figure(figsize=(12, 6))
    df[column_name].value_counts().head(20).plot(kind='bar')
    plt.title(f'Distribution of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.show()

# Plot distributions
plot_category_distribution('Country Code')
plot_category_distribution('City')
plot_category_distribution('Cuisines')


# Identify the top cuisines and cities with the highest number of restaurants

# Get the top 10 cuisines
top_cuisines = df['Cuisines'].value_counts().head(10)
print("Top 10 Cuisines:\n", top_cuisines)

# Get the top 10 cities
top_cities = df['City'].value_counts().head(10)
print("\nTop 10 Cities:\n", top_cities)