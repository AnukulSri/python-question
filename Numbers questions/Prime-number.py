# A prime number is defined as a natural number greater than 1 and is divisible by only 1 and itself. 

n = int(input("Enter a number"))
c=0
for i in range(2,n+1):
    if n%i == 0:
        c +=1

if c == 1:
    print("Number is prime")
else:
    print("Number is not prime")