# ## write a python program to add two number

# a = input('Enter first number : ')
# b = input('Enter the second number : ')

# #type casting
# a = int(a)
# b = int(b)
# print("Sum of that numbers is : ",a+b)


# ## Write to find the reminder while number is divided by the 2

# a = input('Enter the number that you want to divide by the 2 :')
# a = int(a)
# print("The result is : ", a%2)

# ## write p for comparing the value

# a = 45
# b = 89
# print('a is grater then b or not : ',a>b)


# ## write the p for find the avrage of two numbers

# a = input('Enter the first number : ')
# b = input('Enter the second number : ')
# a=int(a)
# b=int(b)
# avg=(a+b)/2
# print('The avrage of the numbers is : ', avg)



# ## write the p for find the sqaure of then number

# a = input('Enter the number : ')
# a = int(a)
# print('sqaure of the number is : ',a*a)


# ## string functions

# a = 'Hello '
# b = 'Bhargav'
# print("New string is :",a+b)
# print(a[0:4])
# a = "you are an engineer"
# print(a.endswith("neer"))
# print(len(a))
# print(a.count("e"))
# print(a.capitalize())
# print(a.find("are"))
# print(a.replace("engineer","trader"))


# ## write a p that display the good mornig followed by user input

# a=input("Enter your name : ")
# print("Good Morning",a)


# ## write a p to make an letter template

# letter='''\nDear friend, name
# you are selected,
# OnBoarding Date is : date \n'''
# a=input("Enter you name\n")
# b=input("Enter the date\n")
# letter=letter.replace("name",a)
# letter=letter.replace("date",b)
# print(letter)


# ## wirte a p to find dooble spaces in string and replace with single space

# a="hello brother  how are you"
# ds=a.find("  ")
# print(ds)
# print(a)
# s=a.replace("  "," ")
# print(s)


# ## LIST METHODS

# hey = [1,9,2,6,2,3,7]
# print(hey)
# hey.append(5)
# print(hey)
# hey.sort()
# print(hey)
# hey.reverse()
# print(hey)
# hey.insert(1,8)
# print(hey)
# w=hey.pop()
# print(w)
# hey.remove(5)
# print(hey)


# ## write a p to store the fruits in list given by the user

# fruits = []
# a=input("enter the fruit name :")
# b=input("enter the fruit name :")
# c=input("enter the fruit name :")
# d=input("enter the fruit name :")
# e=input("enter the fruit name :")
# fruits=[a,b,c,d,e]
# print(fruits)



# ## write a p to sort the list

# Marks = []
# a=int(input("enter the englist marks :"))
# b=int(input("enter the hindi marks :"))
# c=int(input("enter the science marks :"))
# d=int(input("enter the scoial marks :"))
# e=int(input("enter the gujrati marks :"))
# f=int(input("enter the maths marks :"))
# Marks=[a,b,c,d,e,f]
# Marks.sort()
# print(Marks)


# ## write a p to sum of list elements and dictonary concept

# l=[0,1,2,3,4,5,6,7,4,5,2,0,0,3,8,9,10]
# print(sum(l))
# print(l.count(0))
# i = {"a":"hello",
# 14:45,
# "bhargav":"hello"}
# print(i['a'])
# print(i.keys())
# print(i.values())
# print(list(i.keys()))
# print(i.items())
# newdict = {
#     "bhargav":"jaja"
# }
# i.update(newdict)
# print(i)


# ## wirte a program to provide the dictonary of hindi english words

# data={"kem che":"How are you",
# "kya javu che":"where are you going",
# "chamchi":"spoon",
# "chopdi":"book"
# }
# print("Options are ",data.keys())
# user=input("Enter the word: ")
# print("Meaning of that word:",data.get(user))


# ## write a p to input all numbers from user and display that unique number once

# a=int(input("NEter the number 1 "))
# b=int(input("NEter the number 2 "))
# c=int(input("NEter the number 3 "))
# d=int(input("NEter the number 4 "))
# e=input("NEter the number 5 ")
# f=int(input("NEter the number 6 "))
# g=int(input("NEter the number 7 "))
# h=int(input("NEter the number 8 "))
# data={a,b,c,d,e,f,g,h}
# print(data)
# data=set()
# data.add(78)
# data.add(36)
# data.add(35)
# print(len(data))


# ## make an empty dictonary in that 4 person enter their fav language as values and name of that person as keys

# data={}
# bhargav=input("enter your fav language: ")
# bhautik=input("enter your fav language: ")
# aniket=input("enter your fav language: ")
# harsh=input("enter your fav language: ")
# data["bhargav"]=bhargav
# data["bhautik"]=bhautik
# data["aniket"]=aniket
# data["harsh"]=harsh
# print(data)


# ## if else concept

# a=int(input("Enter your age :"))
# if(a>18):
#     print("Your eligable")
# else:
#     print("your are not eligable")


# ## find greates number among 4 that is entered by user

# a=int(input("a enter the number: "))
# b=int(input("b enter the number: "))
# c=int(input("c enter the number: "))
# d=int(input("d enter the number: "))
# if(a>b):
#     f1=a
# else:
#     f1=b
# if(c>d):
#     f2=c
# else:
#     f2=d
# if(f1>f2):
#     print(f1, " is greates number")
# else:
#     print(f2, " is greatest number")


# ## write a program to check the student is passed or fail and conditon is in all subject it has above 33 and total is above 40

# a = int(input("Enter the subject 1 marks: "))
# b = int(input("Enter the subject 2 marks: "))
# c = int(input("Enter the subject 3 marks: "))
# if(a<33 or b<33 or c<33):
#     print("you are failed cause score is lower than 33")
# elif(a+b+c)/3 > 40:
#     print("You are passed")
# else:
#     print("You are failed cause total is less than 40")


# ## wirte a porgram to print table of given number using the for loop

# a=int(input("Enter the number: "))
# for j in range(1,11):
#     print(str(a) + " X " + str(j) + " = " + str(a*j))


# ## wirte a program to greet the all the person that name start with b

# l1=["bhargav","bhautik","aniket","harsh"]
# for i in l1:
#     if i.startswith("b"):
#         print("Good Morning : ",i)


# ## write a program of table that given from the user and print it using the while loop and using the f string

# a=int(input("enter the number : "))
# i=1
# while i<11:
#     print(f"{a} X {i} = {a*i}")
#     i=i+1


# ## write a program to check the given number is prime or not prime

# a=int((input("enter  the number : ")))
# prime=True
# for i in range(2,a):
#     if a%i==0:
#         prime=False
#         break
# if prime:
#     print("prime")
# else:
#     print("not prime")


# ## write a program to find the sum of odd number using the while loop

# n=int(input("enter the number : "))
# i=0
# j=0
# while i<n:
#     if i%2==0:
#         j=j+i
#     i=i+1
# print(j)


# ## wirte aprogram to find the factorial of the given number

# n=int(input("Enter the number : "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)


# ## write a program to print the pattern

# n=3
# for i in range(3):
#     print(" " * (n-i-1),end="")
#     print("*" * (2*i+1),end="")
#     print(" " * (n-i-1))


# ## write a program to print the pattern

# for i in range(3):
#     if i==1:
#         print(" * ",end="")
#         print("   ",end="")
#         print(" * ")
#     else:
#         print(" * ",end="")
#         print(" * ",end="")
#         print(" * ")


# ## wirte a porgram to print table of given number using the for loop

# a=int(input("Enter the number: "))
# for j in range(10,0,-1):
#     print(str(a) + " X " + str(j) + " = " + str(a*j))


# ## functions

# def greet(name):
#     print("Have a nice day: ",name)
# name=input("Enter your name ")
# greet(name)
# def sum(a,b):
#     return print(a+b)
# sum(4,6)


# ## recursion

# def factorial_recusive(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial_recusive(n-1)
# a=factorial_recusive(5)
# print(a)


# ## iterative function

# def factorial_iterative(n):
#     fact = 1
#     for i in range(n):
#         fact = fact * (i+1)
#     return fact
# a=factorial_iterative(5)
# print(a)


# ## write a function to find the greatest of threee number

# def big(a,b,c):
#     if a>b and a>c:
#         print("a is greatest of in all of three")
#         return a
#     if b>a and b>c:
#         print("B is greates of all three")
#         return b
#     else:
#         print("C is greates in alll of three")
#         return c
# print(big(78,68,97))


# ## wirte a function that return the celcius to ferenhight

# def cTOf(c):
#     return print((c*1.8)+32)
# cTOf(33)


# ## write a recusive function to print the sum of first n natural number

# def sum(n):
#     if n==0:
#         return 0
#     return n + sum(n-1)
# print(sum(10))


# ## write  a function that print the pattern 

# def pattern(n):
#     for i in range(n):
#         print("* "*n)
#         n = n-1
#     return print("Above is your pattern")
# pattern(3)


# ## wirte a function convert the inches to centimeter

# def inchesTOcentimeter(n):
#     return print(n*2.54)
# inchesTOcentimeter(10)


# ## write a function to remove the word from list

# def change(l1,key):
#     l1.remove(key)
#     return l
# l = []
# s=int(input("Enter the number about the how many elements you want to add in list "))
# for i in range(s):
#     a=input("Enter the element that you want instert in list ")
#     l.append(a)
# word=input("enter the word that you want remove from the list ")
# print(l)
# change(l,word)
# print(l)


# ## write a function make the multiplication table of given number

# def multable(n):
#     for i in range(11):
#         print(f"{n} X {i} = {n*i}")
#     return print("ABove is your multiplication table")
# n=int(input("enter the number: "))
# multable(n)