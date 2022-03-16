#realizzare un server web che permetta di conoscere i capoluoghi di regione
#l'utente inserisce il nome della regione e il programma restituisce il nome della regione
#caricare i capoluoghi di regioni in una lista di dizionari
# modificare l'es precedente e permettere l'utente di inserire il capoluogo della regione 
#l'utente sceglie se avere la regione o il capoluogo selezionando un radio button


from flask import Flask,render_template, request
app = Flask(__name__)

capoluoghiRegione = {'Abruzzo':'Aquila' , 'Basilicata':'Potenza' , 'Calabria':'Catanzaro' , 'Campania':'Napoli' ,
  'EmiliaRomagna':'Bologna' , 'Friuli':'Trieste' , 'Lazio':'Roma' , 'Liguria':'Genova' , 'Lombardia':'Milano' ,
  'Marche':'Ancona' , 'Molise':'Campobasso' , 'Piemonte':'Torino' , 'Puglia':'Bari' , 'Sardegna':'Cagliari' , 'Sicilia':'Palermo' , 
  'Toscana':'Firenze' , 'Trentino':'Trento' , 'Umbria':'Perugia' , 'ValleDAosta':'Aosta' , 'Veneto':'Venezia'}

Reg = list(capoluoghiRegione.keys())
Cap = list(capoluoghiRegione.values())

@app.route('/', methods=['GET'])
def RC():
    return render_template('info.html')


@app.route('/info', methods=['GET'])
def CR():
    CR = request.args['Tipo']
    if CR == 'Capoluogo':
        return render_template('capoluoghi.html')
    else: 
        return render_template('Regione.html')


@app.route("/regioni", methods=["GET"])
def dataReg():
    regione = request.args["Regione"]
    for key, value in capoluoghiRegione.items():
        if regione == key:
            capoluogo = value
            return render_template("outputes3.html", risposta = capoluogo)
    return "<h1>Errore</h1>"

@app.route("/capologhi", methods=["GET"])
def dataCap():
    capoluogo = request.args["Capoluogo"]
    for key, value in capoluoghiRegione.items():
        if capoluogo == value:
             regione = key
             return render_template("outputes3.html", risposta = regione)
    return "<h1>Errore</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)