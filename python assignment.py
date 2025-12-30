#1
temperature=float(input("enter the input:"))
celsius=temperature

fahrenheit=(celsius * 9/5)+32
kelvin=(celsius+273.15)

print(kelvin)
print(fahrenheit)

#2
Totalbill=int(input("Enter the total bill: "))
friends=int(input("enter the total friends: "))

each_will_pay=int(Totalbill/friends)

print(each_will_pay)
print(type(each_will_pay))

#3
text based emotions into emojis

message=input("enter your message :")
message=message.replace("⇈","😊")
message=message.replace("⇊","😀")
message=message.replace(":)","😊")
message=message.replace("--","💙")
 
print(message)

str=input("enter the input: ")
print(len(str))
print(str.upper())
print(str.lower())

#LIST
movie1=input("enter your fav movie1: ")
movie2=input("enter your fav movie2:")
movie3=input("enter your fav movie3:")
movieList=[movie1,movie2,movie3]
print(movieList)

marksTuple=(87,64,33,95,76)
print(max(marksTuple))
print(min(marksTuple))

marks=int(input("enter the marks:"))
if(marks>=90):
   print("A")
elif(marks>=80):
   print("B")
elif(marks>=70):
   print("C")
else:
   print("D")

#dict
meaning={
   "WIP":"work in progress",
   "vibrant":"full of energy",
   "nostalgia":"longing for the past"
}
print(type(meaning))
print(meaning)
print(meaning["WIP"])

set1={2,3,5,7,1}
print(type(set1))
print(set1)
set2={1,2}
set3=set1.union(set2)
print(set3)
set4=set1.intersection(set2)
print(set4)


i=int(input("enter the input: "))
import time

for i in range(i,0,-1):
   print(i)
   time.sleep(1)
  print("HAPPYY NEW YEARR...🧁")

n=int(input("enter the value :"))
i=1
while(i<=10):
   print(n,"*",i,"=",(n*i))
   i=i+1

import random
number=random.randint(1,100)
guess=0
print("guess the number between 1 and 100")

while guess!=number:
   guess=int(input("enter your guess:"))

   if guess<number:
       print("too low!guess again")
   elif guess>number:
       print("too high!guess again")
   else:
       print("congrats!you guess correct")

