import logging
from flask import Blueprint, request, jsonify, send_file
import cv2
import numpy as np
import io
import imghdr
from werkzeug.utils import secure_filename
from PIL import Image

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bp = Blueprint('main', __name__)

@bp.route('/upload', methods=['POST'])
def upload():
    """
    This function handles the image upload request. It validates the image file,
    checks the file extension and content, gets the quality parameter from the
    request, processes the image with OpenCV according to the quality parameter,
    and returns the processed image as binary data.

    Parameters:
    request: The request object containing the image file and quality parameter.

    Returns:
    send_file: The processed image as binary data if the request is successful,
    otherwise returns a JSON response with an error message.
    """
    try:
        if 'image' not in request.files:
            logger.error('No image part in the request')
            return jsonify({'error': 'No image part in the request'}), 400

        image = request.files['image']

        if image.filename == '':
            logger.error('No image selected for uploading')
            return jsonify({'error': 'No image selected for uploading'}), 400

        # Secure the filename
        filename = secure_filename(image.filename)

        # Check the file extension
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        if not ('.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions):
            logger.error('Invalid file extension: %s', filename)
            return jsonify({'error': 'Invalid file extension'}), 400

        # Check the file content
        image_content = image.read()
        image.seek(0)  # Reset the file pointer to the beginning
        if imghdr.what(None, h=image_content) not in allowed_extensions:
            logger.error('Invalid image file content for: %s', filename)
            return jsonify({'error': 'Invalid image file'}), 400

        # Additional validation using Pillow
        try:
            img = Image.open(io.BytesIO(image_content))
            img.verify()  # Verify that it is, in fact, an image
        except (IOError, SyntaxError) as e:
            logger.error('Invalid image file: %s', e)
            return jsonify({'error': 'Invalid image file'}), 400

        # Check if quality parameter is present
        if 'quality' not in request.form:
            logger.error('Quality parameter is missing')
            return jsonify({'error': 'Quality parameter is required'}), 400

        # Get the quality parameter from the request
        quality = request.form.get('quality', type=int)
        # Validate the quality parameter
        if quality is None or quality < 0 or quality > 100:
            logger.error('Invalid quality value: %s', quality)
            return jsonify({'error': 'Quality must be an integer between 0 and 100'}), 400

        # Read the image directly from the request
        img_array = np.frombuffer(image.read(), np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)

        if img is None:
            logger.error('Failed to decode image: %s', filename)
            return jsonify({'error': 'Failed to decode image'}), 400

        # Process the image with OpenCV
        _, buffer = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

        # Create a BytesIO object from the buffer
        img_io = io.BytesIO(buffer)

        # Validate the processed image
        try:
            processed_img = Image.open(img_io)
            processed_img.verify()
        except (IOError, SyntaxError) as e:
            logger.error('Failed to process image: %s', e)
            return jsonify({'error': 'Failed to process image'}), 400

        # Reset the BytesIO object pointer to the beginning
        img_io.seek(0)

        # Return the processed image as binary data
        return send_file(img_io, mimetype='image/jpeg')

    except Exception as e:
        logger.exception('An unexpected error occurred: %s', e)
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500
