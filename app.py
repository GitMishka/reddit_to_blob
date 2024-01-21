from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fetch-data', methods=['POST'])
def fetch_data():
    # Placeholder for data fetching logic
    return jsonify({"message": "Data fetching started"}), 200

if __name__ == '__main__':
    app.run(debug=True)
