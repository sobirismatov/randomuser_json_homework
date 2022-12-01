from from_json import read_json
data=read_json("users.json")
def get_users_from_country(data:dict, country:str)->list:
    """Gets all users from a country from the data
    Args:
        data (dict): The data from the JSON file
        country (str): The country to get users from
    Returns:
        list: A list of users
    """

    dic=data["users"]
    a=[]
    for i in dic:
        if country == i["country"]:
            a.append(i)
    return a

print(get_users_from_country(data,"USA"))