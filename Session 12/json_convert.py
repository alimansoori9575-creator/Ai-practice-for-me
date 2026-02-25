import json

responce = '''
{
"name":"ali",
"age": "21",
"status": "pass"
}
'''
print(type(responce))
parsed = json.loads(responce)
print(parsed['age'])