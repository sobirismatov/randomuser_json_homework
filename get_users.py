from from_json import read_json
data=read_json("users.json")
def get_users(data:dict)->list:
    """Gets a list of users from the data

    Args:
        data (dict): The data from the JSON file

    Returns:
        list: A list of users
    """
    # Get the list of users
    
    a=[]
    a.append(data)
    return a

print(get_users(data))
