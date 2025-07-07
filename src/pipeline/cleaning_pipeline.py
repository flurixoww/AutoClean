import pandas as pd
from src.data_processing.missing_values import missing_values_imputer


def run_cleaning_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    print("Running cleaning pipeline.")
    df = missing_values_imputer(df)
    print("Pipeline is finished.")
    return df


