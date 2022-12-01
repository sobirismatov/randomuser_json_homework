from from_json import read_json

def count_users(data:dict)->int:
    """Counts the number of users in the data

    Args:
        data (dict): The data from the JSON file

    Returns:
        int: The number of users
    """
    # Count the number of users
    dic=data["users"]
    return len(dic)
data=read_json("users.json")

print(count_users(data)) 
