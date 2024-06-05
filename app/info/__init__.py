from flask import Blueprint

info_bp = Blueprint(
    "info_bp",
    __name__,
    static_folder="static",
    static_url_path="/info/static",
    template_folder="templates"
)

from app.info import info