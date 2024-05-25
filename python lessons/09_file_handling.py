f = open("test2.txt","a")

#"test.txt", "r" for read or "w" for write or "a" for append or "x" to create.
#x returns an error if the file already exists on the same folder.
#To create a file in another folder use the entire path
#going with /Users/YourUser/Desktop/myfile.txt, go to the folder you want. 

f.write("\nThis text will be appended to the file")

f = open("test.txt")
print(f.read())

#f = open("/Users/José/Desktop/python lessons/test3.txt","x")
