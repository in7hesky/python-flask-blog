from flask import render_template
from datetime import datetime
from . import info_bp
from logging import getLogger

logger = getLogger(__file__)

@info_bp.route("/")
def home():
    logger.debug("assembling home page")
    return render_template(
        "index.html", data={
        "total_visits": TotalVisits(),
        "now": datetime.now()
})

@info_bp.route("/about")
def about():
    logger.debug("assembling about page")
    return render_template("about.html")
    
class TotalVisits:
    COUNTER = 0
    
    def get(self):
        TotalVisits.COUNTER += 1
        return TotalVisits.COUNTER