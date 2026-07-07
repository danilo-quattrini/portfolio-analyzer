import re
""" 
Read a file and return the data contained in it

:return: str or exception if the file doesn't exists
"""
def file_data(file_name):
    with open(file_name, 'r') as file:
        return file.read()

""" 
Split data string following a specific regex, from the re module
"""
def split_data(data, regex):
    return [cleaned_data.strip() for cleaned_data in re.split(regex, data)]

""" 
Split a list of elements into different chunks.

:param lst: the list to split
:param element_to_group: the number of element to include in the splitted chunk
"""
def split_list(lst, element_to_group):
    return [lst[i:i+element_to_group] for i in range(0, len(lst), element_to_group)]

""" 
Clean a string of data removing the unnecessary element from the string

:param data: the data string to be cleaned
"""
def data_cleaner(data):
    raw_data_list = split_data(data, r'[:,\n\s]+')
    splitted_list = split_list(raw_data_list, 2)
    
    return [clean_data for clean_data in splitted_list if len(clean_data) == 2]

""" 
Take a string of raw data to clean and return a list of cleaned data separated
"""
def clean_data():
    data = file_data('data.txt')
    return data_cleaner(data)
