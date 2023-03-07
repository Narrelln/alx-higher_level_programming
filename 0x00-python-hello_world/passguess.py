passfile = open('SecretPassFile.txt')
secretPassword = passfile.read()

print('my pass.')
typedPassword = input()

if typedPassword == secretPassword:
    print('Access granted')
    
elif typedPassword == '123abc': 
    print('That password is one that an idiot puts on their luggage.')
        
elif typedPassword == '12334': 
    print('That password is one that an idiot puts on their luggage.') 

else:
    print('Access denied')
    
print("USER input passWord: " )