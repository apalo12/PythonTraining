'''
Created on Jan 27, 2022

@author: apalo12
'''

#############################################################
# STRING
#############################################################
Message = r'APALO12\'s name is Trisha' ## r means do not treat \ as special char
tripleLineMessage = '''
Wade
is
a super cute
DOG
<3
''' 
print(Message)
print(tripleLineMessage)

filename = 'test.txt'
filepath = f'\\home\\apalo12\\{filename}'
print(filepath)

fName = 'Trisha'
lName = 'Palor'
print(fName + ' ' + lName)

str = "Trisha Palor"
print(str[0])
print(str[1])

print(len(str))
print(str[0:2])
print(str[1:])
print('A'+str[1:])
print(str[:-1]+'Z')




#############################################################
# NUMBERS
#############################################################

x = 0.5 * 0.5
##0.25
##The division of two integers always returns a float:
print(x)

x = 20 / 10
"""
2.0
If you mix an integer and a float in any arithmetic operation, the result is a float:
"""

x = 1 + 2.0
##3.0

x = 0.1 + 0.2
##0.30000000000000004
count = 10000000000
##To make the long numbers more readable, you can group digits using underscores, like this:


count = 10_000_000_000
print(count)

CONSTANTS_ALLCAPS = 3.14
#############################################################
# BOOLEAN
#############################################################
print(10>5)
print(5>10)
nullStr = ''
bool(nullStr)
bool('Test')
#############################################################
# INPUT
#############################################################

name = input('Type your name:') ##input fxn returns a string
print('Hello ' + name)

age = input('What is your age:')
ageInMonths = float(age) * 12
print(type(ageInMonths))
print(f'You are {ageInMonths} months old')