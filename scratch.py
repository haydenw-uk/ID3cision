import pandas as pd
import numpy as np
from math import log2

# Load the dataset
df = pd.read_csv('car.csv', header=None, names=['buying', 'maint', 'doors', 'persons', 'lugboot', 'class'])


def calculate_entropy(df, attribute):
    print()
    # Find probability
    # * Find count of attribute type result e.g. count how many 'vhigh' of 'buying'
    # * Find total

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

if __name__ == "__main__":
    print();