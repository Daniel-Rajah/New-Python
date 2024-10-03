
"""
#iterating through list

numbers = [1,2,3,4,5]

for number in numbers:
    print(number)
    if number == 2:
        print('you gay!')
        break
"""

#list version

"""
names = []
ages = []
emails = []

for i in range(2):
    print(i + 1, 'Input')
    name = input('Name: ')
    age = input('Age: ')
    email = input('Email: ')

    names.append(name)
    ages.append(age)
    emails.append(email)

print('List of names:', names,'Their ages:', ages, 'Their emails: ', emails)

"""

#dictionary version

People = []

def add_person():
    name = input('Name: ')
    age = input('Age: ')
    email = input('Email: ')
    Person = {'Name': name, 'Age': age, 'Email': email}
    return Person

print('Welcome to the HR system')
print()
instruction = input('Here you can "Add", "Delete" or "Search": ').lower()

    
if instruction == 'add':
    add_person()
elif instruction == 'Delete'

    