from flask import Flask, render_template, jsonify, request
import requests, os

app = Flask(__name__)

PROJECT_ID = os.getenv("PROJECT_ID")
PIPELINE_ID = os.getenv("PIPELINE_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

def fetch_pipeline_stage_statuses(project_id, pipeline_id, access_token):
    url = f"https://gitlab.com/api/v4/projects/{project_id}/pipelines/{pipeline_id}/jobs"
    headers = {"PRIVATE-TOKEN": access_token} 

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        jobs = response.json()

        stages = ["validate", "plan", "apply", "destroy"]
        stage_statuses = {}

        for stage in stages:
            stage_jobs = [job for job in jobs if job["stage"] == stage]

            if not stage_jobs:
                stage_statuses[stage] = "pending"
            else:
                statuses = {job["status"] for job in stage_jobs}
                if "failed" in statuses:
                    stage_statuses[stage] = "failed"
                elif "running" in statuses:
                    stage_statuses[stage] = "running"
                elif "pending" in statuses:
                    stage_statuses[stage] = "pending"
                elif all(status == "success" for status in statuses):
                    stage_statuses[stage] = "success"
                else:
                    stage_statuses[stage] = "unknown"

        return {"stages": stage_statuses, "status_code": 200}

    except requests.exceptions.RequestException as e:
        # Handle HTTP errors by returning the status code
        if hasattr(e.response, "status_code"):
            return {"stages": {}, "status_code": e.response.status_code}
        return {"stages": {}, "status_code": 500}

@app.route("/")
def pipeline():
    return render_template("pipeline.html", pipeline_id=PIPELINE_ID)

# API route to fetch statuses
@app.route("/api/status")
def pipeline_status():
    # Allow overriding the pipeline ID via query parameter
    pipeline_id = request.args.get("pipeline_id", PIPELINE_ID)

    result = fetch_pipeline_stage_statuses(PROJECT_ID, pipeline_id, ACCESS_TOKEN)
    return jsonify(result)
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content

@app.route("/test-icons")
def test_icons():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Bootstrap Icons Test</title>
        <link rel="stylesheet" href="/static/css/bootstrap-icons.min.css">
    </head>
    <body>
        <h1>Bootstrap Icons Test</h1>
        <i class="bi bi-alarm"></i> Alarm Icon
        <i class="bi bi-check-circle"></i> Check Circle
    </body>
    </html>
    '''


if __name__ == "__main__":
    app.run(port=8080, debug=True)