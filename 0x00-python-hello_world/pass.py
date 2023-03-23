# name = input("What is your name: ")





# if name == 'Mary':
#     print('Hello Mary') 
#     password = input("Type your password: ")    
#     if password == 'swordfish':
#        print('Access granted.') 
#     else:
#         print('Wrong password.')
# else: 
#     print ( "you dont have access")
  
# orname = "Alice"  
# name = input("Please input name: ")
# age = int(input("add age: "))

# if name == orname:
#     print("hi alice, welcome")
# elif age <= 12 :
#     print("you aint " + orname  +" kiddo")
# elif age >= 200:
#     print("YOU ARE NOT " + orname +" AND TO OLD TO LOGIN...")


# name = input("Enter Your Name: ")

# count = 0

# while name != "Alice":
#     name = input("Wrong Enter Your Name: ")
#     if count == 2:
#         print("Numbers of Tries Exceeded")
#         break
#     elif name == 'ola':
#         print("Nice Try ola try again")
#     count += 1
    
# if name == 'Alice':
#     print("Welcome Alice!!")

# Write a guessing game program that collects users input then compare it with the Original number 
# if user input is not Original Number user should keep guessing
# user can only guess 3 times

# count = 0

# Guess = int(input("guess me: "))

# while Guess != 9:
#     count += 1 
#     print(f"you have {3 - count} more trials, guess again")

#     Guess = int(input("guess me: "))
    
#     if count == 2:
#         break
    

# if Guess == 9:
#     print("You Win")
    
# else:
#     print("You lose, Game Over!!")
# Guess = int(input("guess a number: "))

# count = 0

# while Guess != 9:
#     count += 1
#     Guess = int(input("guess a number: "))
#     msg = "You Win" if Guess == 9 else "Wrong"
#     print(msg)
#     if count == 2:
#         break
    
# age = 0
# while age  <= 20:
#     print(f'Age is {age}') 
#     age += 1




# while True:
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#         break
# print('Thank you!')

# spam = 0 
# while spam < 5: 
#     print('Hello, world.') 
#     spam = spam + 1
    

    
# x = int(input("Please enter an integer: "))
# # Please enter an integer: 42
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# words = ['cat', 'window', 'defenestrate']

for u in range(100):
    print(u)

# if 12 == 48/3 or 12 is 12:
#     print("Holberton")
# else:
#     print("School")