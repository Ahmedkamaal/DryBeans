# # Separate data for each class
# data_class1 = data[data['Class'] == class1]
# data_class2 = data[data['Class'] == class2]
#
# # Randomly shuffle the data for each class
# data_class1 = data_class1.sample(frac=1, random_state=0)
# data_class2 = data_class2.sample(frac=1, random_state=0)
#
# # Split the data into train and test sets for each class
# train_class1 = data_class1.iloc[:30]
# test_class1 = data_class1.iloc[30:50]
# train_class2 = data_class2.iloc[:30]
# test_class2 = data_class2.iloc[30:50]
#
# # Concatenate the train and test data for both classes
# train_data = pd.concat([train_class1, train_class2])
# test_data = pd.concat([test_class1, test_class2])
#
# # Extract features and labels
# X_train = train_data[['MinorAxisLength', 'MajorAxisLength']].values
# y_train = train_data['Class'].values
# X_test = test_data[['MinorAxisLength', 'MajorAxisLength']].values
# y_test = test_data['Class'].values
#
# # Encode the class labels
# y_train = label.transform(y_train)
# y_test = label.transform(y_test)

