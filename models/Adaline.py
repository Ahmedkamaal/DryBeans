import numpy as np


class Adaline:
    def __init__(self, learning_rate=0.001, epochs=200, include_bias=False):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0
        self.threshold = -1
        self.include_bias = include_bias

    def train(self, X, y):
        num_features = X.shape[1]
        np.random.seed(42)
        self.weights = np.random.randn(num_features)
        if self.include_bias:
            self.bias = np.random.randn()

        for _ in range(self.epochs):
            output = self.activation(self.net_input(X))
            error = y - output
            self.weights += self.learning_rate * np.dot(X.T, error)
            if self.include_bias:
                self.bias += self.learning_rate * np.sum(error)
            mse = 0.5*np.sum(pow(error, 2))
            if mse < self.threshold:
                break

    def net_input(self, X):
        return np.dot(X, self.weights) + self.bias

    def activation(self, X):
        return X

    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)