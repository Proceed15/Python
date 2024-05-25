'''
Codes from CMD Class Data Dictionary
Execute each one indivudual to summarize tests.
Follow the proper order when needed. 
'''
'''
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
person = ["John", "Green", "1980", "Canada"]
person = { "first_name": "John", "last_name": "Green", "birth_year": 1980, "country_of_birth": "Canada" }
type(person)
<class 'dict'>
person["first_name"]
'John'
person["birth_year"] = 1999
person
{'first_name': 'John', 'last_name': 'Green', 'birth_year': 1999, 'country_of_birth': 'Canada'}
person["birth_year"] = 1979
person
{'first_name': 'John', 'last_name': 'Green', 'birth_year': 1979, 'country_of_birth': 'Canada'}
person["marital_status"] = "Married"
person
{'first_name': 'John', 'last_name': 'Green', 'birth_year': 1979, 'country_of_birth': 'Canada', 'marital_status': 'Married'}
person["children"] = ["Nathalie", "Ethan"]
person
{'first_name': 'John', 'last_name': 'Green', 'birth_year': 1979, 'country_of_birth': 'Canada', 'marital_status': 'Married', 'children': ['Nathalie', 'Ethan']}
person["children"] = ["Anna"]
person
{'first_name': 'John', 'last_name': 'Green', 'birth_year': 1979, 'country_of_birth': 'Canada', 'marital_status': 'Married', 'children': ['Anna']}
person["children"] = ["Nathalie", "Ethan", "Anna"]
person
{'first_name': 'John', 'last_name': 'Green', 'birth_year': 1979, 'country_of_birth': 'Canada', 'marital_status': 'Married', 'children': ['Nathalie', 'Ethan', 'Anna']}
person["children"].append("Ana")
person
{'first_name': 'John', 'last_name': 'Green', 'birth_year': 1979, 'country_of_birth': 'Canada', 'marital_status': 'Married', 'children': ['Nathalie', 'Ethan', 'Anna', 'Ana']}
person["children"].pop("Ana")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    person["children"].pop("Ana")
TypeError: 'str' object cannot be interpreted as an integer
person["children"].del("Ana")
SyntaxError: invalid syntax
person["children"].Del("Ana")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    person["children"].Del("Ana")
AttributeError: 'list' object has no attribute 'Del'
person["children"].del(Ana)
SyntaxError: invalid syntax
person["children"].pop(Ana)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    person["children"].pop(Ana)
NameError: name 'Ana' is not defined. Did you mean: 'any'?
person["children"].remove("Ana")
person
{'first_name': 'John', 'last_name': 'Green', 'birth_year': 1979, 'country_of_birth': 'Canada', 'marital_status': 'Married', 'children': ['Nathalie', 'Ethan', 'Anna']}
person["age"]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    person["age"]
KeyError: 'age'
person.get("age")
person.get("age", "invalid property")
'invalid property'
person["age"]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    person["age"]
KeyError: 'age'
person.get("children", "invalid property")
['Nathalie', 'Ethan', 'Anna']
Key = "first_name"
person[Key]
'John'
person["first_name"]
'John'
person.clear()
person
{}
