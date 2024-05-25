#08_Functions
'''
def say_hello(person):
    print("Hello " + person + ", how are you doing?")

say_hello("Mary")
say_hello("Paul")
say_hello("Kate")
'''
'''
def fahr2celsius(fahr):
    celsius = (5 * (fahr - 32)) / 9
    return celsius

print("Celsius: ", round(fahr2celsius(100),2))
print("Kelvin: ", round(fahr2celsius(100) + 273.5 ,2))
'''

def say_hello(person1, person2="The director"):
    print("Hello " + person1 + ", how are you doing? " + person2 + " is waiting for you.")

'''say_hello("Jane", "Tim")'''
    
say_hello("Jane")
