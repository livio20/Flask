# realizzzare sito web che restituisca la mappa dei quartieri di milano
# ci deve essere una homepage con un link "quartieri di milano" :
# cliccando su quaesto link si deve visuallizare la mappa dei quartieri di milano


import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import contextily
import geopandas as gpd
import io
from flask import Flask, render_template, send_file, make_response, url_for, Response,request
app = Flask(__name__)

matplotlib.use('Agg')


matplotlib.use('Agg')


quartieri = gpd.read_file(
    '/workspace/Flask/ds964_nil_wm (1)-20220322T111443Z-001.zip')


fontanelle = gpd.read_file('/workspace/Flask/Fontanelle-20220328T183849Z-001.zip')


@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html')


@app.route('/visualizza.png', methods=['GET'])
def quartieri1():

    fig, ax = plt.subplots(figsize=(12, 8))

    quartieri.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor='k')
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/visualizza', methods=("POST", "GET"))
def mpl():
    return render_template('visualizza.html',
                           PageTitle="Matplotlib")




@app.route('/form_ricerca', methods=['GET'])
def ricerca_quartiere():
    return render_template('form_ricerca.html') 



@app.route('/ricerca.png', methods=['GET'])
def ricerca_quart():
    
    fig, ax = plt.subplots(figsize=(12, 8))

    quartiere.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor='k')
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/ricerca', methods=("POST", "GET"))
def cerca():
    global quartiere
    ricerca = request.args["Quartiere"]
    quartiere = quartieri[quartieri["NIL"].str.contains(ricerca.upper())]

    return render_template('plot2.html',
                       PageTitle="Matplotlib")

@app.route('/risultato', methods=("POST", "GET"))
def mp():
    global imgUtente

    qrt = request.args['quartiere']
    imgUtente = quartieri[quartieri['NIL']==qrt]

    return render_template('risultato.html',PageTitle = "Matplotlib",quartiere=qrt)


@app.route('/scelta', methods=['GET'])
def scelte():
    qrt = quartieri.NIL.to_list()
    qrt.sort()
    return render_template('scelta.html',PageTitle = "Matplotlib",quartieri=qrt)



@app.route("/fontanelle", methods=["GET"])
def fontanelle1():
    return render_template("fontanelle.html", quartieri= quartieri["NIL"])



@app.route('/fontanelleres', methods=("POST", "GET"))
def fontanelleRes():
    global imgUtente, fontQuart
    
    quartiereUtente = request.args["Quartiere"]
    imgUtente = quartieri[quartieri["NIL"] == quartiereUtente]
    fontQuart = fontanelle[fontanelle.within(imgUtente.geometry.squeeze())]
    print(fontQuart)
    return render_template('fontanelleRes.html', PageTitle = "Matplotlib", quartiere=quartiereUtente, tabella = fontQuart.to_html())

@app.route("/fontanelle.png", methods=["GET"])
def Fontanelle():
    fig, ax = plt.subplots(figsize = (12,8))

    imgUtente.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor="k")
    fontQuart.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor="k")
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')















if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
