# An Armstrong number is one whose sum of digits raised to the power three equals the number itself. 371, 
# for example, is an Armstrong number because 3**3 + 7**3 + 1**3 = 371.

n = int(input("Enter a number"))
a = n
c = 0

while a>0:
    mod = a%10
    d = mod**3
    c += d
    a = a//10

if n==c:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
