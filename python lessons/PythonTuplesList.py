#Python Lists and Tuples
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
students = "Jonh, Mary, Steve"
students = ["John","Mary","Steve"]
type students
SyntaxError: invalid syntax
type(students)
<class 'list'>
len(students)
3
students[0]
'John'
students[2]
'Steve'
students[0,1]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    students[0,1]
TypeError: list indices must be integers or slices, not tuple
students[0:1]
['John']
students[0:2]
['John', 'Mary']
students[-1]
'Steve'
students[:2]
['John', 'Mary']
months = ("January", "February", "March")
type(months)
<class 'tuple'>
months[0]
'January'
months[0,1]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    months[0,1]
TypeError: tuple indices must be integers or slices, not tuple
months[:3]
('January', 'February', 'March')
students
['John', 'Mary', 'Steve']
months
('January', 'February', 'March')
students[2] = "George"
students
['John', 'Mary', 'George']
months[0] = "new month"
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    months[0] = "new month"
TypeError: 'tuple' object does not support item assignment
students.append("Kate")
students
['John', 'Mary', 'George', 'Kate']
students.insert(0,"Peter")
students
['Peter', 'John', 'Mary', 'George', 'Kate']
students.pop(0)
'Peter'
students.pop()
'Kate'
students.remove("Mary")
students
['John', 'George']
students2 = ["Mary", "Kate"]
students + students2
['John', 'George', 'Mary', 'Kate']
