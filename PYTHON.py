#1
name=input("enter your name:")
age=input("enter your age:")
print("hello",name,age)

#2
diameter=float(input("enter value:"))
area=3.141 * diameter
print("area of circle:",area )

#3
age=input("enter the age:")
print(age)
print(type(age))

#4
x=int(input("enter the 1st number:"))
y=int(input("enter the second number:"))
z=x + y
print("sum of the two numbers:",z)

#5
x=int(input("enter the 1st number:"))
y=int(input("enter the second number:"))
z=int(x+y /2)
print("Average of the two numbers:",z)

#6
x=5
y=float(x)
print("Original value:",x)
print(type(x))
print("Converted value:", y)
print(type(y))

#7
a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a**b)

print(a>b)

#STRINGS
#1
str1='hi'
str2="helloo"
str3='''Python'''

print(str1)
print(str2)
print(str3)

#2
str1="helloo"
str2="worldddd"

print(str1 +" "+ str2)

print(len(str1))
str="HARIKA"
print(str[2])

#3
str=input("enter your name: ")
print(str[0])
print(str[-1])
print(len(str))

#4
str="GULABJAMUN"
print(str[0:5])
print(str[:6])
print(str[5:])

#5
str=(input("enter the value"))
print(str[-2:])
mid=len(str) / 2
print(mid)

#methods
#1
str="harika goud"
print(str.upper())
print(str.lower())
print(str.title())
print(str.find("ka"))
print(str.replace("goud","kotha"))
print(str.count("a"))

#2
str="python is easy"
print(str.lower())
new_str=print(str.replace(" ","_"))
print(new_str)

#3
name="harika goud"
age=21
print(F "My name is {name} and iam {age} years old.")

print("hi\n harika")
print("hi\tharika")
print("hi\\harika")
print("hi harika\'s people")
print("he said\"hii\"")

#4
marks=78
if(marks>=90):
   print("your grade is A+")
elif(marks>=80):
   print("your grade is A")

#5
age=25
if(age>=18):
   print("eligible to vote")
else:
   print("not eligible")

#6
number=int(input("enter your number :"))
if(number>0):
   print("number is positive")
elif(number==0):
   print("number is zero")
elif(number<0):
   print("number is negative")

#7
number=int(input("enter your number :"))
if(number>0):
   print("number is positive")
elif(number==0):
   print("number is zero")
else:
   print("number is negative")

#List
#1
food=["apple","pani puri","waffle","7","gulab jamun"]
print(len(food))
print("first value of list: ",food[0])
#2
food[0]="laddu"  # changable-mutable
print(food)
#3
marks=[99,100,90,95]
print(marks[3])
marks[1]=45
print(marks)
print(marks[1:4])
print(marks[:3])
print(marks[-3:-1])
print(max(marks))
print(min(marks))
marks.append(2)
print(marks)
marks.insert(5,80)
print(marks)
marks.remove(99)
print(marks)
marks.pop(2)
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)
#4
food1=input("enter food 1:" )
food2=input("enter food 2:" )
food3=input("enter food 3:" )
foodList=[food1,food2,food3]
print(foodList)
print(len(foodList))
#5
myTuple=(70,80,90)
studentTuple=("harika","ram","ram","krish")
#6
print(studentTuple[2])
emptytuple
emptyTuple=()
print(type(emptyTuple))
singleTuple=(1,)
print(type(singleTuple))
print(studentTuple.count("ram"))
#7
fruitsTuple=("apple","banana","mango","kiwi","strawberry")
print(len(fruitsTuple))
print(fruitsTuple.index("mango"))

#dictionary
#1
student={
   "name":"Harika",
   "age":21,
   "city":"hyderabad"
}
print(student["age"])
print(type(student))
print(student)
student.pop("city")
print(student)
student.keys()
print(student.keys())
student.values()
print(student.values())
student.items()
print(student.items())

#2
marks={
   "maths":90,
   "physics":70,
   "telugu":80
}
print(marks)

#3
languages={"python","java","c","python"}
print(languages)
print(type(languages))

#4
programmingList=["python","java","python","c++","java","c"]

programmingSet=set(programmingList)
print(type(programmingSet))
print(programmingSet)
print(len(programmingSet))

#5
i=1

while(i<=10):
    print(i)
    i+=1
#6
i=10
while(i>=1):
   print(i)
   i-=1
#7
n=1
while(n<=50):
   if(n%2==0):
       print("even numbers:",n)
       n+=2

#8
n=int(input("enter the number: "))
sum=0

while(n>=1):
   sum=sum+n
   n=n-1
print(sum)
print(n)

n=1
while(n<=4):
   print("*" * n)
   n=n+1
#9
n=1
while(n<=5):
   print(n,".Harika")
   n=n+1
n=int(input("enter a number:"))
i=1
while(i<=10):
  print(n,"*",i, "=", n*i)
   i=i+1

for i in range(1,6):
   print("iteration:",i)

for i in range(1,10,2):
   print(i)

for i in range(1,20):
   if i%2==0:
     print("even number:",i)

for i in range(1,50):
       if i%5==0:
          print("harika")
       else:
             print(i)

for i in range(1,10):
  print(i**2)

for i in range(100,0,-1):
   print(i)

name="harika"
for i in range(5):
   print(name.upper())

#functions
def sumFunc():
   a=5
   b=4
   total=a+b
   print(total)

sumFunc()

def welcome_message():
   print("Welcome to Python Programming!!")

welcome_message()
welcome_message()
welcome_message()

def inspire():
   print("“Harika, your dreams are valid. Your effort today is building your success tomorrow.”")
          
inspire()

def good_morning():
   print("Good Morning!..HARIKA")
good_morning()
good_morning()

def display_python():
   print("Python is fun!")
display_python()

def learn():
   print("Python topics:1.conditioning statements,\n2.loops,\n3.functions")
learn()

def average(a,b):      #function with parameters
   averageValue=(a + b)/2
   print(averageValue)

average(10,5)          #with arguments
average(3,6)

def show_age(name,age):
   print(name,"is",age,"years old.")

show_age("Harika",21)

def add_numbers(a,b):
   add=a+b
   print(add)

def diff_numbers(a,b):
   sub=a-b
   print(sub)

add_numbers(10,5)
diff_numbers(10,5)

def fav_food(food):
   print("Harika loves",food)

fav_food("Biryani")

def multiply(a,b):
   return a*b
print(multiply(10,10))
result=multiply(5,10)
print(result)

def square(num):
   return num**2
print(square(11))

def count_vowels_consonants(userInput):
   vowels="aeiouAEIOU"
   countVowel=0
   countConsonant=0
   for eachChar in userInput:
       if(eachChar.isalpha()):
           if(eachChar in vowels):
               countVowel=countVowel+1
           else:
               countConsonant=countConsonant+1

   return countVowel,countConsonant
vowels,consonants=count_vowels_consonants("KOTHA HARIKA goud")

print(vowels,consonants)

def convert_to_upper(word):
   return(word.upper())

word=convert_to_upper("harika kotha")
print(word)

def full_name(fname,lname):
   return fname+" "+lname

name=full_name("Harika","kotha")
print(name)

file handling

file=open("file.py","r")
data=file.read()

print("data of the file is")