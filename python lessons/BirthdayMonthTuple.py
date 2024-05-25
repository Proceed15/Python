print("Birthday Month Finder")

Months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

BirthDate = input("Please provide your birth date with numbers in the format of DD-MM-YYYY: ").replace('-', '_')

# Extract the month part from the input
BirthMonth = int(BirthDate[3:5])

if 1 <= BirthMonth <= 12:
    print("Valid Information Provided")
    print("You were born in", Months[BirthMonth - 1], "(", BirthMonth, ")")
else:
    print("Invalid Information Provided")

'''
Video Code:
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
birthday = input("Type your birthday in the format DD-MM-YYYY: ")

index = int(birthday[3:5]) - 1
bd_month = months[index]

print("You were born in", bd month)
'''

'''
Code Done:
print("Birthday Month Finder")

Months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

BirthDate = input("Please provide your birth date with numbers in the format of DD-MM-YYYY: ").replace('-', '_')

# Extract the month part from the input
BirthMonth = int(BirthDate[3:5])

if 1 <= BirthMonth <= 12:
    print("Valid Information Provided")
    print("You were born in", Months[BirthMonth - 1], "(", BirthMonth, ")")
else:
    print("Invalid Information Provided")

'''
