# Image Optimizer Web Application

This document provides an overview of the Image Optimizer web application, which is a React application using Vite as the build tool. It includes installation instructions and a summary of the key files in the `/imageoptimizer.app` directory.

## Installation Instructions

To get started with the Image Optimizer application, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/imageoptimizer.git
    cd imageoptimizer/imageoptimizer.web
    ```

2. **Install dependencies:**
    ```sh
    npm install
    ```

3. **Run the development server:**
    ```sh
    npm run dev
    ```

4. **Build the application for production:**
    ```sh
    npm run build
    ```

5. **Preview the production build:**
    ```sh
    npm run preview
    ```

## File Structure and Descriptions

### `/src`
- **index.html**: The main HTML file that includes the root div where the React application will be mounted.
- **main.jsx**: The entry point of the React application. It renders the root component into the DOM.
- **App.jsx**: The root component of the application. It contains the main layout and routing logic.

### `/src/components`
- **Header.jsx**: A component that renders the header of the application.
- **Footer.jsx**: A component that renders the footer of the application.
- **ImageUploader.jsx**: A component that allows users to upload images for optimization.
- **ImageList.jsx**: A component that displays the list of uploaded images and their optimization status.

### `/src/styles`
- **global.css**: Contains global CSS styles for the application.
- **header.css**: Contains styles specific to the Header component.
- **footer.css**: Contains styles specific to the Footer component.
- **imageUploader.css**: Contains styles specific to the ImageUploader component.
- **imageList.css**: Contains styles specific to the ImageList component.

### `/src/utils`
- **api.js**: Contains functions for making API calls to the backend server.
- **helpers.js**: Contains helper functions used throughout the application.

### `/public`
- **favicon.ico**: The favicon for the application.
- **robots.txt**: Instructions for web crawlers.

## Making Modifications

To make modifications to the application, follow these steps:

1. **Add new components**: Create a new file in the `/src/components` directory and define your component. Import and use it in `App.jsx` or other components as needed.
2. **Update styles**: Modify the existing CSS files in the `/src/styles` directory or add new CSS files for new components.
3. **API integration**: Update or add new functions in `/src/utils/api.js` to interact with the backend server.
4. **Routing**: Modify the routing logic in `App.jsx` to add new routes or update existing ones.

By following this guide, you should be able to get familiar with the Image Optimizer application and make necessary modifications to enhance its functionality.
