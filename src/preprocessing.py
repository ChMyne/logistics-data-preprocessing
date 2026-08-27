import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# -------------------------------
# 1. Load the logistics dataset
# -------------------------------
data = pd.read_csv("data/logistics_data.csv")

print("===== ORIGINAL DATASET =====")
print(data)

# -------------------------------
# 2. Check missing values
# -------------------------------
print("\n===== MISSING VALUES BEFORE CLEANING =====")
print(data.isnull().sum())

# -------------------------------
# 3. Handle missing values
# Replace missing numerical values with median
# -------------------------------
numerical_columns = [
    "delivery_time",
    "transportation_cost",
    "inventory_level"
]

for column in numerical_columns:
    data[column] = data[column].fillna(
        data[column].median()
    )

print("\n===== MISSING VALUES AFTER CLEANING =====")
print(data.isnull().sum())

# -------------------------------
# 4. Detect outliers using IQR
# -------------------------------
def detect_outliers(column):
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = data[
        (data[column] < lower_bound) |
        (data[column] > upper_bound)
    ]

    return outliers


print("\n===== OUTLIER DETECTION =====")

for column in numerical_columns:
    outliers = detect_outliers(column)

    print(f"\nOutliers in {column}:")
    print(outliers)

# -------------------------------
# 5. Normalize numerical data
# -------------------------------
scaler = MinMaxScaler()

data[numerical_columns] = scaler.fit_transform(
    data[numerical_columns]
)

print("\n===== NORMALIZED DATASET =====")
print(data)

# -------------------------------
# 6. Save the preprocessed dataset
# -------------------------------
data.to_csv(
    "data/preprocessed_logistics_data.csv",
    index=False
)

print("\nData preprocessing completed successfully!")
