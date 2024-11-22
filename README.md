# Image Optimizer

Image Optimizer is a simple tool to optimize images for web usage. It reduces the file size of images without compromising on quality.

## Features
- Image compression
- Single image optimization
- RESTful API for image processing

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation (Python Backend)

>Note: Python Backend is located in `imageoptimizer.app`

### 1. Clone the Repository

```bash
git clone https://github.com/JeremyMorgan/Super-Image-Optimizer.git
cd Super-Image-Optimizer/imageoptimizer.app
```

### 2. Create a Virtual Environment

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables (Optional)

```bash
# On macOS/Linux
export FLASK_APP=run.py
export FLASK_ENV=development

# On Windows
set FLASK_APP=run.py
set FLASK_ENV=development
```
### Run the Application

```bash
# Using Flask CLI
flask run

# Or using Python directly
python run.py
```

## Installation (React Frontend)

>Note: React Frontend is located in `imageoptimizer.web`

## Prerequisites

- Node.js (version 18 or later)
- npm (version 9 or later)

## Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JeremyMorgan/Super-Image-Optimizer.git
cd Super-Image-Optimizer/imageoptimizer.web
```
### 2. Install Dependencies

```bash
npm install
```

### 3. Configure Environment
Ensure your backend server is running and accessible. By default, the application attempts to connect to `http://127.0.0.1:5000/upload`.

### 4. Run the Development Server

```bash
npm run dev
```

The application will be available at `http://localhost:5173`

### 5. Build for Production

```bash
npm run build
```

### 6. Preview Production Build

```bash
npm run preview
```

### Available Scripts

- `npm run dev`: Starts the development server.
- `npm run build`: Builds the application for production.
- `npm run preview`: Serves the production build locally
- `npm run lint`: Runs ESLint to check for code quality

## Technology Stack

- React 18.3.1
- Vite 5.4.10
- ESLint for code linting
- React DOM for rendering

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the Creative Commons License (CC0 1.0 Universal). See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.
