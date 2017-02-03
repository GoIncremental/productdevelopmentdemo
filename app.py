from flask import Flask, render_template, url_for, request, redirect
from tinydb import TinyDB, Query

app = Flask(__name__)

db = TinyDB('passengers.json')

@app.route("/")
def index():
    passenger_data = db.all()
    return render_template('index.html', passenger_data=passenger_data)

@app.route("/save_number", methods=['POST'])
def save_number():
    db.insert({'number': request.form.get('number')})
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)