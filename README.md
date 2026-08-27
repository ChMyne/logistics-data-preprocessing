# Logistics Data Preprocessing

## Project Overview

This project demonstrates the process of data collection, cleaning, and preprocessing in the context of logistics data using Python. The objective is to prepare a raw logistics dataset for further analysis by identifying missing values, detecting potential outliers, and normalizing numerical data.

## Objectives

- Load and examine a logistics dataset.
- Identify missing values in the dataset.
- Handle missing numerical values using the median.
- Detect potential outliers using the Interquartile Range (IQR) method.
- Normalize numerical features using Min-Max Scaling.
- Prepare a cleaned dataset for further analysis.

## Dataset Description

The dataset contains logistics and delivery-related information.

| Column | Description |
|---|---|
| shipment_id | Unique identifier for each shipment |
| warehouse | Warehouse location |
| delivery_time | Number of days required for delivery |
| transportation_cost | Transportation cost for the shipment |
| inventory_level | Available inventory level |
| order_status | Delivery status of the order |

The dataset intentionally contains some missing values to demonstrate data cleaning techniques.

## Data Cleaning

The following numerical columns are checked for missing values:

- delivery_time
- transportation_cost
- inventory_level

Missing values are replaced using the median of the respective column. The median is useful because it is less affected by extreme values compared to the mean.

## Outlier Detection

Potential outliers are detected using the Interquartile Range (IQR) method.

The lower and upper bounds are calculated as:

```text
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
Values outside these bounds are identified as potential outliers.

Data Normalization

Min-Max Scaling is applied to the numerical columns:

delivery_time
transportation_cost
inventory_level

The values are transformed to a range between 0 and 1 using:

X_normalized = (X - X_min) / (X_max - X_min)
Technologies Used
Python
Pandas
NumPy
Scikit-learn
Project Structure
logistics-data-preprocessing/
│
├── data/
│   └── logistics_data.csv
│
├── src/
│   └── preprocessing.py
│
├── README.md
└── requirements.txt
How to Run

Install the required libraries:

pip install -r requirements.txt

Run the preprocessing script:

python src/preprocessing.py
Expected Outcome

The project demonstrates a complete basic data preprocessing workflow. Missing values are handled, potential outliers are identified, and numerical features are normalized. The processed dataset is saved as:

data/preprocessed_logistics_data.csv
Conclusion

High-quality data is essential for reliable analytics and decision-making in logistics. Proper data cleaning and preprocessing help reduce errors, improve consistency, and prepare datasets for future analysis and predictive modeling.
