import json


def read_json(filename:str) -> dict:
    """Reads a JSON file and returns the data as a dictionary

    Args:
        filename (str): The name of the JSON file
    return:
        dict: The data in the file
    """
    dic= json.loads(filename)
    # Read the data from the file

    # Parse the JSON data
    return dic
f=open("users.json")
filename=f.read() 
print(read_json(filename))