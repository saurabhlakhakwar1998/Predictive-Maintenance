import pandas as pd
import joblib
from data_loader import load_data

def run_inference(model_path="models/model.pkl", data_path="data/sample.csv"):
    """
    Runs inference using a trained model on new data.
    
    Parameters:
        model_path (str): Path to the saved model
        data_path (str): Path to the input CSV file
    
    Returns:
        pd.DataFrame: Original data with predictions column
    """
    try:
        # Load trained model
        model = joblib.load(model_path)
        print("✅ Model loaded successfully!")
    except FileNotFoundError:
        print("❌ Model file not found. Please train and save a model first.")
        return None

    # Load input data
    df = load_data(data_path)
    if df is None:
        return None

    # Drop non-numeric columns if any (like machine_id)
    X = df.select_dtypes(include=['float64', 'int64'])

    # Make predictions
    df['predicted_failure'] = model.predict(X)
    print("✅ Inference completed!")
    return df

if __name__ == "__main__":
    results = run_inference()
    if results is not None:
        print(results.head())
