import pandas as pd
import numpy as np
from src.pipeline.cleaning_pipeline import run_cleaning_pipeline

def test_run_cleaning_pipeline():
    df = pd.DataFrame({
        "Age": [28, 24, np.nan, 15],
        "Height": [185, 180, 175, 186],
    })
    assert type(run_cleaning_pipeline(df)) == type(pd.DataFrame()), "if dataframe has the same type"
    assert run_cleaning_pipeline(df).isna().sum().sum() == 0, "function should fill all nan, and return 0"






