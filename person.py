person = {"name": "Sarah Smith", "city": "Orlando", "age": 100}

# for key, value in person.items():
#     print(key, ': ', value, sep='')

name_age = f"{person['name']} is {person['age']} years old. "
city = f"She lives in {person['city']}."
print(name_age + city, sep="")
