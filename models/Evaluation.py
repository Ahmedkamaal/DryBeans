import numpy as np
import matplotlib.pyplot as plt


def confusion_matrix(y_true, y_pred):
    unique_classes = np.unique(y_true)
    num_classes = len(unique_classes)
    matrix = np.zeros((num_classes, num_classes), dtype=int)

    for i in range(num_classes):
        true_class = unique_classes[i]
        true_class_indices = (y_true == true_class)

        for j in range(num_classes):
            predicted_class = unique_classes[j]
            predicted_class_indices = (y_pred == predicted_class)

            matrix[i, j] = np.sum(true_class_indices & predicted_class_indices)

    return matrix


def calculate_overall_accuracy(confusion_matrix):
    # Calculate the overall accuracy using the diagonal of the confusion matrix
    overall_accuracy = np.sum(np.diag(confusion_matrix)) / np.sum(confusion_matrix)
    return overall_accuracy


def plot_decision_boundary(model, X_test, y_test, class1, class2, include_bias=True):
    plt.figure(figsize=(8, 6))
    # Scatter plot for Class 1
    plt.scatter(X_test[y_test == -1, 0], X_test[y_test == -1, 1], color='blue', label=class1)

    # Scatter plot for Class 2
    plt.scatter(X_test[y_test == 1, 0], X_test[y_test == 1, 1], color='red', label=class2)

    x1 = np.linspace(X_test[:, 0].min(), X_test[:, 0].max(), 100)
    x2 = -(model.weights[0] * x1 + model.bias) / model.weights[1]

    if x2 is not None:
        plt.plot(x1, x2, color='black', label='Decision Boundary')

    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title(f'Scatter plot with Decision Boundary for {type(model).__name__}')
    plt.legend()
    plt.grid(True)
    plt.show()
