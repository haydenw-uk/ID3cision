# Cars Company Decision Tree Coursework
# COMP4035 Computer Science Applications - Artificial Intelligence

# Import necessary modules
import math
import pandas as pd


# import seaborn as sns

class Node:
    def __init__(self, attribute=None, value=None, data=None, children=None):
        """
        Constructor for Node class.
        Note: by default, the constructor needs no arguments (other than self)
        because the node object could be different type of node e.g. root, child, leaf...

        :param attribute: attribute name (if applicable)
        :param value: value (if applicable)
        :param data: (sub)dataset (if applicable)
        :param children: children of node (if applicable)
        """
        self.attribute = attribute
        self.value = value
        self.data = data
        self.children = children or []

    def add_child(self, child):
        """
        Adds a new child node to the tree.
        :param child: spliced subset of dataset
        """
        self.children.append(child)


def calculate_entropy(data):
    """
    Calculates entropy for data
    :param data: parsed in dataset
    :return: calculated entropy
    """
    # Find and save unique classes for dataset
    unique_vales = data['class'].unique()
    # Ensures default value of entropy for dataset
    entropy = 0
    # Iterate over every class in dataset
    for value in unique_vales:
        # Counts occurrences of 'value' in class of data
        value_count = data[data['class'] == value].shape[0]
        # Calculates probability of value
        # occurrence out of total dataset count
        value_prob = value_count / data.shape[0]
        # Check entropy not equal to 0
        # 0 entropy means dataset is in order, return immediately
        if value_prob != 0:
            # Calculates entropy based on formula
            entropy -= value_prob * math.log2(value_prob)
    return entropy


def calculate_information_gain(data, attribute):
    """
    Calculates the information gain for a parsed attribute using entropy.
    :param data: Parsed Dataset
    :param attribute: Given attribute to calculate information gain for
    :return: Information gain for specified attribute
    """
    # Calcualte original entropy of dataset
    original_entropy = calculate_entropy(data)
    # Find all subsets of dataset by attribute
    subsets = data.groupby(attribute)
    weighted_entropy = 0
    # Iterate over each subset
    for subset_name, subset in subsets:
        # Calculate current subset's probability
        # by dividing number of instances in subset by total number of instances in total dataset
        subset_prob = subset.shape[0] / data.shape[0]
        # Calculate entropy for subset by calling function
        subset_entropy = calculate_entropy(subset)
        # Sum cumulative entropies correctly (weighted entropy)
        weighted_entropy += subset_prob * subset_entropy
    # Calculate information gain as difference in entropies
    information_gain = original_entropy - weighted_entropy
    # Return information gain
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

def predict_instance(tree, instance):
    """ Predicts the class of an instance using a tree structure.
    :param tree: The root node of the tree
    :param instance: The input instance to predict
    :return: The predicted class of the instance
    """
    current_node = tree
    child_node = None

    while current_node.children:
        instance_value = instance[current_node.attribute]

        for child in current_node.children:
            if child.value == instance_value:
                child_node = child
                break

        if child_node:
            current_node = child_node
        else:
            break

    return current_node.data['class'].mode()[0]


def measuring_accuracy_of_decision_tree(tree, test_data):
    correct_predictions = 0

    for index, instance in test_data.iterrows():
        prediction = predict_instance(tree, instance)
        if prediction == instance['class']:
            correct_predictions += 1

    accuracy = correct_predictions / test_data.shape[0]
    return accuracy


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
    print("Accuracy of dataset : " + str(accuracy))
