first = input("FirstName : ")
last = input("LastName : ")
'''
instead using this  format
message = "First" + "[" + last + "]" is a Coder"
you can lessen the code with this
'''
formattedString = f'{first} [{last}] is a Coder'
print(formattedString)

