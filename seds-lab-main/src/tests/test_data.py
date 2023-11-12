import csv
import pytest
from ..models.row_2_list import *


dataset = []
with open('../data/house_price.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        dataset.append(row)



# Test if the function correctly handles rows with missing values
# Parametrize the test function to iterate through each row in the dataset
@pytest.mark.parametrize("input_row", dataset)
def test_row_to_list_with_missing_values(input_row):
    input_string = ';'.join(input_row)  # Convert list to string using semicolons
    x = row_to_list(input_string)
    assert ' ' not in x, f"Missing value found in input: {input_row}"