import sys
import os

# Add root folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np
import joblib
import logging
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error

from src.data_processing import load_data, preprocess_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def train_and_serialize():
    # 1. Load and Preprocess Data
    logging.info("Loading and preprocessing data...")
    train_raw, _ = load_data()
    df = preprocess_data(train_raw)
    
    # Filter out closed stores and zero sales as per Rossmann competition standard
    df = df[(df['Open'] != 0) & (df['Sales'] > 0)]
    
    # Select Features and Target
    feature_cols = [
        'Store', 'DayOfWeek', 'Promo', 'StateHoliday', 'SchoolHoliday',
        'StoreType', 'Assortment', 'CompetitionDistance',
        'Year', 'Month', 'Day', 'WeekOfYear', 'IsWeekend'
    ]
    
    X = df[feature_cols]
    y = df['Sales']
    
    # Split into Train and Validation sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 2. Build Pipeline (Scaler + Random Forest Regressor)
    logging.info("Building machine learning pipeline...")
    model_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('rf', RandomForestRegressor(n_estimators=50, max_depth=15, random_state=42, n_jobs=-1))
    ])
    
    # 3. Fit Model
    logging.info("Training Random Forest model...")
    model_pipeline.fit(X_train, y_train)
    
    # Evaluate
    preds = model_pipeline.predict(X_val)
    rmse = np.sqrt(mean_squared_error(y_val, preds))
    mae = mean_absolute_error(y_val, preds)
    logging.info(f"Validation MAE: {mae:.2f}")
    logging.info(f"Validation RMSE: {rmse:.2f}")
    
    # 4. Serialize Model with Timestamp
    timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S-00")
    model_filename = f"model-{timestamp}.pkl"
    joblib.dump(model_pipeline, model_filename)
    logging.info(f"Model saved successfully as: {model_filename}")

if __name__ == '__main__':
    train_and_serialize()