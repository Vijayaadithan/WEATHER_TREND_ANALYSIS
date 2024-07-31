import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)  # Load the CSV data file.

def clean_and_transform_data(df):
    # Convert date column to datetime
    df['datetime_utc'] = pd.to_datetime(df['datetime_utc'])
    df['year'] = df['datetime_utc'].dt.year
    df['month'] = df['datetime_utc'].dt.month
    df['date'] = df['datetime_utc'].dt.day

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values
    df.fillna(method='ffill', inplace=True)

    return df

def save_processed_data(df, output_path):
    df.to_csv(output_path, index=False)  # Store to the new CSV file


file_path = r"C:\Users\91735\OneDrive\Desktop\securin\testset.csv"
output_path = 'processed_delhi_weather_data.csv'
    
df = load_data(file_path)
df = clean_and_transform_data(df)
save_processed_data(df, output_path)



