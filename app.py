from flask import Flask, render_template
from candidate_dao import get_all_candidates
from company_dao import get_all_companies
from job_dao import JobDao
from application_dao import ApplicationDao

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/candidates')
def candidates():
    candidate_list = get_all_candidates()
    return render_template('candidates.html', candidates=candidate_list)

@app.route('/companies')
def companies():
    company_list = get_all_companies()
    return render_template('companies.html', companies=company_list)

@app.route('/jobs')
def jobs():
    job_list = JobDao.get_all_jobs()
    return render_template('jobs.html', jobs=job_list)

@app.route('/applications')
def applications():
    app_list = ApplicationDao.get_all_applications()
    return render_template('applications.html', applications=app_list)

@app.route('/interviews')
def interviews():
    return render_template('interviews.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)