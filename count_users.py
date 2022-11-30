import json
def count_users(data:dict)->int:
    """Counts the number of users in the data

    Args:
        data (dict): The data from the JSON file

    Returns:
        int: The number of users
    """
    # Count the number of users
    dic =json.loads(data)
    dic=dic["users"]

    return len(dic)
f=open("users.json")
data=f.read()
print(count_users(data))