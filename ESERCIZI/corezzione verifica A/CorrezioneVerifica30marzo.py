import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import contextily
import geopandas as gpd
import io



from flask import Flask, render_template, request, Response , redirect , url_for
app = Flask(__name__)

import pandas as pd

stazioni = pd.read_csv('/workspace/Flask/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv',sep=';')
stazionigeo = gpd.read_file('/workspace/Flask/ds710_coordfix_ripetitori_radiofonici_milano_160120_loc_final.geojson')
quartieri = gpd.read_file('/workspace/Flask/ds964_nil_wm (1)-20220322T111443Z-001.zip')


@app.route('/', methods=['GET'])
def home():
    return render_template('home1.html')



@app.route('/numero', methods=['GET'])
def numero():

#numero stazioni per ogni municipio 
    global risultato 
    risultato=stazioni.groupby('MUNICIPIO')['OPERATORE'].count().reset_index()


    return render_template('elenco.html',risultato=risultato.to_html())


@app.route('/grafico', methods=['GET'])
def grafico():

    fig, ax = plt.subplots(figsize = (6,4))
    x = risultato.MUNICIPIO
    y = risultato.OPERATORE

    ax.bar(x,y, color='red')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    return Response(output.getvalue(), mimetype='image/png')



@app.route('/selezione', methods=['GET'])
def selezione():

    scelta = request.args['Scelta']
    if scelta == 'es1' :
        return redirect(url_for('numero'))
    elif scelta == 'es2':
        return redirect(url_for('input'))
    else:
        return redirect(url_for('dropdown'))


@app.route('/input', methods=['GET'])
def input():
    return render_template('input.html')


@app.route('/ricerca', methods=['GET'])
def ricerca():
    global quartiere, stazioni_quartiere

    nome_quartieri = request.args['quartiere']
    quartiere= quartieri[quartieri.NIL.str.contains(nome_quartieri)]
    stazioni_quartiere = stazionigeo[stazionigeo.intersects(quartiere.geometry.squeeze())]

    return render_template('elenco1.html', risultato=stazioni_quartiere.to_html())

    
    
@app.route('/mappa', methods=['GET'])
def mappa():

    fig, ax = plt.subplots(figsize=(12, 8))

    stazioni_quartiere.to_crs(epsg=3857).plot(ax=ax,color='k')
    quartiere.to_crs(epsg=3857).plot(ax=ax, alpha=0.5,)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')



@app.route('/dropdown', methods=['GET'])
def dropdown():
    nomi_stazioni= stazioni.OPERATORE.to_list()
    nomi_stazioni= list(set(nomi_stazioni))
    nomi_stazioni.sort()
    return render_template('dropdown.html',stazioni=nomi_stazioni)



@app.route('/sceltastazione', methods=['GET'])
def sceltastazione():
    global quartiere1 ,stazione_utente
    stazione = request.args['stazione']
    stazione_utente= stazionigeo[stazionigeo.OPERATORE==stazione]
    quartiere1=quartieri[quartieri.contains(stazione_utente.geometry.squeeze())]
    return render_template('vistastazione.html', quartiere=quartiere1)







@app.route('/mappaquart', methods=['GET'])
def mappaquart():

    fig, ax = plt.subplots(figsize=(12, 8))

    stazione_utente.to_crs(epsg=3857).plot(ax=ax,color='k')
    quartiere1.to_crs(epsg=3857).plot(ax=ax, alpha=0.5,)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
















































if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)