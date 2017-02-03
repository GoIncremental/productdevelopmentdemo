import os
from flask import Flask, render_template, url_for, request, redirect
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
from twilio.rest import TwilioRestClient


account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
sms_number = '447400029698'
client = TwilioRestClient(account_sid, auth_token)

app = Flask(__name__)

db = TinyDB(storage=MemoryStorage)

@app.route("/")
def index():
    passenger_data = db.all()
    return render_template('index.html', passenger_data=passenger_data)

@app.route("/save_number", methods=['POST'])
def save_number():
    db.insert({'number': request.form.get('number'), 
               'first_name': request.form.get('first_name')})
    return redirect(url_for('index'))

@app.route("/send_sms", methods=['GET'])
def send_sms():
    passenger_data = db.all()
    for passenger in passenger_data:
        message = client.messages.create(to=passenger.get('number'), 
                                         from_=sms_number,
                                         body="{} - Hurry !! Gate now closing for BA0057.".format(passenger.get('first_name')))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=int(os.getenv("PORT")))