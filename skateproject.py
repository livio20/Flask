import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import contextily
import geopandas as gpd
import io
import pandas as pd



from flask import Flask, render_template, request, Response , redirect , url_for
app = Flask(__name__)


park1 = pd.read_csv('skatepark_milano_list.csv')
milano = gpd.read_file('ds964_nil_wm-20220322T104009Z-001.zip')
PARKS1 = gpd.read_file('PARKS.geojson')
SHOPS1 = gpd.read_file('SHOPS.geojson')

@app.route("/", methods=["GET"])
def scelta():
    return render_template("choice.html")


@app.route('/selezione', methods=['GET'])
def selezione():

    scelta = request.args['Scelta']
    if scelta == 'utente':
        return render_template("utente.html")
    elif scelta == 'ospite':
        return render_template("home.html")


@app.route('/selezione1', methods=['GET'])
def selezione1():

    scelta = request.args['Scelta']
    if scelta == 'login':
        return render_template("login.html")
    elif scelta == 'new_account':
        return render_template("new_account.html")






##login registrazione##




@app.route('/inserisci', methods=['GET'])
def inserisci():
    return render_template('new_account.html')

@app.route('/dati', methods=['GET'])
def dati():
    
    
    email = request.args['email']
    psw = request.args['psw']
    pswrepeat = request.args['psw-repeat']
    
    
    df1 = pd.read_csv('database.csv')
    
    
    nuovi_dati = {'email':email,'psw':psw,'psw-repeat':pswrepeat}
    
    df1 = df1.append(nuovi_dati,ignore_index=True)
    
    
    df1.to_csv('database.csv', index=False)
    rdf1 = df1.to_html()
    #return df1.to_html()
    return render_template('indexs2.html', tables=[rdf1], titles=[''])







@app.route('/login', methods=['GET'])
def login():
    email = request.args['email']
    psw = request.args['psw']
    
    if user["email"] == request.args["email"]:
            if user["psw"] == request.args['psw']:
                
                return render_template('welcome2.html', email=email,psw=psw)
        #return render_template('error.html')
    return render_template('error.html', err='utente non registrato')
   # return render_template('login.html', utenti = utenti)

@app.route('/data1', methods=['GET'])
def data():
    
    email = request.args['email']
    psw = request.args['psw']
    confirm = request.args['psw-repeat']

    
    df1 = pd.read_csv('database.csv')
    
    
    nuovi_dati = {'email':email,'psw':psw,'psw-repeat':psw-repeat}
    
    df1 = df1.append(nuovi_dati,ignore_index=True)
    
    
    df1.to_csv('database.csv', index=False)
    rdf1 = df1.to_html()
    
    if psw == confirm:
            if email:
                if psw:
                    if confirm:
                        if email:
                            utenti.append({"email": email, "psw": psw, "confirm": confirm})
                            print(utenti)
                            #return redirect(url_for("/login"))
                            return render_template('login.html', utenti=utenti , tables=[rdf1], titles=[''])
    

    return render_template('error.html', nome = email, err='errore generico')




















































































































@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("home.html")

@app.route("/login1", methods=["GET"])
def home1():
    return render_template("home.html")


@app.route("/storia", methods=["GET"])
def storia():
    return render_template("storia.html")


@app.route("/tavole", methods=["GET"])
def tavole():
    return render_template("tavole.html")


@app.route("/truck", methods=["GET"])
def truck():
    return render_template("truck.html")


@app.route("/ruote", methods=["GET"])
def ruote():
    return render_template("ruote.html")


@app.route("/cuscinetti", methods=["GET"])
def cuscinetti():
    return render_template("cuscinetti.html")


@app.route("/hardware", methods=["GET"])
def hardware():
    return render_template("hardware.html")


@app.route("/grip_tape", methods=["GET"])
def grip():
    return render_template("grip_tape.html")


@app.route("/tool", methods=["GET"])
def tool():
    return render_template("tool.html")


@app.route("/wax", methods=["GET"])
def wax():
    return render_template("wax.html")


@app.route("/guida_tavole", methods=["GET"])
def guida_tavole():
    return render_template("guida_tavole.html")


@app.route("/guida_truck", methods=["GET"])
def guida_truck():
    return render_template("guida_truck.html")


@app.route("/guida_ruote", methods=["GET"])
def guida_ruote():
    return render_template("guida_route.html")


@app.route("/contatti", methods=["GET"])
def contatti():
    return render_template("contatti.html")

@app.route("/maps", methods=["GET"])
def maps():
    return render_template("maps.html")


#MAPPA MAPS#

@app.route('/mappa', methods=['GET'])
def mappa():

    fig, ax = plt.subplots(figsize = (12,8))

    PARKS1.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, color='RED')
    SHOPS1.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, color='blue')
    milano.to_crs(epsg=3857).plot(ax=ax, alpha=0.2, edgecolor='k')
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')






#mappe e ricerca skatepark#
@app.route("/skatepark", methods=["GET"])
def park():
    
    return render_template("skatepark.html",risultato=PARKS1.to_html())
   
@app.route('/mappapark', methods=['GET'])
def mappapark():

    fig, ax = plt.subplots(figsize = (12,8))

    PARKS1.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, color='RED')
    milano.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor='k')
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/ricercapark', methods=['GET'])
def ricercapark():
    global quartiere,park_quartiere
    nome_park=request.args["park3"]
    quartiere=milano[milano.NIL.str.contains(nome_park.upper())]
    park_quartiere=PARKS1[PARKS1.within(quartiere.geometry.squeeze())]
    
    return render_template("skatepark_risultato.html",risultatopark2=park_quartiere.to_html())

@app.route('/mappapark1', methods=['GET'])
def mappapark1():

    fig, ax = plt.subplots(figsize = (10,10))

    park_quartiere.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, color='RED')
    quartiere.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor='k')
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


#mappe e ricerca skateshop#
@app.route("/skateshop", methods=["GET"])
def shop():
    return render_template("skateshop.html",risultatoshop=SHOPS1.to_html())   

@app.route('/mappashop', methods=['GET'])
def mappashop():

    fig, ax = plt.subplots(figsize = (12,8))

    SHOPS1.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, color='RED')
    milano.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor='k')
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/ricercashop', methods=['GET'])
def ricercashop():
    global quartiere,shop_quartiere
    nome_shop=request.args["shop3"]
    quartiere=milano[milano.NIL.str.contains(nome_shop.upper())]
    shop_quartiere=SHOPS1[SHOPS1.within(quartiere.geometry.squeeze())]
    
    return render_template("skateshop_risultato.html",risultatoshop2=shop_quartiere.to_html())

@app.route('/mappashop1', methods=['GET'])
def mappashop1():

    fig, ax = plt.subplots(figsize = (10,10))

    shop_quartiere.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, color='RED')
    quartiere.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor='k')
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')






#fine#
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
