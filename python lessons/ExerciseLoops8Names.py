#Exercise: Loops First One - 8 names

import random
print("Person Picker 3000")

persons = []
x = 1

while x < 9:
    person = input("Type the name of a person: ")
    persons.append(person)
    x += 1

aperson = random.choice(persons)

print("Here is one person of your list:", aperson)

'''
#Video code:
import random
people = []

for x in range(0, 8):
    person = input("Type the name of a person: ")
    people.append(person)

index = random.randint(0,7)

random_person = people[index]

print("Picking a random person: ", random_person)
'''
