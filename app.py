from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template("Main template.html")

@app.route('/Tutorial1')
def Tutorial1():
    return render_template("SOEN287_A1_40132567_IsmaelRekik.html")

@app.route('/Tutorial2')
def Tutorial2():
    return render_template("Page 2.html")