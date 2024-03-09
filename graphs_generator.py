# Import all functions created in the main program - main.py
from main import *

# Import necessary libraries
import pandas as pd
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Load dataset
    print("Loading dataset ...")
    cardata = pd.read_csv('car.csv', header=None, names=['buying', 'maint', 'doors', 'persons', 'lugboot', 'class'])

    # Set all possible attributes manually into list
    attributes = ['buying', 'maint', 'doors', 'persons', 'lugboot']

    print("Building decision tree ...")
    # Build tree from root
    root = build_decision_tree(cardata, attributes)

    # Load test dataset from random sampling of main dataset
    test_cardata_sample = pd.read_csv('car.csv', header=None, names=['buying', 'maint', 'doors', 'persons', 'lugboot', 'class'])

    # Compute 'true' labels and predicted labels
    # Collect actual test data sample class values
    y_true = test_cardata_sample['class']
    y_pred = []
    for _, instance in test_cardata_sample.iterrows():
        # Iterate over instances in test data and create collection of predictions
        prediction = predict_instance(root, instance)
        y_pred.append(prediction)

    # Calculate the confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix for Decision Tree:\n", cm)

    # Plot the confusion matrix graphically
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
    plt.title("Confusion Matrix for Decision Tree")
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Labels")
    plt.show()