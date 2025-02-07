# simulation.py
import random
import requests
import json
from ai_optimizer import predict_optimization

# URL of the running Flask app. Change the port if needed.
BASE_URL = "http://127.0.0.1:5000"

def simulate_transaction():
    """
    Simulate a random data transaction and post it to the Flask app.
    """
    operations = ["INSERT", "UPDATE", "DELETE"]
    # Create random performance metric between 0.5 and 3.0
    performance_metric = round(random.uniform(0.5, 3.0), 2)
    
    # Dummy data for simulation
    data_payload = {
        "operation": random.choice(operations),
        "data": f"Simulated data {random.randint(1000, 9999)}",
        "performance_metric": performance_metric
    }
    
    try:
        response = requests.post(f"{BASE_URL}/transaction", json=data_payload)
        if response.status_code == 201:
            print(f"Transaction added: {data_payload}")
            # Use our AI module to get a suggestion for optimization based on performance_metric
            suggestion = predict_optimization(performance_metric)
            print(f"AI Optimization Suggestion: {suggestion}")
        else:
            print(f"Error: {response.json().get('error')}")
    except Exception as e:
        print(f"Request failed: {e}")

def run_simulation(n=5):
    """
    Run the simulation for n transactions.
    """
    print("Starting workload simulation...")
    for i in range(n):
        simulate_transaction()

if __name__ == "__main__":
    run_simulation(5)
