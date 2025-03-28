from flask import Flask, jsonify, request

app = Flask(__name__)

VALID_KEYS = ["key1", "key2", "key3"]

@app.route('/api/keys', methods=['GET'])
def get_keys():
    return jsonify(VALID_KEYS)

@app.route('/api/validate_key', methods=['POST'])
def validate_key():
    data = request.json
    key = data.get('key')
    
    if key in VALID_KEYS:
        return jsonify({"valid": True})
    else:
        return jsonify({"valid": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
