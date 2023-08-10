# A palindromic number is a number (such as 16461) that remains the same when its digits are reversed. 

n = int(input("Enter a number "))
a = n
rev = 0
while a>0:
    mod = a%10
    rev = (rev*10) +mod
    a = a//10

if rev == n:
    print("Number is palindrome")
else:
    print("Number is not prime")
