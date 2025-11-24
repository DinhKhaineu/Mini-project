from flask import Flask, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import logging
import os

from config import DBConfig
from database import MySQLClient
from repository import StudentRepository
from analytics import StudentAnalytics

app = Flask(__name__)
CORS(app)

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

repo = None
analytics = None

try:
    config = DBConfig()
    client = MySQLClient(config)
    repo = StudentRepository(client)
    analytics = StudentAnalytics(repo)
    logger.info("Set up successfully")
except Exception as e:
    logger.info(f"Fail to set up {e}")


@app.route("/api/students")
def get_student():
    if repo is None:
        return jsonify({"Repos is not successfully set up"}), 500
    
    try: 
        student_df = repo.fetch_all_students()
        if student_df.empty:
            return jsonify([])
        students_json = student_df.to_dict('records')
        return jsonify(students_json)
    except Exception as e:
        logger.error(f"Error fetching students: {e}")
        return jsonify({"error": str(e)}), 500
    
@app.route("/api/run-report", methods = ["POST"])
def run_report():
    if analytics is None:
        return jsonify({"Analytics is not successfully set up"}), 500
    try:
        student_df = repo.fetch_all_students()
        if student_df.empty:
            return jsonify({"No data avail"}), 400
        final_report = analytics.run_full_analysis(student_df)
        os.makedirs("Result", exist_ok=True)
        final_report.to_csv("Result/final_report.csv", index = False)
        return jsonify({"Report successfully generated"})
    except Exception as e:
        logger.error(f"Error running report: {e}")
        return jsonify({"error:": str(e)}), 500

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True, port = 5000)
    