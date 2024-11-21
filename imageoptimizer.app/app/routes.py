from flask import Blueprint, request, jsonify, send_file
import cv2
import numpy as np
import io
import imghdr
from werkzeug.utils import secure_filename
from PIL import Image

bp = Blueprint('main', __name__)

@bp.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({'error': 'No image selected for uploading'}), 400

    # Secure the filename
    filename = secure_filename(image.filename)

    # Check the file extension
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    if not ('.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions):
        return jsonify({'error': 'Invalid file extension'}), 400

    # Check the file content
    image_content = image.read()
    image.seek(0)  # Reset the file pointer to the beginning
    if imghdr.what(None, h=image_content) not in allowed_extensions:
        return jsonify({'error': 'Invalid image file'}), 400

    # Additional validation using Pillow
    try:
        img = Image.open(io.BytesIO(image_content))
        img.verify()  # Verify that it is, in fact, an image
    except (IOError, SyntaxError) as e:
        return jsonify({'error': 'Invalid image file'}), 400

    # Get the quality parameter from the request, default to 10 if not provided
    quality = request.form.get('quality', default=10, type=int)

    # Validate the quality parameter
    if quality < 0 or quality > 100:
        return jsonify({'error': 'Quality must be between 0 and 100'}), 400

    # Read the image directly from the request
    img_array = np.frombuffer(image.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)

    if img is None:
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
        return jsonify({'error': 'Failed to process image'}), 400

    # Reset the BytesIO object pointer to the beginning
    img_io.seek(0)

    # Return the processed image as binary data
    return send_file(img_io, mimetype='image/jpeg')
