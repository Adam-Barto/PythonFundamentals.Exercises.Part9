# ### Part A
# * Create a program called *json_helper.py*
# * Define a function called *read_json*. Given a string representing a file path to a json file,
# this function should open said file and convert its contents into a json object.
# * The json object should be returned.
import json
import os
import pickle


def read_json(path: str):
    return json.load(open(path))


#
# ### Part B
# * Define a function called *read_all_json_files*. Given a string representing a path to a directory, this function
# should read all of the json files and return a list containing all of the json objects.
# * Make sure to incorporate the work from part A.
#

def read_all_json_files(path: str):
    new_list = []
    json_file_names = [filename for filename in os.listdir(path) if filename.endswith('.json')]
    for value in json_file_names:
        new_list.append(read_json(path + '/' + value))
    return new_list


# ### Part C * Define a function called *write_pickle*. This function should take a file path and some data. Given
# these parameters, the function should write the contents of the json files to a file called
# **super_smash_characters.pickle**.
#

def write_pickle(path: str, some_data):
    pickle.dump(some_data, open(path, 'wb'))


# ### Part D
# * Define a function called *load_pickle*. Given a file path, this function opens a pickled file and returns the data.
# * Use this function to print the pickled data from Part C to the screen.

def load_pickle(path: str):
    return pickle.load(open(path, 'rb'))
