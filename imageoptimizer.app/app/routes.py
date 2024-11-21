from flask import Blueprint, request, jsonify, send_file
import cv2
import numpy as np
import io

bp = Blueprint('main', __name__)

@bp.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({'error': 'No image selected for uploading'}), 400

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

    # Return the processed image as binary data
    return send_file(img_io, mimetype='image/jpeg')
