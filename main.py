# Cars Company Decision Tree Coursework
# COMP4035 Computer Science Applications - Artificial Intelligence

# Import necessary modules
import math
import pandas as pd
import seaborn as sns

def get_number_of_classes(data):
    """
    :param data: Dataset Pandas object with 'names' list of class names
    :return: The number of unique classes in the dataset
    """
    unique_classes = data['class'].value_counts()
    return len(unique_classes)

def calculate_probability(data, number_of_classes, attribute):
    # Return a tuple of the probabilty that it's not

    print()
    # Get

    # Calculate attribute not

def calculate_entropy(p):
    print()



def calculate_information_gain():
    print("Calculating information gain...")


if __name__ == "__main__":
    cardata = pd.read_csv('car.csv', header=None, names=['buying', 'maint', 'doors', 'persons', 'lugboot', 'class'])

    number_of_classes = get_number_of_classes(cardata)
    print(cardata['buying'].iloc[1])



    #overall_entropy = calculate_entropy(cardata)
    #print(f"Overall entropy : {overall_entropy}")


    # Find the unique classes and count quantity
    #unique_classes = cardata['class'].unique()
    #num_classes = len(unique_classes)
    #print(f"Unique classes: {unique_classes}\nNumber of classes: {num_classes}")


    # Calculate total overall entropy