import requests
from PIL import Image
from io import BytesIO

# Replace with the actual image URL
image_url = 'https://example.com/path/to/your/image.jpg'  
file_path = 'C:\\Users\\ende\\Desktop\\10x\\Week-7\\Scripts\\temp\\downloaded_photos\\lobelia\\photo_9@13-11-2021_18-13-10.jpg'

try:
    response = requests.get(image_url)
    content_type = response.headers['Content-Type']

    if 'image' in content_type:
        # If the content is an image, save it
        image_data = BytesIO(response.content)
        with Image.open(image_data) as img:
            img.save(file_path)
        print(f"Image downloaded and saved successfully: {file_path}")
    else:
        # If the content is not an image, print the content type and some of the content
        print(f"Downloaded content is not an image. Content type: {content_type}")
        print(response.text[:500])  # Print the first 500 characters of the content

except Exception as e:
    print(f"Failed to download or save the image: {e}")
