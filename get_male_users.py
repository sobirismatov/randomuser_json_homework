from from_json import read_json
data=read_json("users.json")
def get_male_users(data:dict)->list:
    """Gets all male users from the data
    Args:
        data (dict): The data from the JSON file
    Returns:
        list: A list of users
    """
    dic=data["users"]
    a=[]
    for i in dic:
        if i["gender"]=="male":
            a.append(i)
    return a

print(get_male_users(data))
