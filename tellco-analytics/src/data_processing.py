import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(train_path='data/train.csv', test_path='data/test.csv', store_path='data/store.csv'):
    """Loads train, test, and store datasets and merges store details."""
    train = pd.read_csv(train_path, parse_dates=['Date'], low_memory=False)
    test = pd.read_csv(test_path, parse_dates=['Date'], low_memory=False)
    store = pd.read_csv(store_path, low_memory=False)
    
    train_merged = pd.merge(train, store, on='Store', how='left')
    test_merged = pd.merge(test, store, on='Store', how='left')
    return train_merged, test_merged

def preprocess_data(df):
    """Extracts date features, encodes categorical variables, and fills missing values."""
    logging.info("Preprocessing features...")
    df = df.copy()
    
    # 1. Extract Date Features
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['WeekOfYear'] = df['Date'].dt.isocalendar().week.astype(int)
    df['IsWeekend'] = df['DayOfWeek'].apply(lambda x: 1 if x in [6, 7] else 0)
    
    # 2. Handle Missing Values
    df['CompetitionDistance'] = df['CompetitionDistance'].fillna(df['CompetitionDistance'].median())
    df['CompetitionOpenSinceMonth'] = df['CompetitionOpenSinceMonth'].fillna(0)
    df['CompetitionOpenSinceYear'] = df['CompetitionOpenSinceYear'].fillna(0)
    df['Promo2SinceWeek'] = df['Promo2SinceWeek'].fillna(0)
    df['Promo2SinceYear'] = df['Promo2SinceYear'].fillna(0)
    df['PromoInterval'] = df['PromoInterval'].fillna('None')
    df['Open'] = df['Open'].fillna(1)
    
    # 3. Categorical Encoding
    mappings = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 0: 0}
    df['StoreType'] = df['StoreType'].map(mappings).fillna(0)
    df['Assortment'] = df['Assortment'].map(mappings).fillna(0)
    df['StateHoliday'] = df['StateHoliday'].astype(str).map({'0': 0, 'a': 1, 'b': 2, 'c': 3}).fillna(0)
    
    return df

if __name__ == '__main__':
    train_df, test_df = load_data()
    train_clean = preprocess_data(train_df)
    print("Preprocessing successful! Processed Train Shape:", train_clean.shape)
    