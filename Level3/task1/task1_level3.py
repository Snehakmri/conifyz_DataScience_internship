'''
Task: Predictive Modeling
 Task 1
 Build a regression model to predict the
 aggregate rating of a restaurant based on
 available features.
 Split the dataset into training and testing sets
 and evaluate the model's performance using
 appropriate metrics.
 Experiment with different algorithms (e.g.,
 linear regression, decision trees, random
 forest) and compare their performance.

'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Load the dataset
data = pd.read_csv('Dataset.csv')

# Drop columns that are not useful for prediction
data_cleaned = data.drop(columns=['Restaurant ID', 'Restaurant Name', 'Country Code', 'City', 'Address',
                                  'Locality', 'Locality Verbose', 'Longitude', 'Latitude', 'Currency',
                                  'Rating color', 'Rating text'])

# Handle missing values
data_cleaned = data_cleaned.dropna()

# Convert categorical features to numerical using one-hot encoding
categorical_features = ['Cuisines', 'Has Table booking', 'Has Online delivery', 'Is delivering now', 'Switch to order menu']
data_encoded = pd.get_dummies(data_cleaned, columns=categorical_features)

# Separate features and target variable
X = data_encoded.drop(columns='Aggregate rating')
y = data_encoded['Aggregate rating']

# Standardize numerical features
scaler = StandardScaler()
numerical_features = ['Average Cost for two', 'Price range', 'Votes']
X[numerical_features] = scaler.fit_transform(X[numerical_features])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(random_state=42)
}

# Train and evaluate models
results = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    results[model_name] = {
        'MAE': mae,
        'RMSE': rmse,
        'R²': r2
    }

# Display the results
for model_name, metrics in results.items():
    print(f"Model: {model_name}")
    print(f"  MAE: {metrics['MAE']}")
    print(f"  RMSE: {metrics['RMSE']}")
    print(f"  R²: {metrics['R²']}")
    print()
