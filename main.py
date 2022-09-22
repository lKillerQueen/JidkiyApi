from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    now = datetime.now().strftime('%S')
    hitler = ''
    if int(now) % 2 == 0:
        hitler = 'четное'
    else:
        hitler = 'нечетное'
    response = app.make_response('')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.status_code = 418
    return response


app.run()