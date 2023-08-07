# A neon number is a number where the sum of digits of square of the number is equal to the number.
# Examples: Input : 9 Output : Neon Number Explanation: square is 9*9 = 81 and sum of the digits of the square is 9.

n = int(input("Enter a number"))
sq = n**2

c =0
while sq>0:
    mod = sq%10
    c += mod
    sq = sq//10

if c == n:
    print("Number is neon")
else:
    print("Number is not neon")