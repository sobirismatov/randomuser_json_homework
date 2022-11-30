import json
def get_users(data:dict)->list:
    """Gets a list of users from the data

    Args:
        data (dict): The data from the JSON file

    Returns:
        list: A list of users
    """
    # Get the list of users
    dic= json.loads(data)
    a=[]
    a.append(dic)
    return a
f=open("users.json")
data=f.read() 
print(get_users(data))
