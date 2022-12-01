from from_json import read_json
data=read_json("users.json")
def get_users_older_than(data:dict, age:int)->list:
    """Gets all users older than a certain age from the data
    Args:
        data (dict): The data from the JSON file
        age (int): The age to filter users by
    Returns:
        list: A list of users
    """
    
    dic =data["users"]
    a=[]
    for i in dic:
        if age<i["age"]:
            a.append(i)
    return a


print(get_users_older_than(data,25))