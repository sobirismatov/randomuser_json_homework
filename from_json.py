import json
def read_json(filename:str) -> dict:
    """Reads a JSON file and returns the data as a dictionary

    Args:
        filename (str): The name of the JSON file
    return:
        dict: The data in the file
    """
    f=open(filename).read()
    dic= json.loads(f)
    # Read the data from the file

    # Parse the JSON data
    return dic

