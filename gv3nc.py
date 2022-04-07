from flask import Flask, render_template, request, Response
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('scegli.html')

@app.route('/selezione', methods=['GET'])
def selezione():

    scelta = request.args['Scelta']
    if scelta == 'si' :
        return render_template('si.html')
    elif scelta == 'no':
        return render_template('no.html')
 





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)