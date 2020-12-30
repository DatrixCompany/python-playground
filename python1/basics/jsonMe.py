import json

x = '{"name": "john", "age": 30}'
y = json.loads(x)

objBeforeJson = {
    "name": 'hola', "age": 55
}
objAfterJson = json.dumps(objBeforeJson)
objAgain = json.loads(objAfterJson)

print(y)
print(objBeforeJson)
print(objAfterJson)
print(objAgain["name"])

try:
    print(g)
except:
    print("expetion")

price = 49
txt = "The price {1} is {0:.2f} dollars, {name} {2}"
print(txt.format(price, x, 'h', 'htttt', name='John'))
