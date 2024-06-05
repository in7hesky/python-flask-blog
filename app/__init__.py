from flask import Flask

def create_app():
    app = Flask(__name__)
    
    with app.app_context():
        from . import info
        
        app.register_blueprint(info.info_bp)
        
        return app