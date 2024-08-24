contacts = {
    "number": 4,
    "students": [
        {"name": "John Holt", "email": "sara.holt@gmail.com"},
        {"name": "Dean Ford", "email": "dean.ford@gmail.com"},
        {"name": "Jeff Beck", "email": "jeff.beck@gmail.com"},
        {"name": "Nick West", "email": "nick.west@gmail.com"},
    ]
}

for student in contacts["students"]:
    print(student["email"])

