x = "Hi there"

for i in range(5):
    print(i, x)

array = [1,2,3]
print(array)

mixArr = [1,"hey", True]
print(mixArr)

mixArr.append("bye")
mixArr.insert(1,10)

print(mixArr)

import json

person = {"name":"Axel", "favNum": 7}
print(person, json.dumps(person), person["name"])

if (type(person["name"]) is str):
    print("It's a string")