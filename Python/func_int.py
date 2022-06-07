

1. x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]= 15
print(x[1][0])
print (x)

students[0]['last_name'] = 'Bryant'
print (students[0]['last_name'])
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0]
)

z = [ {'x': 10, 'y':20}]
z[0]['y'] = 30
print(z[0]['y'])
print (z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


 2.     def iterateDictionary(listParam): 
        for student in listParam:
            print(student ['first_name'], student ['last_name'])

            # (notes)- remember that if you want them right next to each other they have to be in the same parenthesis shown above which makes "Micheal Jordan"


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Micheal', 'Amy', 'Eduardo', 'Josh', 'Graham','Patrick', 'Minh', 'Devon']
}


def printInfo(param):
    print(len(param['location']), 'LOCATIONS')
    for location in param['locations']:
        print(location)


def printInfo(param):
    print(len(param['instructors']), 'INSTRUCTORS')
    for location in param['instructors']:
        print(location)

# 3.And iterateDictionary2('last_name', students) should output:


3. def iterateDictionary2('first_name', students)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

 4. def printInfo(students):

def printInfo(some_dict):    
    print(len(some_dict['locations']), "LOCATIONS")    
    for location in some_dict['locations':         print(location)    
    print()    
    print(len(some_dict['instructors']), "INSTRUCTORS")    
    for location in some_dict['instructors']:        print(location) sanjose = {    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon'] } 
    printInfo(sanjose) 




