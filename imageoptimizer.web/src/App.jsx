import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'


/**
 * Main application component for image optimization.
 * Handles image selection, quality adjustment, and optimization process.
 * Displays both original and optimized images with size comparisons.
 *
 * @returns {JSX.Element} The rendered application component
 */
function App() {
  const [count, setCount] = useState(0)
  const [selectedImage, setSelectedImage] = useState(null);
  const [selectedImageUrl, setSelectedImageUrl] = useState(null);
  const [selectedImageSize, setSelectedImageSize] = useState(null);
  const [quality, setQuality] = useState(80);
  const [optimizedImageUrl, setOptimizedImageUrl] = useState(null);
  const [optimizedImageSize, setOptimizedImageSize] = useState(null);

  /**
   * Formats file size from bytes to a human-readable string.
   *
   * @param {number} bytes - The file size in bytes
   * @returns {string} Formatted file size with appropriate unit (Bytes, KB, MB, or GB)
   */
  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  const handleImageSelect = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(file);
      setSelectedImageSize(file.size);
      setSelectedImageUrl(URL.createObjectURL(file));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!selectedImage) {
      alert('Please select an image first');
      return;
    }

    const formData = new FormData();
    formData.append('image', selectedImage);
    formData.append('quality', quality);

    try {
      const response = await fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const blob = await response.blob();
        const imageUrl = URL.createObjectURL(blob);
        setOptimizedImageUrl(imageUrl);
        setOptimizedImageSize(blob.size);
      } else {
        console.error('Upload failed');
      }
    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

  useEffect(() => {
    return () => {
      // Cleanup URLs when component unmounts
      if (selectedImageUrl) {
        URL.revokeObjectURL(selectedImageUrl);
      }
      if (optimizedImageUrl) {
        URL.revokeObjectURL(optimizedImageUrl);
      }
    };
  }, [selectedImageUrl, optimizedImageUrl]);

  return (
    <div className="container">
      <header className="header">
        <h1>Image Optimizer</h1>
      </header>

      <main className="main-content">
        <form onSubmit={handleSubmit} className="upload-form">
          <div className="upload-section">
            <label htmlFor="image-upload">Upload Image</label>
            <input
              id="image-upload"
              type="file"
              accept="image/*"
              onChange={handleImageSelect}
            />
          </div>

          <div className="quality-section">
            <label htmlFor="quality">Quality: {quality}%</label>
            <input
              type="range"
              id="quality"
              min="0"
              max="100"
              value={quality}
              onChange={(e) => setQuality(parseInt(e.target.value))}
            />
          </div>

          <div className="button-section">
            <button type="submit">Optimize Image</button>
          </div>
        </form>

        <div className="images-comparison">
          {selectedImageUrl && (
            <div className="image-container">
              <h2>Original Image</h2>
              <img 
                src={selectedImageUrl} 
                alt="Original version" 
                style={{ maxWidth: '100%', height: 'auto' }}
              />
              <p>Size: {formatFileSize(selectedImageSize)}</p>
            </div>
          )}

          {optimizedImageUrl && (
            <div className="image-container">
              <h2>Optimized Image</h2>
              <img 
                src={optimizedImageUrl} 
                alt="Optimized version" 
                style={{ maxWidth: '100%', height: 'auto' }}
              />
              <p>Size: {formatFileSize(optimizedImageSize)}</p>
              {selectedImageSize && optimizedImageSize && (
                <p>Size Reduction: {(((selectedImageSize - optimizedImageSize) / selectedImageSize) * 100).toFixed(1)}%</p>
              )}
            </div>
          )}
        </div>
      </main>
    </div>
  )
}

export default App
