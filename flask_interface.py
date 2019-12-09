import os

from retrain_AI import retrain
from test_performance import test_data
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__, template_folder='')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test_performance", methods=['POST'])
def test_input():
    if (request.method == 'POST'):
        file_name = request.form.get("path")
        print(file_name)
        falling_classification, landing_classification = test_data(file_name)
        return jsonify({
            "fallOutput": falling_classification,
            "landOutput": landing_classification
        })

@app.route("/retrain_AI", methods=['POST'])
def AI_retrain():
    if (request.method == 'POST'):
        desired_falling_output = request.form.get("falling")
        desired_landing_output = request.form.get("landing")
        file_name = request.form.get("path")
        output = retrain(file_name, desired_falling_output, desired_landing_output)
        return jsonify({ "retrain": output})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')