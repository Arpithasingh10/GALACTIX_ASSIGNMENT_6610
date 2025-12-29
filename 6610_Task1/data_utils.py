import pandas as pd
import numpy as np

# 1. Detect missing values
def detect_missing_values(df):
    """
    Returns count of missing values per column
    """
    return df.isnull().sum()


# 2. Detect duplicate rows
def detect_duplicates(df):
    """
    Returns number of duplicate rows
    """
    return df.duplicated().sum()


# 3. Detect outliers using IQR method
def detect_outliers(df):
    """
    Detects outliers for all numeric columns using IQR
    """
    outliers = {}
    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        count = df[(df[col] < lower_bound) | (df[col] > upper_bound)].shape[0]
        outliers[col] = count

    return outliers


# 4. Normalize numeric columns (Min-Max Scaling)
def normalize_numeric_columns(df):
    """
    Normalizes numeric columns using Min-Max normalization
    """
    df_normalized = df.copy()
    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        min_val = df[col].min()
        max_val = df[col].max()

        if max_val != min_val:
            df_normalized[col] = (df[col] - min_val) / (max_val - min_val)

    return df_normalized


# 5. Remove duplicates using custom rule
def remove_duplicates_custom(df):
    """
    Removes duplicates based on first two columns
    (generic rule, no hardcoding)
    """
    if df.shape[1] >= 2:
        return df.drop_duplicates(subset=df.columns[:2])
    return df


