
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Age": [28, 24, 16, 18],
    "Height": [185, 180, 175, 186],
})

def bucketize_column(df: pd.DataFrame, col_name: str, categories: list, new_column_name: str, operator: str) -> pd.DataFrame:
    df_copy = df.copy()
    if df_copy[col_name].dtype not in [np.float64, np.int64]:
        raise TypeError(f"Column's dtype is not np.float64 or np.int64. \n Note: expected {np.float64} or {np.int64}"
                        f"but got {df_copy[col_name].dtype}", )
    df_copy[new_column_name] = np.nan
    if operator == "==":
        for i, val in enumerate(df_copy[col_name]):
            for cat in categories:
                if val == cat:
                    df_copy.loc[i, new_column_name] = categories.index(cat)
                    break

    return df_copy

print(bucketize_column(df, "Age", [24, 16], "groups", "=="))

