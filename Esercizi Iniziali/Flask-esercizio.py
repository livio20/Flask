from datetime import datetime
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('flask-esercizio-risposta.html')


@app.route('/meteo')
def meteo():
    return render_template('meteo.html')


@app.route('/frasicelebri')
def libro():
    return render_template('meteo.html')



@app.route('/quantomanca')
def calendario():
    return render_template('meteo.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
