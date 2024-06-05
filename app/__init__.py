from flask import Flask
from dynaconf import FlaskDynaconf
import os
import sys

def create_app():
    app = Flask(__name__)
    dynaconf = FlaskDynaconf(extensions_list=True)
    
    with app.app_context():
        os.environ["ROOT_PATH_FOR_DYNACONF"] = app.root_path
        
        dynaconf.init_app(app)
        
        app.config["SECRET_KEY"] = bytearray(app.config["SECRET_KEY"], "UTF-8")
        
        from . import info
        app.register_blueprint(info.info_bp)
        
        return app