import os
import logging
import subprocess
import sys

# Setting up logging
logging.basicConfig(filename='object_detection.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to install packages
def install(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure psutil is installed
install('psutil')

import torch
import cv2
import pandas as pd
from sqlalchemy import create_engine

# Load the YOLOv5 model
yolov5_path = r'C:\Users\ende\Desktop\10x\Week-7\yolov5'
model = torch.hub.load(yolov5_path, 'custom', path='yolov5s.pt', source='local')

# Root directory containing images
root_dir = r'C:\Users\ende\Desktop\10x\Week-7\Scripts\temp\downloaded_photos'  # Update with the path where your "downloaded_photos" folder is located

# Subdirectories to process
subdirs = ['CheMed', 'lobelia']

# Create a list to store detection results
detection_results = []

# Loop through each subdirectory
for subdir in subdirs:
    subdir_path = os.path.join(root_dir, subdir)
    
    if not os.path.exists(subdir_path):
        logging.warning(f'Subdirectory {subdir_path} does not exist.')
        continue
    
    # Loop through all images in the subdirectory
    for filename in os.listdir(subdir_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(subdir_path, filename)
            try:
                # Verify image path
                if not os.path.exists(image_path):
                    logging.error(f'Image file does not exist: {image_path}')
                    continue

                # Verify image loading
                print(f'Reading image: {image_path}')
                img = cv2.imread(image_path)
                if img is None:
                    logging.error(f'Failed to load image {image_path}')
                    continue
                else:
                    print(f'Image {filename} loaded with shape: {img.shape}')
                
                # Perform object detection
                results = model(img)
                print(f'Detection results for {filename}: {results.xyxy}')
                
                # Extract results
                for result in results.xyxy[0].cpu().numpy():
                    x1, y1, x2, y2, confidence, class_id = result
                    class_name = model.names[int(class_id)]
                    detection_results.append({
                        'filename': filename,
                        'directory': subdir,
                        'x1': x1,
                        'y1': y1,
                        'x2': x2,
                        'y2': y2,
                        'confidence': confidence,
                        'class': class_name
                    })
                    print(f'Detection results for {filename}: {detection_results[-1]}')
                logging.info(f'Processed {filename} from {subdir} successfully.')
            except Exception as e:
                logging.error(f'Error processing {filename} from {subdir}: {e}')

# Convert detection results to a DataFrame
df_results = pd.DataFrame(detection_results)

# Save results to a CSV file
df_results.to_csv('detection_results.csv', index=False)

# Display the results DataFrame
print(df_results.head())

# Specify an absolute path for the SQLite database file
db_path = r'C:\Users\ende\Desktop\10x\Week-7\db.sqlite'

# Create an SQLite database file if it doesn't exist
if not os.path.exists(db_path):
    open(db_path, 'w').close()
    logging.info('SQLite database file created at %s', db_path)

# Check if df_results is empty before saving to the database
if not df_results.empty:
    # Connect to the SQLite database
    engine = create_engine(f'sqlite:///{db_path}')

    # Save DataFrame to SQLite database
    try:
        df_results.to_sql('detection_data', engine, if_exists='replace', index=False)
        logging.info('Detection data saved to SQLite database.')
    except Exception as e:
        logging.error('Error saving detection data to SQLite database: %s', e)
        raise
else:
    logging.warning('DataFrame df_results is empty. No data to save to SQLite database.')
