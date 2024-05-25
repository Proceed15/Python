myString = "PT"
len(myString)
2
myString = "PT1000098984"
len(myString)
12
myString[0:2]
'PT'
myString[2:12]
'1000098984'
myString = "1000098984PT"
myString[-2:-1]
'P'
myString[-2:0]
''
myString[-2:-2]
''
myString[-2:12]
'PT'
myString[-2:]
'PT'
myString[:3]
'100'
"Hello" + " " + "World"
'Hello World'
"Hello" + 1234
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    "Hello" + 1234
TypeError: can only concatenate str (not "int") to str
"Hello" + "1234"
'Hello1234'
"user" + str(22)
//Basic cmd commands with strings followed by their respectives results.
