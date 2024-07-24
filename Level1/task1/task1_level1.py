'''
Level 1:  Data Exploration and Preprocessing
 Task 1:
 Explore the dataset and identify the number
 of rows and columns.
 Check for missing values in each column and
 handle them accordingly.
 Perform data type conversion if necessary.
 Analyze the distribution of the target variable
 ("Aggregate rating") and identify any class
 imbalances

 '''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Explore the dataset and identify the number of rows and columns
df = pd.read_csv("Dataset.csv")
print(type(df))

num_rows, num_cols = df.shape


rows = df.shape[0]  
cols = df.shape[1] 

print("No of rows: ", rows)  
print("No of columns: ", cols)  


df.columns = df.columns.str.replace(' ', '_')

#Check for missing values in each column and handle them accordingly

#missing_values = df.isnull().sum()
#print('Missing values per column:')

missing_values = df.isnull()
print(missing_values)

#handling

# Handle missing values
# Option 1: Drop rows with any missing values
df.dropna(inplace=True)

# Option 2: Fill missing values with mean (for numeric column 'Age')
df['Votes'].fillna(df['Votes'].mean(), inplace=False)

# Option 3: Fill missing values with a specific value (for 'Location')
df['City'].fillna('Unknown', inplace=False)

# Display the cleaned DataFrame
print('\nCleaned DataFrame:')
print(df)


# Perform data type conversion

print("df.dtypes")
print(df.dtypes)

#Convert Restaurant_ID to string 
df['Restaurant_ID'] = df['Restaurant_ID'].astype('string')

print("\n df.Restaurant_ID.dtypes ")
print(df.Restaurant_ID.dtypes)


#Perform data type conversion if necessary.Analyze the distribution of the target variable("Aggregate rating") and identify any class imbalances

# Analyze the distribution of the target variable
target_distribution = df['Aggregate_rating'].value_counts()
print("Target Distribution:(Aggregate rating):\n", target_distribution)

# Plot the distribution of the target variable
plt.figure(figsize=(8, 6))
sns.countplot(x='Aggregate_rating', data=df)
plt.title('Distribution of Target Variable')
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.show()

#-----------------------------------------------------------------------------------------------------------------
# Identify class imbalance
''''
# Automatically create 3 quantile bins
df['target_bin_qcut'] = pd.qcut(df['Aggregate_rating'], q=3, labels=['Low', 'Medium', 'High'])

total = len(df)
target_distribution_qcut = df['target_bin_qcut'].value_counts()
print("Target Distribution (pd.qcut()):\n", target_distribution_qcut)

# Plot the distribution of the discretized target variable using pd.qcut()
plt.figure(figsize=(8, 6))
sns.countplot(x='target_bin_qcut', data=df)
plt.title('Distribution of Discretized Target Variable (pd.qcut())')
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.show()


# Identify class imbalance for pd.qcut()
for label in target_distribution_qcut.index:
    count = target_distribution_qcut[label]
    print(f"Class {label} (pd.qcut()): {count} ({(count / total) * 100:.2f}%)")

'''

df['target_bin_cut'] = pd.cut(df['Aggregate_rating'], bins=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

# Using pd.qcut() for equal-sized bins
df['target_bin_qcut'] = pd.qcut(df['Aggregate_rating'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

# Analyze the distribution of the discretized target variable using pd.cut()
target_distribution_cut = df['target_bin_cut'].value_counts().sort_index()
print("Target Distribution (pd.cut()):\n", target_distribution_cut)

# Plot the distribution of the discretized target variable using pd.cut()
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.countplot(x='target_bin_cut', data=df)
plt.title('Distribution of Target Variable (pd.cut())')
plt.xlabel('Bin')
plt.ylabel('Frequency')
plt.show()

