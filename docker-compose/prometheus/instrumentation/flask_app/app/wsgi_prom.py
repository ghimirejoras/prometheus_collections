from flask import Flask, Response
from prometheus_client import Counter, generate_latest

COUNTER = Counter('app_requests', 'App Requests.')

app = Flask(__name__)
@app.route('/')
def hello():
    COUNTER.inc()
    return 'Scrappy Hello World!'

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
