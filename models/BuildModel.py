import pandas as pd
import warnings

warnings.filterwarnings('ignore')
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
from models.Evaluation import *
import numpy as np


class BuildModel:

    def __init__(self):
        self.data = pd.read_excel('models/Dry_Bean_Dataset.xlsx')
        self.features = []
        self.labels = []
        self.X = None
        self.y = None
        self.include_bias = False
        self.model = None
        self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None
        self.accuracy = None
        self.label_encoder = None
        self.encoding_dict = {}
        self.scaler = None

    def preprocess_data(self):
        self.print_data()
        self.handle_na()
        df_filtered = self.data[(self.data['Class'] == self.labels[0]) | (self.data['Class'] == self.labels[1])]
        self.X = df_filtered[self.features].values
        self.y = df_filtered['Class'].values

        self.y = self.y.ravel()
        self.label_encoder = LabelEncoder()
        self.y = self.label_encoder.fit_transform(self.y)
        self.y[self.y == 0] = -1

        self.scaler = StandardScaler()
        self.X = self.scaler.fit_transform(self.X)

        # if self.include_bias:
        #     self.X = np.c_[self.X, np.ones(self.X.shape[0])]

    def preprocess_x(self, df):
        df = df[self.features].values
        df = self.scaler.transform(df)
        return df


    def build(self):
        self.preprocess_data()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=40,
                                                                                stratify=self.y,
                                                                                random_state=0,
                                                                                shuffle=True)
        self.model.train(self.X_train, self.y_train)
        y_pred = self.model.predict(self.X_test)
        # Calculate accuracy
        print("Algorithm Evaluation")


        conf_matrix = confusion_matrix(self.y_test, y_pred)
        print("Confusion Matrix:")
        print(conf_matrix)

        self.accuracy = calculate_overall_accuracy(conf_matrix)
        print(f"Accuracy: {self.accuracy * 100.0:.2f}%")
        print('bias = ', self.model.bias)

    def plot(self):
        y_pred = self.model.predict(self.X_test)
        conf_matrix = confusion_matrix(self.y_test, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=[-1, 1])
        disp.plot(cmap='Blues')
        plot_decision_boundary(self.model, self.X_test, self.y_test, self.labels[0], self.labels[1],
                               include_bias=self.include_bias)

    def print_data(self):
        # print(self.data.to_string())

        print("Data Exploration")
        print(self.data.describe())
        print('\n\n')
        print(self.data.info())
        print('\n\n')
        print('Shape of data: ', self.data.shape)
        print('number of rows:', self.data.shape[0])
        print('number of columns:', self.data.shape[1])
        # print(self.data.duplicated().sum())
        print('sum of duplicated data: ', self.data.duplicated().sum())
        print(self.data.dtypes)
        print('unique in Class: ', self.data['Class'].unique())
        print(self.data['Class'].value_counts())
        print("Nulls in each column :")
        print(self.data.isnull().sum().sort_values(ascending=False))


    def handle_na(self):
        for column in self.features:
            if column in self.data.columns:
                mean = self.data[column].mean()
                self.data[column].fillna(mean, inplace=True)


# class1 = 'BOMBAY'
# class2 = 'SIRA'

# Encode the class labels


# Scale the features


# include_bias = True  # bias

# Augment the feature vectors with a constant value of 1 for the bias term if include_bias is True


# Split the dataset into train and test sets with a fixed random seed


# Adaline Algorithm
# adaline = Adaline(learning_rate=0.01, epochs=100)


# confusion_matrix


# overall_accuracy


# Plot the decision boundary and scatter plot


print("_________________________________________________")

# Perceptron Algorithm
# perceptorn = Perceptron(learning_rate=0.01, n_iterations=100)

# Plot the decision boundary and scatter plot
# plot_decision_boundary(perceptorn, X_test, y_test, class1, class2, include_bias=True)

print("_________________________________________________")
