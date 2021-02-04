from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    '''renders the root page describing the survey and asking for consent'''
    return render_template('index.html')


@app.route('/survey')
def survey():
    return render_template('survey.html')


@app.route('/decline')
def decline():
    return render_template('decline.html')


@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


@app.route('/api/results')
def results():
    reverse = request.args.get('reverse')
    if reverse:
        pass
    else:
        pass
    return {}


@app.route('/admin/summary')
def summary():
    return render_template('admin.html')