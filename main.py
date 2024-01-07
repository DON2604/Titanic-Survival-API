from flask import Flask, jsonify
from training import learn

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
        <p>🚀 Welcome to the Titanic Survival Prediction 🛳️ API! Make predictions by sending a GET request to the <code>/predict</code> endpoint with the required parameters. Here's an example:</p>
        <p>🔗 Example: <a href="http://127.0.0.1:8000/predict/1.0/1.0/25.0/50.0">http://127.0.0.1:8000/predict/1.0/1.0/25.0/50.0</a></p>
        <p>📊 The parameters <code>a</code>, <code>b</code>, <code>c</code>, and <code>d</code> should be float values.</p>
    '''

@app.route("/predict/<float:a>/<float:b>/<float:c>/<float:d>")
def predict(a, b, c, d):
    try:
        result = learn(a, b, c, d)
        return jsonify(result)
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide valid float values for parameters."})

if __name__ == "__main__":
    app.run(debug=True)
