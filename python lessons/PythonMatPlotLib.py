#Modules: matplotlib.

'''
Before using the matplotlib, first you need to install it on Windows CMD.
The commands before are just the install one.
The commands below are for the generation of a Graph.
'''

Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [1,2,3,4]
plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001BD97540F90>]
plt.show()
legend = ["January", "February", "March", "April"]
plt.xticks(x,legend)
([<matplotlib.axis.XTick object at 0x000001BD990CAF50>, <matplotlib.axis.XTick object at 0x000001BD990C8FD0>, <matplotlib.axis.XTick object at 0x000001BD990C8850>, <matplotlib.axis.XTick object at 0x000001BD99108E10>], [Text(1, 0, 'January'), Text(2, 0, 'February'), Text(3, 0, 'March'), Text(4, 0, 'April')])
plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001BD986F5A10>]
plt.show()
plt.bar(x,y)
<BarContainer object of 4 artists>
plt.ylabel("Sales in US$")
Text(0, 0.5, 'Sales in US$')
plt.title("Monthly Sales")
Text(0.5, 1.0, 'Monthly Sales')
plt.show()
