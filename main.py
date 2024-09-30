from src.data_processing import load_data, clean_data
from src.rfm_calculations import calculate_rfm
from src.segmentation import segment_customers
from src.visualization import plot_rfm_distribution, plot_segment_pie_chart

def main():
    file_path = 'data/customer_data.csv'  # Update as necessary
    df = load_data(file_path)
    df = clean_data(df)
    
    rfm = calculate_rfm(df)
    rfm_segmented = segment_customers(rfm)
    
    plot_rfm_distribution(rfm_segmented)
    plot_segment_pie_chart(rfm_segmented)

if __name__ == "__main__":
    main()
