from flask import Flask, render_template
from monitor import Monitor

app = Flask(__name__)
#define new monitor
test = Monitor()


@app.route("/")
def index():
    return render_template('home.html', temperature = test.get_temp())

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
