# realizzzare sito web che restituisca la mappa dei quartieri di milano
# ci deve essere una homepage con un link "quartieri di milano" :
# cliccando su quaesto link si deve visuallizare la mappa dei quartieri di milano


from flask import Flask, render_template, send_file, make_response, url_for, Response
app = Flask(__name__)

import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


matplotlib.use('Agg')


quartieri = gpd.read_file('/workspace/Flask/ds964_nil_wm (1)-20220322T111443Z-001.zip')


@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html')




@app.route('/quartieri.png', methods=['GET'])
def quartieri1():

    fig, ax = plt.subplots(figsize = (12,8))

    quartieri.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/quartieri', methods=("POST", "GET"))
def mpl():
    return render_template('quartieri2.html',
                           PageTitle = "Matplotlib")


@app.route('/cerca', methods=['GET'])
def cerca1():
    return render_template('cerca.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
