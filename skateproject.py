from flask import Flask, render_template, request, Response
app = Flask(__name__)



@app.route("/", methods=["GET"])
def scelta():
    return render_template("scelta.html")









































if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)