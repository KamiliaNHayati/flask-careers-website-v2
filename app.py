from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
from sqlalchemy import text

app = Flask(__name__)

JOBS = [
    {'id': 1, 'title': 'Data Analyst', 'location': 'Remote', 'salary': '$80,000'},
    {'id': 2, 'title': 'Data Scientist', 'location': 'Remote', 'salary': '$90,000'},
    {'id': 3, 'title': 'Data Engineer', 'location': 'Remote', 'salary': '$100,000'}
]

@app.route('/')
def index():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name="Carreerly")

@app.route('/api/jobs')
def list_jobs():
    return jsonify(load_jobs_from_db())

@app.route('/job/<id>')
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Job not found", 404
    return render_template('jobpage.html', job=job, company_name="Carreerly")

@app.route('/api/job/<id>')
def show_job_json(id):
    job = load_job_from_db(id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404
    return jsonify(job)

@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id): # because use post method, the result will be in the form data
    data = request.form
    job = load_job_from_db(id)
    add_application_to_db(id, data)
    return render_template('application_submitted.html', application=data, job=job)

if __name__ == "__main__":
    app.run(debug=True)