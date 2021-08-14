from flask import Flask, render_template, jsonify
from monitor import Monitor

app = Flask(__name__)
#define new monitor
test = Monitor()

@app.route("/temperature",methods=["GET"])
def get_temperature():
    return jsonify({"temperature":test.get_temp()})

@app.route("/memory", methods=["GET"])
def get_memory():
    mem = test.get_storage()
    return jsonify({"used":mem[0],"pct":mem[1]})

@app.route("/uptime", methods=["GET"])
def get_uptime():
    ut = test.get_cpu_usage()
    return jsonify({"uptime":ut[3],"users":ut[6]})

@app.route("/")
def index():
    return render_template('home.html', memory = test.get_total_storage())

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
