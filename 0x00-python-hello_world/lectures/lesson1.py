# This program says hello and asks for my name.

yourName = input()

print("The user name is ", yourName)
print('It is good to meet you,' + yourName)

print('The length of your name is:') 
 
print(len(yourName))
print('What is your age?') # ask for their
myAge = input()

print('You will be ' + str(int(myAge) + 1) + ' in a year.')
