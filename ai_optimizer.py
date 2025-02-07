# ai_optimizer.py
import numpy as np
from sklearn.linear_model import LinearRegression

def train_dummy_model():
    """
    Train a simple linear regression model using simulated data.
    This dummy model 'learns' from sample performance metrics.
    """
    # Simulated training data: performance_metric vs. optimal index (simulated value)
    X = np.array([[0.5], [1.0], [1.5], [2.0], [2.5]])
    y = np.array([1, 2, 3, 4, 5])  # This is just dummy data
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_optimization(performance_metric, model=None):
    """
    Given a performance metric, predict an 'optimal' configuration value.
    If no model is provided, we train a dummy model.
    """
    if model is None:
        model = train_dummy_model()
    # Predict the optimal value based on performance_metric
    predicted_value = model.predict([[performance_metric]])
    # For demonstration, we return a string suggestion
    return f"Suggested optimization level: {predicted_value[0]:.2f}"

# Example usage (you can test this module independently):
if __name__ == "__main__":
    model = train_dummy_model()
    test_metric = 1.8
    suggestion = predict_optimization(test_metric, model)
    print(f"For a performance metric of {test_metric}, {suggestion}")
