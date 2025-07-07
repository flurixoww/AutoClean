import numpy as np
import pandas as pd


def missing_values_imputer(df: pd.DataFrame, strategy: str='median', fill_non_numeric = False) -> pd.DataFrame:
    """Imputes missing values in a pandas DataFrame.

    This function fills missing values in a DataFrame using specified strategies
    for numeric and non-numeric columns. It creates a copy of the original
    DataFrame to avoid modifying it in place.

    Args:
        df: The input pandas DataFrame.
        strategy: The imputation strategy for numeric columns.
            Can be 'median' or 'mean'. Defaults to 'median'.
        fill_non_numeric: The value to use for filling missing values in
            non-numeric columns. If set to True, it fills with 'Unknown'.
            Defaults to None.

    Returns:
        A new DataFrame with missing values imputed.

    Raises:
        ValueError: If an invalid strategy is provided.
    """
    df_copy = df.copy()
    if strategy not in ['median', 'mean']:
        raise ValueError("Invalid strategy. Accepted values are 'median' or 'mean'.")

    numeric_columns = df_copy.select_dtypes(include=np.number).columns
    non_numeric_columns = df_copy.select_dtypes(exclude=np.number).columns

    if fill_non_numeric == True:
        for col in non_numeric_columns:
            df_copy[col] = df_copy[col].fillna('Unknown')
    elif fill_non_numeric == False:
        for col in non_numeric_columns:
            df_copy[col] = df_copy[col].fillna(np.nan)
    else:
        for col in non_numeric_columns:
            df_copy[col] = df_copy[col].fillna(fill_non_numeric)

    if strategy == 'median':
        for col in numeric_columns:
            median_value = df_copy[col].median()
            df_copy[col] = df_copy[col].fillna(median_value)
    elif strategy == 'mean':
        for col in numeric_columns:
            mean_value = df_copy[col].mean()
            df_copy[col] = df_copy[col].fillna(mean_value)

    return df_copy

