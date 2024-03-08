from main import *

import math
import pandas as pd
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# ... (rest of your code here) ...

if __name__ == "__main__":
    # Load dataset
    print("Loading dataset ...")
    cardata = pd.read_csv('car.csv', header=None, names=['buying', 'maint', 'doors', 'persons', 'lugboot', 'class'])

    # Set all possible attributes manually into list
    attributes = ['buying', 'maint', 'doors', 'persons', 'lugboot']

    print("Building decision tree ...")
    # Build tree from root
    root = build_decision_tree(cardata, attributes)

    # --- DISPLAYING TREE ----
    print("\n*** OUTPUT DECISION TREE ***")
    # Graphically displau the tree to terminal
    output_decision_tree(root)

    # --- TESTS, ACCURACY MEASUREMENTS ---
    print("\n\n--- TESTING, ACCURACY MEASUREMENT DATA ---")
    test_cardata_sample = pd.read_csv('car.csv', header=None, names=['buying', 'maint', 'doors', 'persons', 'lugboot', 'class'])

    # Test the decision tree
    accuracy = measuring_accuracy_of_decision_tree(root, test_cardata_sample)
    print("Accuracy of model on test random sampled data : " + str(accuracy))

    # Compute true labels and predicted labels
    y_true = test_cardata_sample['class']
    y_pred = [predict_instance(root, instance) for _, instance in test_cardata_sample.iterrows()]

    # Calculate the confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix:\n", cm)

    # Plot the confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Labels")
    plt.show()