# Image Optimizer

## Overview
The Image Optimizer is a Python Flask application designed to optimize images by reducing their file size without compromising quality. This tool is useful for web developers and designers who need to optimize images for faster loading times and improved performance.

## Features
- Image compression
- Format conversion (e.g., JPEG to PNG)
- Batch processing of multiple images
- RESTful API for integration with other applications

## Installation

### Prerequisites
- Python 3.8 or higher
- Flask
- Pillow (Python Imaging Library)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/imageoptimizer.git
    cd imageoptimizer/imageoptimizer.app
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    export FLASK_APP=app.py
    flask run
    ```

## Usage

### API Endpoints
- **POST /optimize**: Optimize a single image.
    - **Request**: Multipart form data with the image file.
    - **Response**: Optimized image file.

- **POST /optimize/batch**: Optimize multiple images.
    - **Request**: Multipart form data with multiple image files.
    - **Response**: ZIP file containing optimized images.

### Example Request
```bash
curl -X POST -F "image=@/path/to/image.jpg" http://localhost:5000/optimize -o optimized_image.jpg
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.
