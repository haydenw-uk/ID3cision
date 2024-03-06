# Cars Company Decision Tree Coursework
# COMP4035 Computer Science Applications - Artificial Intelligence

# Import necessary modules
import math
import pandas as pd
#import seaborn as sns

class Node:
    def __int__(self, attribute=None, value=None, data=None, children=None):
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



def calculate_information_gain():
    print("Calculating information gain...")


if __name__ == "__main__":
    cardata = pd.read_csv('car.csv', header=None, names=['buying', 'maint', 'doors', 'persons', 'lugboot', 'class'])

    #number_of_classes = get_number_of_classes(cardata)
    #print(cardata['buying'].iloc[1])



    #overall_entropy = calculate_entropy(cardata)
    #print(f"Overall entropy : {overall_entropy}")


    # Find the unique classes and count quantity
    #unique_classes = cardata['class'].unique()
    #num_classes = len(unique_classes)
    #print(f"Unique classes: {unique_classes}\nNumber of classes: {num_classes}")


    # Calculate total overall entropy