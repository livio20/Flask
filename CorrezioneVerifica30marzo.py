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

stazioni= pd.read_csv('/workspace/Flask/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv',sep=';')

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





































































if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)