#defining a funtion(non paramaterised funtion)
'''def pr():
    print("Hi I am a user defined funtion pr")

pr() ''' #Calling of a funtion

#paramaterised funtion, Funtion capable of accepting value
'''def pg(name):
    print("Hi my name is" " "+ name)
pg("Ankit")'''

'''def pr(first_name , last_name):
    print("Hi my name is"" "+first_name+" "+last_name)
pr("Ankit","Gupta")'''

'''def pr(*name):  # *name is treated as tuple so its is in indexing
    print("My name is "+name[0])
pr("Shukla","Gupta","Sharma")'''

'''def pr(name1,name2,name3):
    print("My name is "+name1)
pr(name1="Ankit",name2="Lpu",name3="College")'''

'''def pr(name):
    for i in name:
        print(i)
name=["Ankit","lpu","School"]
pr(name)'''

# return is a keyword
'''def pr(n):
    return n*5
print(pr(5))'''

#recursion funtion call itself to perform a task
'''def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
print(factorial(6))

def sum(x):
    if x<=1:
        return 1
    else:
        return(x+ sum(x-1))
print(sum(5))
#Reverse a number
n=int(input("Enter the integer number:"))
revs=0
while (n>0):
    # Logic
    remainder = n%10
    revs= (revs*10) + remainder
    n=n//10
print(revs)'''
#Armstrong Number
'''n=int(input())
s=n
b=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**b)
    n=n//10

if s==sum:
    print("Armstrong")
else:
    print("Not Armstrong")'''

'''a="Ankit"  #Global variable

def pr():
    a="Cipher" #localvariable
    global a
print(pr(a))'''

'''a=int(input())
b=str(a)
d=b[-1]
c=int(b[0])**int(d)
if c%2==0:
    print("Even")
else:
    print("odd")'''

'''a=str(input())
b=a[::-1]
if a==b:
    print("Pallindrome")
else:
    print("not Pallindrome")'''

'''x="nitin"
w=''

for i in x:
    w=i+w
if (x==w):
    print("Pallindrome")
else:
    print("Not Pallindrome")'''

#arrange the list in ascending order
'''a=[]
b=int(input())
for i in range(1,b+1):
    value=int(input(" "))%i
    a.append(value)

for i in range(b):
    for j in range(i+1,b):
        if(a[i]>a[i]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)'''

'''def patt(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()

n=5
print(patt(n))'''

print("Roman numeral to Integer Calculator.")
#Defining a function to convert roman numerals into integers.
def romanToInt(s):
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} #All possible Values
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            num+=roman[s[i]]
            i+=1
      return num
while True:
      x = input("Enter an number in Roman Numeral(in capital letters): ")
      print("Value in integer is=",romanToInt(x))
      
#Asking user whether he wants another calculation.
      choice = input("Do you want next calculation?(YES/NO)")

      if choice == "YES":
            continue
      else:
            print("Thank you!")
            break



