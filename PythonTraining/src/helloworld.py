'''
Created on Jan 26, 2022

@author: apalo12
'''

def printHello():
    name = ['Trisha','Wade']
    countNm = name.__len__()
    print(countNm)
    for i in range(countNm):
        print("Hello ",name[i])
    

printHello()
print("Hello world")

