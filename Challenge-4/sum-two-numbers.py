# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
 

# Constraints:

# -1000 <= a, b <= 1000


a,b=map(int,input("Enter the numbers:").split())
def getSum(a, b):
    while b!=0:
        carry=a&b
        a=a^b
        b=carry<<1
    return a
print(getSum(a,b))

## a=2 b=3
## 0010
## 0011
## carry=0010
## a=0001
## b=0100
## carry=0000
## a=0101
## b=0000
## a=5
## b=0
## return 5





