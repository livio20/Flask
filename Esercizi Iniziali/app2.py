##realizzzare un server web che visualizzzi l'ora e colori lo sfondo in base all'orario : un colore della mattina , uno per il pomeriggio , uno per la sera e uno per la notte


from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/', methods=["GET"])
def time():
  return render_template(now.strftime('%Y-%m-%d %H:%M:%S))




if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3245, debug=True)