from flask import Flask, jsonify, request
app = Flask(__name__)
balance = 100.0
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the Simple Banking API!",
        "endpoints": {
            "check_balance": "/balance [GET]",
            "deposit": "/deposit [POST]"
        }
    })
@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify({"balance": balance})
@app.route('/deposit', methods=['POST'])
def deposit_money():
    global balance
    data = request.get_json() or {}
    amount = data.get("amount", 0)
    if amount <= 0:
        return jsonify({"error": "Invalid deposit amount"}), 400
    balance += amount
    return jsonify({"message": f"Deposited ${amount} successfully", "new_balance": balance})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

