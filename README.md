# Ethiopian Medical Businesses Data Warehouse

## Project Overview

As a data engineer at Kara Solutions, this project involves building a data warehouse to store data on Ethiopian medical businesses scraped from the web and Telegram channels. The data warehouse is designed to be robust, scalable, and capable of handling the unique challenges associated with scraping and data collection from Telegram channels. Additionally, the project integrates object detection capabilities using YOLO (You Only Look Once) to enhance data analysis.

## Business Need

A data warehouse significantly enhances data analysis. With all data stored centrally, comprehensive analyses can be performed to find valuable insights about Ethiopian medical businesses. This data helps identify trends, patterns, and correlations that are hard to detect with fragmented data, leading to better decision-making. A well-designed data warehouse also makes querying and reporting more efficient, enabling businesses to get actionable intelligence quickly and accurately.

## Project Structure

```plaintext
my_project/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
└── requirements.txt
```

## Tasks Overview

### Task 1 - Data Scraping and Collection Pipeline

- **Telegram Scraping:** Utilized the Telegram API and wrote custom scripts using the `telethon` package to extract data from public Telegram channels relevant to Ethiopian medical businesses.
- **Image Scraping:** Collected images from specific Telegram channels for object detection.

### Task 2 - Data Cleaning and Transformation

- **Data Cleaning:** Removed duplicates, handled missing values, and standardized formats.
- **Data Storage:** Stored the cleaned data in a SQLite database.

### Task 3 - Object Detection Using YOLO

- **Environment Setup:** Installed necessary dependencies, including YOLO and its required libraries.
- **Object Detection:** Used the pre-trained YOLO model to detect objects in the collected images.
- **Data Storage:** Stored the detection results in a database table.

### Task 4 - Expose the Collected Data Using FastAPI

- **Environment Setup:** Installed FastAPI and Uvicorn.
- **API Development:** Created a FastAPI application to expose the collected data through various endpoints.

## Getting Started

### Prerequisites

- Python 3.7+
- SQLite
- Git

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Endework/Kara-Solutions.git
   cd ethiopian-medical-data-warehouse
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the YOLO environment:**

   ```bash
   git clone https://github.com/ultralytics/yolov5.git
   cd yolov5
   pip install -r requirements.txt
   cd ..
   ```

### Running the Application

1. **Run the data scraping scripts:**

   Ensure the `telethon` API credentials are set up and run the data scraping scripts to collect data from Telegram channels.

2. **Run the object detection script:**

   Ensure the images are collected and placed in the specified directory, then run the YOLO object detection script to process the images and store the results.

3. **Run the FastAPI application:**

   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API:**

   The FastAPI application will be available at `http://127.0.0.1:8000`.

## Project Details

### main.py

Contains the FastAPI application setup and defines the API endpoints.

### database.py

Configures the database connection using SQLAlchemy.

### models.py

Defines the SQLAlchemy models for the database tables.

### schemas.py

Defines the Pydantic schemas for data validation and serialization.

### crud.py

Implements CRUD (Create, Read, Update, Delete) operations for the database.

## Future Work

- **Enhance Data Integration:** Integrate additional data sources to enrich the data warehouse.
- **Improve Data Analysis:** Implement more advanced data analysis techniques and visualizations.
- **Scalability:** Explore options for scaling the data warehouse using cloud-based solutions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

