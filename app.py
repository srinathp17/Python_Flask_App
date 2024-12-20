from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[
    {'id': 101, 'title': 'Software Engineer', 'location': 'New York, USA', 'salary': '$120,000'},
    {'id': 102, 'title': 'Data Analyst', 'location': 'San Francisco, USA', 'salary': '$95,000'},
    {'id': 103, 'title': 'Project Manager', 'location': 'London, UK', 'salary': '£85,000'},
    {'id': 104, 'title': 'Web Developer', 'location': 'Berlin, Germany', 'salary': '€70,000'},
    {'id': 105, 'title': 'Frontend Developer', 'location': 'Remote'}
]

@app.route('/')
def Hello():
    return render_template('home.html', jobs=JOBS, company_name='Careers')

@app.route('/api/json')
def list_jobs():
    return jsonify(JOBS)
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)