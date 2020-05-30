from flask import Flask, redirect, url_for, request, render_template, session
import requests
from flask_session import Session
import json

app = Flask(__name__, template_folder= 'Templates')

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

context_set = ""
conversation=[]
@app.route('/', methods = ['POST','GET'])
def index():
    if session.get("conversation") is None:
        session["conversation"] = []
    if request.method=='GET':
        return render_template('index.html', conversation=session["conversation"])

    if request.method == 'POST':
        val = str(request.form.get('msg'))
        session["conversation"].append("You: "+val)
        data = json.dumps({"sender": "Rasa","message": val})
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
        res = res.json()

        val = res[0]['text']
        session["conversation"].append("Bot: "+val)
        if len(res)>1:
            for i in range(1, len(res)):
                session["conversation"].append("   : "+res[i]['text'])
        return render_template('index.html', conversation=session["conversation"])

if __name__ == '__main__':
  app.run(debug=True)
