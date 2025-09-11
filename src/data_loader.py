import pandas as pd

def load_data(file_path="data/sample.csv"):
    """
    Loads machine sensor data from a CSV file.
    
    Parameters:
        file_path (str): Path to the CSV file (default: data/sample.csv)
    
    Returns:
        pd.DataFrame: Loaded dataframe
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Data loaded successfully! Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print("❌ CSV file not found. Please check the file path.")
        return None

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        print(df.head())
