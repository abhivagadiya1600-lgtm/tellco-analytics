import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(train_path='data/train.csv', test_path='data/test.csv', store_path='data/store.csv'):
    """Loads train, test, and store datasets and merges store details."""
    logging.info("Loading datasets...")
    train = pd.read_csv(train_path, parse_dates=['Date'], low_memory=False)
    test = pd.read_csv(test_path, parse_dates=['Date'], low_memory=False)
    store = pd.read_csv(store_path, low_memory=False)
    
    logging.info(f"Train shape: {train.shape}, Test shape: {test.shape}, Store shape: {store.shape}")
    
    # Merge store metadata into train and test datasets
    train_merged = pd.merge(train, store, on='Store', how='left')
    test_merged = pd.merge(test, store, on='Store', how='left')
    
    return train_merged, test_merged, store

if __name__ == '__main__':
    train_df, test_df, store_df = load_data()
    print("Data loaded successfully!")
    print("\nTrain Head:")
    print(train_df.head(2))