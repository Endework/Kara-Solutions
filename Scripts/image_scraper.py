import json
import os
import requests
import csv
import logging

# Setup logging
logging.basicConfig(filename='scraping.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to download photos
def download_photos(base_url, json_file, download_dir):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    rows = []
    for message in data['messages']:
        if 'photo' in message:
            photo_url = os.path.join(base_url, message['photo'])
            date = message['date']
            text = extract_text_from_message(message)
            
            # Download photo
            response = requests.get(photo_url)
            if response.status_code == 200:
                photo_name = photo_url.split('/')[-1]
                with open(os.path.join(download_dir, photo_name), 'wb') as file:
                    file.write(response.content)
                logging.info(f"Downloaded {photo_name}")
                # Store info in rows list
                rows.append([photo_url, date, text])
            else:
                logging.error(f"Failed to download {photo_url}")
    
    return rows

# Function to extract text from message
def extract_text_from_message(message):
    if 'text' in message:
        text = ''
        for item in message['text']:
            if isinstance(item, dict) and item.get('type') == 'link':
                continue  # Skip link items
            elif isinstance(item, str):
                text += item.strip() + ' '
        return text.strip()
    return ''

# Function to write to CSV
def write_to_csv(csv_file, rows):
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Photo URL', 'Date', 'Text'])
        writer.writerows(rows)

# Main function
def main():
    # List of JSON files and base URLs
    channels = [
        {'name': 'CheMed', 'json_file': '../Data/CheMed.json', 'base_url': 'https://t.me/CheMed123'},
        {'name': 'lobelia', 'json_file': '../Data/lobelia.json', 'base_url': 'https://t.me/lobelia4cosmetics'}
    ]

    # Temporary directory to store downloaded photos
    temp_dir = 'temp/'
    os.makedirs(temp_dir, exist_ok=True)

    # Download photos and save information to CSV
    for channel in channels:
        json_file = channel['json_file']
        base_url = channel['base_url']
        download_dir = os.path.join(temp_dir, 'downloaded_photos', channel['name'])
        os.makedirs(download_dir, exist_ok=True)
        
        rows = download_photos(base_url, json_file, download_dir)

        # Write to CSV
        csv_file = os.path.join(temp_dir, f"{channel['name']}_photo_info.csv")
        write_to_csv(csv_file, rows)
        logging.info(f"Photo information saved to {csv_file}")

    logging.info("Processing completed.")

if __name__ == "__main__":
    main()
