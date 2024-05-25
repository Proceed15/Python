print("Information_Oracule")

person = {"name": "Bruce", "gender": "M", "age": "42", "address": "Gotham City", "phone": "o1 56 88756-4643"}

key = input("What informarion do you want to know about the person? ").lower()

result = person.get(key, "That information is not available")

print(result)
'''
print("Information_Oracule")

person = {"fn": "Bruce", "ln": "Wayne", "age": "42", "adress": "Gotham City", "phone": "o1 56 88756-4643"}

print("What information do you want to know about this person? ")
print("Digit the number of  your choice: 1-First Name 2-Last Name 3-Age 4-Adress 5-Phone")
info = input("Number of choice: ")

index = int(info[0:1])

if 1 <= index <= 5:
    if index == 1:
        print(person["fn"])
    if index == 2:
        print(person["ln"])
    if index == 3:
        print(person["age"])
    if index == 4:
        print(person["adress"])
    if index == 5:
        print(person["phone"])
else:
    print("Invalid information provided")
'''

