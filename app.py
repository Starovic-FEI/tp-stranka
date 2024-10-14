#!/home/tp/status-site/venv/bin/python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # test by nixer
def status():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/meetings')
def meetings():
    return render_template('meetings.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=20081)