import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
@app.route('/saveEmails',methods=['POST'])
def saveEmails():
    if request.method == 'POST':
        emails = request.form['emails']
        response= jsonify(emails)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/testing',methods=['GET'])
def testing():
    response = flask.jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
app.run()