import pandas as pd
import logging
import os
from sqlalchemy import create_engine

# Setting up logging
logging.basicConfig(filename='data_pipeline.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Step 1: Load your cleaned data into pandas DataFrames
try:
    df_telegram = pd.read_csv(r'C:\Users\ende\Desktop\10x\Week-7\Data\cleaned_telegram.csv')
    df_image = pd.read_csv(r'C:\Users\ende\Desktop\10x\Week-7\Data\cleaned_image.csv')
    logging.info('CSV files loaded successfully.')
except Exception as e:
    logging.error('Error loading CSV files: %s', e)
    raise

# Step 2: Database Storage (Optional: If you have a database to store your data)

# Specify an absolute path for the SQLite database file
db_path = r'C:\Users\ende\Desktop\10x\Week-7\db.sqlite'

# Ensure the directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Create an SQLite database file if it doesn't exist
if not os.path.exists(db_path):
    open(db_path, 'w').close()
    logging.info('SQLite database file created at %s', db_path)

# Connect to the SQLite database
engine = create_engine(f'sqlite:///{db_path}')

# Step 3: Save DataFrames to SQLite database
try:
    df_telegram.to_sql('telegram_data', engine, if_exists='replace', index=False)
    df_image.to_sql('image_data', engine, if_exists='replace', index=False)
    logging.info('Data saved to SQLite database.')
except Exception as e:
    logging.error('Error saving data to SQLite database: %s', e)
    raise
