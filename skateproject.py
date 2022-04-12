from flask import Flask, render_template, request, Response
app = Flask(__name__)


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
    elif scelta == 'accesso':
        return render_template("new_account.html")


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
    return render_template("guida_ruote.html")


@app.route("/contatti", methods=["GET"])
def contatti():
    return render_template("contatti.html")

@app.route("/maps", methods=["GET"])
def maps():
    return render_template("maps.html")

@app.route("/mas", methods=["GET"])
def mas():
    return render_template("mps.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
