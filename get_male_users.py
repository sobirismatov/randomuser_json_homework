import json
def get_male_users(data:dict)->list:
    """Gets all male users from the data
    Args:
        data (dict): The data from the JSON file
    Returns:
        list: A list of users
    """
    dic=json.loads(data)
    dic=dic["users"]
    a=[]
    for i in dic:
        if i["gender"]=="male":
            a.append(i)
    return a
f=open("users.json")
data=f.read()
print(get_male_users(data))