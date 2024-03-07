# Cars Company Decision Tree Coursework
# COMP4035 Computer Science Applications - Artificial Intelligence

# Import necessary modules
import math
import pandas as pd
#import seaborn as sns

class Node:
    def __init__(self, attribute=None, value=None, data=None, children=None):
        self.attribute = attribute
        self.value = value
        self.data = data
        self.children = children or []

    def add_child(self, child):
        self.children.append(child)


def calculate_entropy(data):
    unique_vales = data['class'].unique()
    entropy = 0
    for value in unique_vales:
        value_count = data[data['class'] == value].shape[0]
        value_prob = value_count / data.shape[0]
        if value_prob != 0:
            entropy -= value_prob * math.log2(value_prob)
    return entropy

def calculate_information_gain(data, attribute):
    """
    Calculates the information gain for a parsed attribute using entropy.
    :param data: Parsed Dataset
    :param attribute: Given attribute to calculate information gain for
    :return: Information gain for specified attribute
    """
    original_entropy = calculate_entropy(data)
    subsets = data.groupby(attribute)
    weighted_entropy = 0
    for subset_name, subset in subsets:
        subset_prob = subset.shape[0] / data.shape[0]
        subset_entropy = calculate_entropy(subset)
        weighted_entropy += subset_prob * subset_entropy
    information_gain = original_entropy - weighted_entropy
    return information_gain

def build_decision_tree(data, attributes):
    """ Builds a decision tree based on the input data frame and attributes
    based on an implementation of the ID3 algorithm.
    :param data: DataFrame containing the instances.
    :param attributes: List of attributes to consider.
    :return: Root node of the decision tree
    """
    root = None

    if not data.empty:
        # Check if all instances belong to the same class
        unique_classes = data['class'].unique()
        if len(unique_classes) == 1:
            # Create a leaf node with the class value
            root = Node(data=data)
        else:
            # Calculate the information gain for each attribute
            information_gains = []
            for attr in attributes:
                information_gains.append(calculate_information_gain(data, attr))

            # if there are attributes left to split on
            if information_gains:
                # Select attribute with max information gain out of remainder of the data
                best_attribute = attributes[information_gains.index(max(information_gains))]

                # Create the root note with best to use attribute
                root = Node(attribute=best_attribute)

                # Split data based on the values of the best attribute
                subsets = data.groupby(best_attribute)

                # Create the child nodes for each of the subsets
                for subset_name, subset in subsets:
                    filtered_attributes = []
                    for attr in attributes:
                        if attr != best_attribute:
                            filtered_attributes.append(attr)
                    child = build_decision_tree(subset.drop(best_attribute, axis=1), filtered_attributes)
                    child.value = subset_name
                    root.add_child(child)
            else:
                # If there are no further attributes to split on, now create a
                # leaf node with the class which has the majority
                class_with_majority = data['class'].mode()[0]
                root = Node(data=data[data['class'] == class_with_majority])

    return root

def output_decision_tree(node, level=0):
    """ Prints the output decision tree in a formatted manner for a user to view.
    :param node: The root node of the tree to ensure the entire tree can be output
    :param level: The entry-level of the tree to ensure the whole tree can be output
    """
    # Indents using tabs size multiplied by level to show clear visual difference in nodes of tree
    indent = "\t" * level
    if node:
        if node.attribute:
            print(str(indent) + "Attribute: " + str(node.attribute))
        else:
            print(str(indent) + "Class: " + str(node.data['class'].unique()[0]))
        for child in node.children:
            print(str(indent) + "Value: " + str(child.value))
            next_level = level + 1
            output_decision_tree(child, next_level)

if __name__ == "__main__":
    # Load dataset
    cardata = pd.read_csv('car.csv', header=None, names=['buying', 'maint', 'doors', 'persons', 'lugboot', 'class'])

    # Set all possible attributes manually into list
    attributes = ['buying', 'maint', 'doors', 'persons', 'lugboot']

    # Build tree from root
    root = build_decision_tree(cardata, attributes)

    # Graphically
    output_decision_tree(root)