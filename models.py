# models.py
from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy object which will be initialized later in app.py.
db = SQLAlchemy()

# Define a model for a simulated data transaction in our cloud database.
class DataTransaction(db.Model):
    __tablename__ = 'data_transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String(50), nullable=False)  # e.g., INSERT, UPDATE, DELETE
    data = db.Column(db.String(200), nullable=False)        # A string representation of the data
    status = db.Column(db.String(20), default='pending')      # Transaction status
    performance_metric = db.Column(db.Float, default=0.0)     # Simulated metric (e.g., execution time)

    def __repr__(self):
        return f"<DataTransaction {self.id} {self.operation}>"
