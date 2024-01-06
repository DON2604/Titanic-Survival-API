from flask import Flask, jsonify
from training import learn

app = Flask(__name__)

@app.route("/predict/<float:a>/<float:b>/<float:c>/<float:d>")
def calculate_sum(a,b,c,d):
    result = learn(a, b, c, d)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

