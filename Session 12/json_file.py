import json
data = {
    'name': "Ali",
    'age': '21'
}
json_string = json.dumps(data)

# to write json into a file named config.json
with open("config.json", "w") as f:
    json.dump(data, f)
