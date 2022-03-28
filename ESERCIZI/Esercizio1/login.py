from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello_world():
    return render_template('loginform.html')

@app.route('/date', methods = ['GET'])
def date():
    username = request.args['username']
    password = request.args['password']

    if username == 'admin' and password == 'xxx123##':
        return render_template('loginrender.html' ,name=username)
    else:
        return render_template('eror-render.html', name=username)
    


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)




#appes2
#realizzare un sito web che permetta la registrazione dei
#l'utente inserisce il nome, pass conferma ,della pass e il sesso
#se le informazioni sono corrette il sito salva le informazioni in una struttura dati opportuna 
#(una lista di dizionari)
#prevedere la possibilità di fare il login inserendo username e pass
#se sono correte fornire un messaggio di benvenuto diverso a secondo del sesso 