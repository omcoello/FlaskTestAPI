from flask import Flask
from .config import Config
from .database import SQLAlchemySingleton
from .views import main, products_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db = SQLAlchemySingleton.get_instance(app)

    app.register_blueprint(main)
    app.register_blueprint(products_bp)
        
    with app.app_context():
        db.create_all()
    
    return app
