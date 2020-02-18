import json

f = open("path.json", "r")
x = f.read()
y = json.loads(x)
print(y["age"])
