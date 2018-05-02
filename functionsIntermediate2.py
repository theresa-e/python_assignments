# Part 1:

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def printStudents ():
    for i in students:
        print(i["first_name"] + " " + i["last_name"])

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def usersPrint():
    for i in users:
        print (i)
        for j in range(0, len(users[i])):
            firstNames = users[i][j]['first_name']
            lastNames = users[i][j]['last_name']
            nameLength = len(firstNames) + len(lastNames)
            print (f"{j+1} - {firstNames} {lastNames} - {nameLength}")
