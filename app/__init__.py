from flask import Flask, send_from_directory
from dynaconf import FlaskDynaconf
from pathlib import Path
import os
import sys
import logging
import logging.config
import yaml

def create_app():
    app = Flask(__name__)
    dynaconf = FlaskDynaconf(extensions_list=True)
    
    with app.app_context():
        os.environ["ROOT_PATH_FOR_DYNACONF"] = app.root_path
        
        dynaconf.init_app(app)
        
        app.config["SECRET_KEY"] = bytearray(app.config["SECRET_KEY"], "UTF-8")
        _configure_logging(app, dynaconf)
        
        from . import info
        app.register_blueprint(info.info_bp)
        
        @app.route('/favicon.ico')
        def favicon():
            return send_from_directory(
                os.path.join(app.root_path, 'static'),
                'images/favicon.ico',
                mimetype="image/vnd.microsoft.icon"
            )
        
        return app

def _configure_logging(app, dynaconf):
    logging_config_path = Path(app.root_path).parent / "logging_config.yaml"
    
    with open(logging_config_path, "r") as fh:
        logging_config = yaml.safe_load(fh.read())
        env_logging_level = dynaconf.settings.get("logging_level", "INFO").upper()
        logging_level = logging.INFO if env_logging_level == "INFO" else logging.DEBUG
    
        logging_config["handlers"]["console"]["level"] = logging_level
        logging_config["loggers"][""]["level"] = logging_level
        logging.config.dictConfig(logging_config)