import math


def fermat(n):
    b = 0
    a = 0
    t = math.sqrt(int(n))
    t = int(t)
    s = math.pow(t, 2) - n
    while isPerfectSquare(s) == False:
        t += 1
        s = math.pow(t, 2) - n

    s = int(math.sqrt(int(s)))
    a = t + s
    if a > t - s:
        b = a
        a = t - s
    else:
        b = t - s
    
    if a >= 2 and b > a:
        return b - a
    print("not result")
    return None

# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    if x < 0:
        return False
    s = int(math.sqrt(x))
    return s*s == x
 
# Returns true if n is a Fibinacci Number, else false
def isFibonacci(n):
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perferct square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)


def cal():
    n = int(input("Enter a number: "))
    print("the value of b - a is")
    print(fermat(n))


if __name__ == "__main__":
    cal()


    


