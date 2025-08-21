import pandas as pd


def fill_missing_median(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    if columns is None:
        columns = df.select_dtypes(include='number').columns
    df_copy = df.copy()
    for col in columns:
        median = df_copy[col].median()
        df_copy[col].fillna(median, inplace=True)
    return df_copy


def drop_missing(df: pd.DataFrame, threshold=0.5) -> pd.DataFrame:
    df_copy = df.copy()
    missing_fraction = df_copy.isna().mean()
    cols_to_keep = missing_fraction[missing_fraction <= threshold].index
    return df_copy[cols_to_keep]


def normalize_data(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    if columns is None:
        columns = df.select_dtypes(include='number').columns
    df_copy = df.copy()
    for col in columns:
        min_val = df_copy[col].min()
        max_val = df_copy[col].max()
        if max_val != min_val:
            df_copy[col] = (df_copy[col] - min_val) / (max_val - min_val)
        else:
            df_copy[col] = 0.0
    return df_copy
