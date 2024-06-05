from flask import render_template
from datetime import datetime
from . import info_bp

@info_bp.route("/")
def home():
    return render_template(
        "index.html", data={
        "total_visits": TotalVisits(),
        "now": datetime.now()
})

@info_bp.route("/about")
def about():
    return render_template("about.html")
    
class TotalVisits:
    COUNTER = 0
    
    def get(self):
        TotalVisits.COUNTER += 1
        return TotalVisits.COUNTER