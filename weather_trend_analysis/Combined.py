from preprocessing import load_data, clean_and_transform_data, save_processed_data
from storing_in_db import create_database, store_data_in_db

def print_message(message):
    print(f"[INFO] {message}")

def main():
    # File paths
    file_path = r"C:\Users\91735\OneDrive\Desktop\securin\testset.csv"
    processed_data_path = r"processed_delhi_weather_data.csv"
    db_name = r"weather_data.db"
    table_name = "delhi_weather"
    
    # Step 1: Data Processing
    print_message("Loading data...")
    df = load_data(file_path)
    
    print_message("Cleaning and transforming data...")
    df = clean_and_transform_data(df)
    
    print_message("Saving processed data...")
    save_processed_data(df, processed_data_path)

    # Step 2: Data Storage
    print_message("Creating database...")
    create_database(db_name)
    
    print_message("Storing data in database...")
    store_data_in_db(db_name, df, table_name)
    
    print_message("Process completed successfully.")

main()
