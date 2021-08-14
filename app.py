from flask import Flask, render_template, jsonify
from monitor import Monitor

app = Flask(__name__)
#define new monitor
test = Monitor()

@app.route("/temperature",methods=["GET"])
def get_temperature():
    return jsonify({"temperature":test.get_temp()})

@app.route("/")
def index():
    return render_template('home.html')

if __name__ == '__main__':
    test.get_cpu_usage()
    app.run(debug=True, port=5000, host='0.0.0.0')
