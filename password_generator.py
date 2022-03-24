import random
import pyperclip as pc
import os

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

string = lower + upper + numbers

length = input("enter length:")

def loop1():
    
    more = input("do you need more than one?(y/n):")
    
    if more == 'n':
        
        nrun()
    
    elif more == 'y':
        
        yrun()
    
    else:
        
        print('error...please retry')
        
        loop2()

def loop2():
    
    more = input("do you need more than one?(y/n):")
    
    if more == 'n':
        
        nrun()
    
    elif more == 'y':
        
        yrun()
    
    else:
        
        print('error...please retry')
        
        loop1()

def nrun():
    pwd = ''.join(random.sample(string,int(length)))
    
    pc.copy(pwd)
    
    print("password have been copied to clipboard")

def yrun():

    amount = int(input("how many passwords do you need?:"))
    
    while 1 <= amount:
        
        pwd = ''.join(random.sample(string,int(length)))
        
        path = 'pwd.txt'
        
        f = open(path, 'a')
        
        f.write(pwd + '\n')
        
        amount = amount - 1
    
    print('GO CHECK THIS FILE ↓GO CHECK THIS FILE↓')
    
    print(os.path.dirname(os.path.abspath(__file__)) + '\\pwd.txt')

loop1()