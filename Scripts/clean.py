import pandas as pd
import logging
import os
from sqlalchemy import create_engine

# Setting up logging
logging.basicConfig(filename='data_pipeline.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


try:
    df_telegram = pd.read_csv(r'C:\Users\ende\Desktop\10x\Week-7\Data\cleaned_telegram.csv')
    df_image = pd.read_csv(r'C:\Users\ende\Desktop\10x\Week-7\Data\cleaned_image.csv')
    logging.info('CSV files loaded successfully.')
except Exception as e:
    logging.error('Error loading CSV files: %s', e)
    raise




db_path = r'C:\Users\ende\Desktop\10x\Week-7\db.sqlite'


os.makedirs(os.path.dirname(db_path), exist_ok=True)


if not os.path.exists(db_path):
    open(db_path, 'w').close()
    logging.info('SQLite database file created at %s', db_path)


engine = create_engine(f'sqlite:///{db_path}')


try:
    df_telegram.to_sql('telegram_data', engine, if_exists='replace', index=False)
    df_image.to_sql('image_data', engine, if_exists='replace', index=False)
    logging.info('Data saved to SQLite database.')
except Exception as e:
    logging.error('Error saving data to SQLite database: %s', e)
    raise
