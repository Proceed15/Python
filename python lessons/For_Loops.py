#for loops

blog_posts = ["The 10 coolest math functions in Python",
              "",
              "How to make http requests in Python",
              "A tutorial about data types in Python"]

for post in  blog_posts:
    if post == "":
        continue
    else:
        print(post)

print('-----------------------')

myString = "This is a string"

for char in myString:
    print(char)

print('-----------------------')

for x in range(0,11):
    print(x)

print('-----------------------')

person = {'Name': 'Karen Smith', 'Age': 25, 'Gender': 'Female'}

for key in person:
    print(key, ":", person[key])

print('-----------------------')

blog_posts = {"Python":
              ["The 10 coolest math functions in Python",
              "How to make http requests in Python",
              "A tutorial about data types in Python"],
              "Javascript":
              ["Namespaces in Javascript",
               "New function available in ES6"]}
for category in blog_posts:
    print("Posts about", category)
    for post in blog_posts[category]:
        print(post)
