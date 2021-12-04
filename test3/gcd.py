import math
from sympy import symbols


def modFunction(f1, f2, Z):
    a = symbols('a')
    b = symbols('b')
    print(f"{f1}")
    print(f"{f2}")
    print(f'{f1}/{f2} == {f1/f2}')
    print(f'{f1}%{f2} == {f1%f2}')
    # if math.gcd(f1, f2) == 1:
    #     print(f'gcd({f1}, {f2}) == 1')
    # else:
    #     print(f'gcd({f1}, {f2}) == {math.gcd(f1, f2)}')


def computeGCD(x, y):
    return math.gcd(x, y)


def order(N):
    ord = []
    for n in range(N):
        if computeGCD(n, N) == 1:
            # print(f"{n} and {N} is gcd 1")
            try:
                i = 1
                while math.pow(n, i) % N != 1 or i == 100:
                    i += 1
                if i == 100 and math.pow(n, i) % N == 1:
                    group = [n, i]
                    ord.append(group)
                elif i <= 100:
                    group = [n, i]
                    ord.append(group)
            except OverflowError:
                continue
    return ord


def unit(N):
    ord = []
    for n in range(N):
        if computeGCD(n, N) == 1:
            ord.append(n)
    return len(ord)


def rem_mod(x, y):
    u = unit(y)
    k = y - u
    return int(math.pow(x, k) % y)


def inverseZ(x, y):
    z = 0
    if math.gcd(x, y) != 1:
        return 0
    try:
        while x * z % y != 1:
            z += 1
    except OverflowError:
        z = 0
    return z


def primitive_Elem(n, N):
    result = []
    first = unit(N)
    second = order(first)
    for s in second:
        i = s[0]
        if i > 1:
            m = int(math.pow(n, i) % N)
            result.append(m)
    result.sort()
    return result


def num_primitive_elem(N):
    f = unit(N)
    return unit(f)


def questionList():
    q = "q: exit the question"
    t1 = "1: gcd"
    t2 = "2: order elements"
    t3 = "3: order unit"
    t4 = "4: Euler's theorem for mod"
    t5 = "5: find the iverse of x in Z(y)"
    t6 = "6: GF(X) == order unit - 1"
    t7 = "7: Given that x is a primitive element of Z(y), find all primitive elements"
    t8 = "8: How many primitive elements in the Z(x) "
    t9 = "9: find mod with symbols"
    
    ql = [t1, t2, t3, t4, t5, t6, t7, t8, t9, q]
    print("\n")
    print("*"*80)
    for i in ql:
        print(i)
    t = input("Enter the question number:")
    question(t)


def question(t):
    try:
        if str(t) == 'q' or t == "" or t is None:
            print("exit the function")
        else:
            t = int(t)
            single = [2, 3, 6, 8]
            double = [1, 4, 5, 7]
            functions = [9]
            if t in double:
                x, y = input("Enter two number (with space): ").split(" ")
                if t == 1:
                    gcd = computeGCD(int(x), int(y))
                    print("gcd is:")
                    print(gcd)
                if t == 4:
                    rem = rem_mod(int(x), int(y))
                    print(f"{x}^{y} mod {y} = {rem}")
                if t == 5:
                    rem = inverseZ(int(x), int(y))
                    if rem != 0:
                        print(f"{x}^(-1) = {rem} (mod {y})")
                    else:
                        print(f'gcd({x}, {y}) = {math.gcd(int(x), int(y))}, '
                              f'so {x} has no inverse in Z({y})')
                if t == 7:
                    result = primitive_Elem(int(x), int(y))
                    print(f"{x} is primitive element of Z({y}), result is")
                    print(result)
            if t in single:
                N = input("Enter a order number: ")
                if t == 2:
                    ord = order(int(N))
                    print("order elements are")
                    print(ord)
                if t == 3:
                    print(f"{N} unit is {unit(int(N))}")
                if t == 6:
                    k = int(N) - 1
                    print(f"GF({N}) = {unit(int(k))}")
                if t == 8:
                    print(f"Z({N}) = {num_primitive_elem(int(N))}")
            if t in functions:
                print('f1 (mod f2) in Z(n) [the symbol use a, b]')
                f1 = input("function 1 [a or b]:")
                f2 = input("function 2 [a or b]:")
                z = int(input("Z(n) [integer]: "))
                modFunction(f1, f2, z)
            questionList()
    except ValueError:
        print("exit the function")
    




if __name__ == "__main__":
    questionList()
    


