from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/square/<int:a>")
def square(a):
    output = a*a
    result = {
        "Operation" : "Addition",
        "IP": "124.847.65.12",
        "Entered Number" : a,
        "Output" : output
    }
    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True)