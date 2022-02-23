from flask import Flask, render_template
app = Flask(__name__)

from datetime import datetime




@app.route('/')
def hello_world():
  return render_template('flask-esercizio-risposta.html')

@app.route('/meteo')
def stica():
  return render_template('meteo.html')



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3245, debug=True)