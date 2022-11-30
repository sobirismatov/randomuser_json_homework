import json
def get_male_users_from_country(data:dict, country:str)->list:
    """
    Get male users from a country from the data
    Args:
        data (dict): The data from the JSON file
        country (str): The country to get users from
    Returns:

        list: A list of users
    """ 
    dic=json.loads(data)
    di= dic["users"]
    a=[]
    for i in dic:
        if i["gender"]=="mele":
            a.append(i["name"])
        return a
         
f=open("users.json")
data=f.read()
print(get_male_users_from_country(data))
    