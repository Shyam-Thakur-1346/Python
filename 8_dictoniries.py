my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(my_dict)
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["city"])
print(my_dict.get("name"))

my_dict.update({"name":"ram"})
print(my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

print(my_dict.pop("age",25))
print(my_dict.popitem())