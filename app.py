import os
from bottle import route, run

@route('/hello/')
def hello():
    return "hello world"
    
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))