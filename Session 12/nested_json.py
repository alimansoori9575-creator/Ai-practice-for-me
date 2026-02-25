import json

json_responce = '''
{
        "user": {
            "id": "101",
            "profile": {
                "name": "Ali",
                "roles": ["admin", "editor"]
        }
    }
}
'''
parsed_dict = json.loads(json_responce)
print(type(parsed_dict))

# now i want to access name 
name = parsed_dict['user']['profile']['name']
print(name)
# to access roles
roles = parsed_dict['user']['profile']['roles']
print(roles)
# to get one role here are two method
# 1
for i in roles:
    print(i)
# 2
print(roles[0])
print(roles[1])