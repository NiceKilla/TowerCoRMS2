from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

incident_log = []

@app.route("/")
def dashboard():
    return render_template("dashboard.html", incidents=incident_log)

@app.route("/trigger", methods=["POST"])
def trigger_alert():
    data = request.json
    sensor_type = data.get("sensor")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    incident = {"sensor": sensor_type, "timestamp": timestamp}
    incident_log.append(incident)
    return jsonify({"status": "alert received", "incident": incident})

if __name__ == "__main__":
    app.run(debug=True)
