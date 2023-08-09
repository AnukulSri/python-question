# Program to find lcm of given numbers
## Input
# 10
# 5

# Output: LCM of 10 and 5 is 10

def LCM(a, b):
    greater = max(a, b)
    smallest = min(a, b)

    for i in range(greater, a*b+1, greater):
        # print(i)
        if i % smallest == 0:
            # print("check",i)
            return i
 
if __name__ == '__main__':
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    print(f'LCM of {a} and {b} is {LCM(a, b)}')