#################################
#######EXERCISE 1 30 MARKS#######
#################################
#Student Name: KE Motsoane
#Student No:218250416
#Date :9 February 2023
#Assignment 3: Python
#Problem 1
#Given string
s='fullstackslp'

#print the following
#f
print(s[0])
#p
print(s[11])
#'stack'
print(s[4:9])
#slp
print(s[9:])
#cks
print(s[7:10])

#Bonus Reverse
s ='fullstrackslp' [::-1]
print(s)

#Problem2 - Lists
#Grab hello from the following
d1 = {'Simple_key':'hello'}
print(d1[0:1])
d2 = {'k1':{'k2':'hello'}}
#d3 ={'k1':[{'nest_key'}:['this is deep'],['hello']]}

#Problem 4 -Sets(4)
#use a set to find the unique values of the list below
myList = [1,1,1,1,1,2,2,2,2,3,3,3,3] 

set_list = set(myList) 
print("The unique elements of the input list using set():\n") 
list = (list(set_list))
 
for i in list: 
    print(i) 

#Problem 5 -Formatting (5)

#You are given 2 variables
age = 45 
name = 'Kyle'
#use print formatting to print the following stirng
print("Hello my dogs name is {} and he looks {} years old".format(name,age))

