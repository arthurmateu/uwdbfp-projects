import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        entry_content = request.form.get("content")
        print(entry_content, datetime.datetime.today().strftime("%d/%m/%Y"))
    return render_template("home.html")
