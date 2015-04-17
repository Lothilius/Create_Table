__author__ = 'Lothilius'

import csv
import re
import numpy as np



# Pull top two rows from CSV file
def array_from_file(filename):
    """Given an external file containing data,
            create an array from the data.
            The assumption is the top row contains column
            titles."""
    data_array = []
    with open(filename, 'rU') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            data_array.append(row)

    data_array = np.array(data_array)
    return data_array

# Clean up the Data so that the column names are mysql friendly.
def clean_name(the_name):
    # Replace spaces with underscores.
    the_name = the_name.replace(' ', '_')

    # Remove non alpha characters
    regex = re.compile('[^a-zA-Z_]')
    the_name = regex.sub('', the_name)

    return the_name

# Get Max Length for values in a column
def max_length(column):
    the_max_length = len(max(column, key=len))
    item = max(column, key=len)
    return the_max_length, item


# Analyze data row for type
def create_type_array(array, file_name):
    type_list = ['CREATE TABLE ' + clean_name(file_name).capitalize() + '( key_id INT NOT NULL AUTO_INCREMENT, ']

    for i in range(0, len(array[0])):
        length, item = max_length(array[1::, i])

        if item.isdigit():
            type_list.append(clean_name(array[0][i]) + ' INT DEFAULT NULL, ')
        elif item.find('-') == 4 and item.find(':') == 13 and length == 24:
            type_list.append(clean_name(array[0][i]) + ' DATE DEFAULT NULL, ')
        else:
            type_list.append(clean_name(array[0][i]) + ' VARCHAR(' + str(length) + ') DEFAULT NULL, ')

    type_list.append('PRIMARY KEY (key_id));')

    return type_list


# if each.isdigit():
#            type_list.append('Integer' + ', nullable=False')
#        elif each.find('-') == 4 and each.find(':') == 13 and length == 24:
#            type_list.append('DateTime' + ', nullable=False')
#        else:
#            type_list.append('String(' + str(length) + '), nullable=False')

# 'CREATE TABLE' + file_name + '( key_id INT NOT NULL AUTO_INCREMENT,
#    -> ' + name[i] + ' VARCHAR(100) NOT NULL,
#    -> ' + tutorial_author VARCHAR(40) NOT NULL,
#    -> submission_date DATE,
#    -> 'PRIMARY KEY ( tutorial_id )
#    -> );'

