from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('app.instance.config')
    
    
    # Register routes
    with app.app_context():
        from . import routes
        print("Routes imported successfully")
    return app

