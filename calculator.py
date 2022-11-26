'''def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Selet the oprator that you want to perform")
print("1.Addition")
print("1.Subtract")
print("1.Multiply")
print("1.Division")

choice=input("Choose 1/2/3/4:")
#if choice in ('1','2','3','4'')

if choice in ("1","2","3","4"):
    n1=float(input("Enter the first number"))
    n2=float(input("Enter the second number"))

    if choice =="1":
        print(sum(n1,n2))
    elif choice =='2':
        print(sub(n1,n2))
    elif choice =='3':
        print(mul(n1,n2))
    elif choice =='4':
        print(div(n1,n2))
    else:
        print("Select the correct option")'''


#a=int(input())

'''if a%2==0:
    print("It is Even Number")
else:
    print("Odd")'''
count = 0
n = int(input('\nEnter whole number to check : '))
i = 2
while i <= (n/2):
    if (n%i) == 0:
        count = 1
        break
    else:
        i += 1
    
if n <= 1:
    print(n,'is neither prime nor composite')
elif count == 0:
    print(n,'is a prime number.')
elif count == 1:
    print(n,'is not a prime number.')

