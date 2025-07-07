import numpy as np
import pandas as pd
import pytest

from src.data_processing.missing_values import missing_values_imputer


def test_missing_values_imputer():
    df = pd.DataFrame({
        "Name": ["Alex", "George", "John", np.nan],
        "Age": [28, 24, np.nan, 15],
        "Height": [185, 180, 175, 186],
    })

    test_df = pd.DataFrame({
        "Name": ["Alex", "George", "John", "Casey"],
        "Age": [28.0, 24.0, 24.0, 15.0],
        "Height": [185, 180, 175, 186],
    })

    with pytest.raises(ValueError, match="Invalid strategy. Accepted values are 'median' or 'mean'."):
        missing_values_imputer(df, strategy='random')
    assert missing_values_imputer(df, fill_non_numeric='Casey').equals(test_df)