import json
def get_users_younger_than(data:dict, age:int)->list:
    """Gets all users younger than a certain age from the data
    Args:
        data (dict): The data from the JSON file
        age (int): The age to filter users by
    Returns:
        list: A list of users
    """
    dic =json.loads(data)
    dic =dic["users"]
    a=[]
    for i in dic:
        if age>i["age"]:
            a.append(i)
    return a

f=open("users.json")
data=f.read()
print(get_users_younger_than(data,25))
    