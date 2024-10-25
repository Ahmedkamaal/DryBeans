import numpy as np


class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=100, include_bias=False):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.bias = 0
        self.threshold = -1
        self.weights = None
        self.include_bias = include_bias

    def initialize_weights(self, no_features):
        np.random.seed(42)
        self.weights = np.random.randn(no_features)
        if self.include_bias:
            self.bias = np.random.rand()

    def signum_activation(self, X):
        return np.dot(X, self.weights) + self.bias

    def predict(self, X):
        return np.where(self.signum_activation(X) >= 0.0, 1, -1)

    def train(self, X, Y):
        self.initialize_weights(X.shape[1])
        np.random.seed(42)
        for _ in range(self.n_iterations):
            prediction = self.predict(X)
            error = Y - prediction
            self.weights += self.learning_rate * np.dot(X.T, error)
            if self.include_bias:
                self.bias += self.learning_rate * np.sum(error)
            mse = 0.5 * np.sum(pow(error, 2))
            if mse < self.threshold:
                break
