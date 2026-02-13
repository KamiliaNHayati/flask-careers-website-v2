from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        job = []
        for row in result.all():
            job.append(dict(row._mapping))
        return job

@app.route('/') # using slash it means empty after the domain name 
def index():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name="Carreerly")

@app.route('/jobs')
def list_jobS():
    return jsonify(load_jobs_from_db())

if __name__ == "__main__":
    app.run(debug=True) # when i change the code it will automatically reload
