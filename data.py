import pandas as pd


def csv_to_pandas(file_name, delimiter):
    return pd.read_csv(f'static/tables/{file_name}', sep=delimiter)
