# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 05:22:13 2024

@author: lenovo
"""
users = {}

def register():
    username = input("Enter a unique username: ")
    
    if username in users:
        print("Username already exists. Please try a different username.")
        return
    password = input("Enter a new password: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    enrol = input("Enter your enrollment number: ")
        
    users["username"] = ["{password},{email},{phone},{enrol}"]
    
    print("User registered successfully!")
    attempt_quiz()
    
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users and password in users[username]:
        print(f"Login successful! Welcome, {username}!")
        attempt_quiz()
        
    else:
        print("No such user found! Register first.")
        register()
        
        
def attempt_quiz():
    sub = int(input("Enter 1 for DSA Quiz,\n"
                    "Enter 2 for DBMS Quiz,\n"
                    "Enter 3 for python Quiz : "))
    
    if sub == 1 :
        Marks = 0
        answer = ["ARRAY","LINKED LIST","QUEUE","STACK","VECTOR"]
        i=1
        while(i != 6):
            if(i == 1):
                print("Q1) State Linear data structure which uses contiguous memory allocation.")
                ans = input("Enter your answer: ")
                if( answer[0] == ans.capitalize()):
                    Marks+=2 
                i+=1
            elif(i == 2):
                print("Q2) State Linear data structure which uses pointer.")
                ans = input("Enter your answer: ")
                if( answer[1] == ans.capitalize()):
                    Marks+=2
                i+=1
            elif(i == 3):
                print("Q3) State Linear data structure which uses FIFO.")
                ans = input("Enter your answer: ")
                if( answer[2] == ans.capitalize()):
                    Marks+=2 
                i+=1       
            elif(i == 4):
                 print("Q4) State Linear data structure which uses LIFO.")
                 ans = input("Enter your answer: ")
                 if( answer[3] == ans.capitalize()):
                     Marks+=2
                 i+=1   
            elif(i == 5):
                 print("Q5) State Linear data structure which uses dynamic array.")
                 ans = input("Enter your answer: ")
                 if( answer[4] == ans.capitalize()):
                     Marks+=2 
                 i+=1
    print(f"You scored {Marks}/10.Thank you for taking the test!")             
register()


        
    
        
    