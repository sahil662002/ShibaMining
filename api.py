from flask import Flask, jsonify, request

from database_v2 import (
    get_balance,
    get_mining,
    start_mining,
    claim_mining,
    add_user,
)

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "project": "Shiba Mining API",
        "version": "1.0"
    })


@app.route("/balance/<int:user_id>")
def balance(user_id):
    return jsonify({
        "user_id": user_id,
        "balance": get_balance(user_id)
    })

@app.route("/start_mining", methods=["POST"])
def api_start_mining():

    data = request.get_json()

    user_id = data["user_id"]

    start_mining(user_id)

    return jsonify({
        "success": True,
        "message": "Mining Started"
    })

@app.route("/mining/<int:user_id>")
def mining(user_id):

    mining = get_mining(user_id)

    if not mining:
        return jsonify({
            "active": False
        })

    return jsonify({
        "active": True,
        "user_id": mining["user_id"],
        "start_time": mining["start_time"],
        "end_time": mining["end_time"],
        "reward": mining["reward"],
        "claimed": mining["claimed"]
    })

@app.route("/claim", methods=["POST"])
def api_claim():

    data = request.get_json()

    user_id = data["user_id"]

    success = claim_mining(user_id)

    if success:
        return jsonify({
            "success": True,
            "message": "Reward Claimed"
        })

    return jsonify({
        "success": False,
        "message": "Mining not finished or already claimed"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
