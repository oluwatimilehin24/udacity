from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route('/status')
def healthcheck():
    response = app.response_class(
               response=json.dumps({"result":"OK - healthy"}),
               status=200,
               mimetype='application/json'
    )

    ##  Log Line
    app.logger.info('Status request succesfull')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
               response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
               status=200,
               mimetype='application/json'
    )

    ##  Log Line
    app.logger.info('Metrics request succesfull')
    return response

@app.route("/")
def hello():
    ##  Log Line
    app.logger.info('Main request succesfull')
    return "Hello World!"

if __name__ == "__main__":

    ##  stream logs to app.log file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    
    app.run(host='0.0.0.0')
