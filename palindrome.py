print("This program will find if a number is palindrome or not")
num=int(input("Enter the number: "))
numCopy=num
n=0
while num>0:
    number=int(num%10)
    n=int((n*10)+number)
    num=int(num/10)
if(n==numCopy):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
