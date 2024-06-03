from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html", data={
            "total_visits": TotalVisits(),
            "now": datetime.now()
        })

class TotalVisits:
    COUNTER = 0
    
    def get(self):
        TotalVisits.COUNTER += 1
        return TotalVisits.COUNTER