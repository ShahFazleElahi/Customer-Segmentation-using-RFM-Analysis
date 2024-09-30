def calculate_rfm(df):
    snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceID': 'count',
        'Amount': 'sum'
    }).rename(columns={
        'InvoiceDate': 'Recency',
        'InvoiceID': 'Frequency',
        'Amount': 'MonetaryValue'
    })
    return rfm
