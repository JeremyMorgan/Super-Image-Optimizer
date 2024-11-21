from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads/'
    app.config['DEBUG'] = True  # Add this line to enable debug mode

    from . import routes
    app.register_blueprint(routes.bp)

    return app
