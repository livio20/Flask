# appes2
# realizzare un sito web che permetta la registrazione dei
# l'utente inserisce il nome, pass conferma ,della pass e il sesso
# se le informazioni sono corrette il sito salva le informazioni in una struttura dati opportuna
# (una lista di dizionari)
# prevedere la possibilità di fare il login inserendo username e pass
# se sono correte fornire un messaggio di benvenuto diverso a secondo del sesso


from flask import Flask, render_template, request
app = Flask(__name__)
lista = []


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('appes2registra.html')


@app.route('/registrazione', methods=['GET'])
def registrazione():

    name = request.args['name']
    username = request.args['username']
    Sex = request.args['Sex']
    password = request.args['password']
    Conferma_Password = request.args['Conferma_Password']
    if password == Conferma_Password:
        lista.append({'name': name, 'username': username,
                     'password': password, 'Sex': Sex})
        return render_template('appes2login.html')
    else:
        return render_template('appes2errore.html')


@app.route('/login1', methods=['GET'])
def login1():
    username_log = request.args['username']
    password_log = request.args['password']

    for utente in lista:
        if utente['username'] == username_log and utente['password'] == password_log:
            if utente['Sex'] == 'M':
               return render_template('appes2benvenuto.html', nome_user=utente['name'])
            else: 
                return render_template('appes2benvenuta.html', nome_user=utente['name'])
            
    return render_template('appes2errore.html', messaggio='username o password sbagliati')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
