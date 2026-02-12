from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Remote',
        'salary': '$80,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Remote',
        'salary': '$90,000'
    },
    {
        'id': 3,
        'title': 'Data Engineer',
        'location': 'Remote',
        'salary': '$100,000'
    }
]

@app.route('/') # if / be accessed will return 'Hello World!'
def index():
    return render_template('home.html', jobs=JOBS, company_name="Carreerly")

@app.route('/jobs')
def list_jobS():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True) # when i change the code it will automatically reload
