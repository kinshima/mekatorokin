from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# 勤怠データを読み込む
with open("attendance.json", encoding="utf-8") as f:
    attendance_data = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", records=attendance_data)

@app.route("/api")
def api():
    return jsonify(attendance_data)

if __name__ == "__main__":
    app.run()