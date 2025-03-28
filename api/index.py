from flask import Flask, jsonify

app = Flask(__name__)

VALID_KEYS = ["key1", "key2", "key3"]

@app.route('/api/keys', methods=['GET'])
def get_keys():
    return jsonify(VALID_KEYS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
