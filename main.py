from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"])
def promo():
    return render_template("index.html")

@app.route('/sign_up', methods=["GET"])
def sign_up():
    return render_template("sign_up.html")

@app.route('/sign_in', methods=["GET"])
def sign_in():
    return render_template("sign_in.html")

@app.route('/email_confirmation', methods=["GET"])
def email_confirmation():
    return render_template("email_confirmation")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5500)