from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

JOBS = [
    {'id': 1, 'title': 'Data Analyst', 'location': 'Remote', 'salary': '$80,000'},
    {'id': 2, 'title': 'Data Scientist', 'location': 'Remote', 'salary': '$90,000'},
    {'id': 3, 'title': 'Data Engineer', 'location': 'Remote', 'salary': '$100,000'}
]

def load_jobs_from_db():
    if engine is None:
        return JOBS
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        return [dict(row._mapping) for row in result.all()]

@app.route('/')
def index():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name="Carreerly")

@app.route('/jobs')
def list_jobs():
    return jsonify(load_jobs_from_db())
    
if __name__ == "__main__":
    app.run(debug=True)