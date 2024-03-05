import pandas as pd
import numpy as np
from math import log2


def information_gain(before_test_entropy, after_test_entropy):
    return after_test_entropy - before_test_entropy

def calculate_entropy(data_frame, attribute_to_test):
    # LIST unique_attribs_results <-- Append all possible unique results of attribute e.g. 'vhigh' / 'high' / 'med' etc.
    unique_possible_attribs_results = []
    for i in range(len(df)):
        if df[attribute_to_test].iloc[i] not in unique_possible_attribs_results:
            unique_possible_attribs_results.append(df[attribute_to_test].iloc[i])
    print(unique_possible_attribs_results)

    all_attrib_results = []
    # Add all results from relevant property across all dataset to a list
    for j in range(len(df)):
        all_attrib_results.append(df[attribute_to_test].iloc[j])
    print(all_attrib_results)

    # Count 'vhigh'
    count = 0
    for j in range(len(list_of_targets)):
        if list_of_targets[j] == 'vhigh':
            count = count + 1


    # FOR LENGTH OF unique_attribs
        # P =
            # * Find count of attribute type result e.g. count how many 'vhigh' of 'buying'
            # * Find total of attribute with all results e.g. (length of dataframe)
            # * P = Divide count of attrib type resuls / total of attributes with all results
    # END FOR

    # Calculate Entropy
    # E <-- RESULT (Insert all P values into calculation)
    # RETURN E






if __name__ == "__main__":
    # Load the dataset
    df = pd.read_csv('car.csv', header=None, names=['buying', 'maint', 'doors', 'persons', 'lugboot', 'class'])
    calculate_entropy(df,'buying')
    print("END ----")
    #print(information_gain())


    list_of_targets = []
    # Extract the target variable
    for i in range(len(df)):
        list_of_targets.append(df['buying'].iloc[i])

        # Count 'vhigh'
        count = 0
        for j in range(len(list_of_targets)):
            if list_of_targets[j] == 'vhigh':
                count = count + 1

        # Count 'high'

        # Count 'med'

        # Count 'low'

    print(str(count) + " of vhigh")
    print(list_of_targets)

