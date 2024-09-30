import matplotlib.pyplot as plt
import seaborn as sns

def plot_rfm_distribution(rfm):
    plt.figure(figsize=(12, 6))
    sns.histplot(rfm['MonetaryValue'], bins=30, kde=True)
    plt.title('Monetary Value Distribution')
    plt.xlabel('Monetary Value')
    plt.ylabel('Frequency')
    plt.show()

def plot_segment_pie_chart(rfm):
    segment_counts = rfm['RFM_Score'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%')
    plt.title('Customer Segmentation Distribution')
    plt.show()
