from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    return jsonify({"received": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
