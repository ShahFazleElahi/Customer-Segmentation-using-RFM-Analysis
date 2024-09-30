import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path, on_bad_lines='skip')
    return df

def clean_data(df):
    if 'InvoiceDate' in df.columns:
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df = df.dropna(subset=['CustomerID', 'InvoiceDate', 'Amount'])
    return df
