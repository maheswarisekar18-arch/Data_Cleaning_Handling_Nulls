import pandas as pd
import numpy as np

data = {
    'patient_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 101, 107, 118, 119, 120],
    'age': ['25', '34', None, '45', '29', None, '38', '52', '27', '41',
            '33', 'unknown', '48', '26', '35', '25', '38', '31', None, '44'],
    'weight': ['70', '65', '80', None, '75', None, '68', '90', '72', '85',
               '78', None, '82', '69', 'N/A', '70', '68', '74', None, '88'],
    'blood_pressure': [120, 130, None, 140, 125, None, 135, None, 118, 145,
                      128, None, 138, 122, None, 120, 135, 126, None, 142],
    'medication': ['Aspirin', 'Metformin', 'Lisinopril', None, 'Aspirin',
                   'Metformin', 'Lisinopril', 'Aspirin', None, 'Metformin',
                   'Lisinopril', 'Aspirin', None, 'Metformin', 'Aspirin',
                   'Aspirin', 'Lisinopril', 'Metformin', 'Aspirin', None],
    'insurance_provider': ['Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None,
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', 'Blue Cross',
                          'Aetna', None, 'UnitedHealth', 'Blue Cross', 'Aetna',
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None]
}

df = pd.DataFrame(data)
df_cleaned = df.copy() # Create a copy of the original DataFrame to work on
print("Original DataFrame:\n", df) # Display the original DataFrame with missing values and duplicates
print("***********************Task 1: Inspect the data **********************")
print("\nDataFrame Info:\n", df.info())
print("\n missing values in each column:\n", df.isnull().sum())
print("\n missing value percentages in each column:\n", df.isnull().sum() / len(df) * 100)
print("\n count of Duplicate rows in the DataFrame:\n", df.duplicated().sum())
print("***********************Task 2: Data Type Conversion**********************")
print("age column to numeric values, coercing errors to NaN:\n", pd.to_numeric(df_cleaned['age'], errors='coerce'))
print("\n weight column to numeric values, coercing errors to NaN:\n", pd.to_numeric(df_cleaned['weight'], errors='coerce'))
print("\n new missing value after conversion in age column:\n", pd.to_numeric(df_cleaned['age'], errors='coerce').isnull().sum())
#Convert insurance_provider to category type using astype('category')
df_cleaned['insurance_provider'] = df_cleaned['insurance_provider'].astype('category')
print("\n insurance_provider column converted to category type:\n", df_cleaned['insurance_provider'].dtype)
print("\n Data types of all columns after conversion:\n", df_cleaned.dtypes)
print("**********************Task 3: Handle Missing Values**********************")
df_cleaned['age'] = pd.to_numeric(df_cleaned['age'], errors='coerce') # Convert age to numeric, coercing errors to NaN
df_cleaned['weight'] = pd.to_numeric(df_cleaned['weight'], errors='coerce') # Convert weight to numeric, coercing errors to NaN
df_cleaned['blood_pressure'] = pd.to_numeric(df_cleaned['blood_pressure'], errors='coerce') # Convert blood_pressure to numeric, coercing errors to NaN
df_cleaned['medication'] = df_cleaned['medication'].fillna(df_cleaned['medication'].mode()[0]) # Fill missing values in medication column with mode
#df_cleaned['insurance_provider'] = df_cleaned['insurance_provider'].fillna("Unknown") # Fill missing values in insurance_provider column with "Unknown"
print("\n missing values after filling:\n", df_cleaned.isnull().sum())
print("**********************Task 4: Handle Duplicates**********************")
print("\n duplicate rows in the DataFrame:\n", df_cleaned[df_cleaned.duplicated(keep=False)]) # Display duplicate rows in the original DataFrame
df_cleaned=df_cleaned[df_cleaned.duplicated(subset=['patient_id'])]
df_cleaned = df_cleaned.drop_duplicates(subset=['patient_id'], keep='first') # Remove duplicate rows based on patient_id, keeping the first occurrence
print("\n shape before removing duplicates: \n", df.shape)
print("\n shape after removing duplicates: \n", df_cleaned.shape)

print("***************Task 5: Complete Workflow with Verification**********************")

print("\n shape before removing duplicates: \n", df.shape)
print("\n shape after removing duplicates: \n", df_cleaned.shape)
print("\n missing values after filling:\n", df_cleaned.isnull().sum())
print("\n missing value before filling:\n", df.isnull().sum())
print("\n duplicate rows before removing duplicates:\n", df[df.duplicated(keep=False)])
print("\n duplicate rows after removing duplicates:\n", df_cleaned[df_cleaned.duplicated(keep=False)])
print("\n data types of all columns after conversion:\n", df_cleaned.dtypes)
print("\n data types of all columns before conversion:\n", df.dtypes)


