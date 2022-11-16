from flask import Flask, redirect, url_for, jsonify,render_template, request, flash
import json
import time

app = Flask(__name__)


@app.route("/", methods=["GET"])
def user():
    ts = int(time.time())
    datajson = {"message": "Automated all the things!",
                "timestamp": ts}
    json_format = json.dumps(datajson, indent=6)
    return render_template("index.html", json_format=json_format)


@app.route('/test')
def index():
    return jsonify({'hello': 'world'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
