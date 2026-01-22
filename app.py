from flask import Flask, request, jsonify
from database import create_table, connect_db

app = Flask(__name__)

create_table()

@app.route("/add", methods=["POST"])
def add_transaction():
    data = request.get_json()
    transaction_type = data.get("type")
    amount = data.get("amount")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (type, amount) VALUES (?, ?)",
        (transaction_type, amount)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Transaction added successfully"})

@app.route("/transactions", methods=["GET"])
def get_transactions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)

