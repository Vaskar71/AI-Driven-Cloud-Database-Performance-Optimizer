# app.py
from flask import Flask, request, jsonify
from config import Config
from models import db, DataTransaction

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy with the app instance
db.init_app(app)

# Create the database tables (if they do not exist)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "Welcome to the AI-Based Cloud Database Management System!"

# Route to add a new data transaction.
@app.route('/transaction', methods=['POST'])
def add_transaction():
    """
    Expected JSON payload:
    {
        "operation": "INSERT/UPDATE/DELETE",
        "data": "Sample data text",
        "performance_metric": 1.23  // Optional metric for simulation
    }
    """
    data = request.get_json()
    if not data or "operation" not in data or "data" not in data:
        return jsonify({"error": "Invalid payload. 'operation' and 'data' fields are required."}), 400

    # Create a new DataTransaction object.
    transaction = DataTransaction(
        operation=data["operation"],
        data=data["data"],
        performance_metric=data.get("performance_metric", 0.0)
    )
    try:
        db.session.add(transaction)
        db.session.commit()
    except Exception as e:
        # Rollback in case of error.
        db.session.rollback()
        return jsonify({"error": f"Database error: {str(e)}"}), 500

    return jsonify({"message": "Transaction added successfully.", "id": transaction.id}), 201

# Route to view all transactions.
@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = DataTransaction.query.all()
    result = []
    for tx in transactions:
        result.append({
            "id": tx.id,
            "operation": tx.operation,
            "data": tx.data,
            "status": tx.status,
            "performance_metric": tx.performance_metric
        })
    return jsonify(result), 200

if __name__ == '__main__':
    # Run the Flask application.
    app.run(debug=True)
