# Cars Company Decision Tree Coursework
# COMP4035 Computer Science Applications - Artificial Intelligence

# Import necessary modules
import math
import pandas as pd

def get_number_of_classes(data):
    unique_classes = data['class'].value_counts()
    return len(unique_classes)
def calculate_entropy(data):
    print("Calculating entropy of data...")
    total_records = len(data)
    if total_records == 0:
        return 0





def calculate_information_gain():
    print("Calculating information gain...")


if __name__ == "__main__":
    cardata = pd.read_csv('car.csv', header=None, names=['buying', 'maint', 'doors', 'persons', 'lugboot', 'class'])
    number_of_classes = get_number_of_classes(cardata)
    print(number_of_classes)

    # Find the unique classes and count quantity
    #unique_classes = cardata['class'].unique()
    #num_classes = len(unique_classes)
    #print(f"Unique classes: {unique_classes}\nNumber of classes: {num_classes}")


    # Calculate total overall entropy