import math
from itertools import permutations
import numpy as np
from sympy import symbols
import prime

q = "q: exit the question"
t1 = "1: gcd"
t2 = "2: order elements"
t3 = "3: order unit"
t4 = "4: Euler's theorem for mod"
t5 = "5: find the inverse of x in Z(y)"
t6 = "6: GF(X) == order unit - 1"
t7 = "7: Given that x is a primitive element of Z(y), find all primitive " \
     "elements"
t8 = "8: How many primitive elements in the Z(x) "
t9 = "9: find mod with symbols [can't do, skip]"
t10 = "10: Calculate the decryption exponent d. For RSA encryption \n  [n, e]"
t11 = "11: Decipher the received ciphertext c, and solve the n-letter word [" \
      "skip, didn't finish]"
ql = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, q]


def modFunction(f1, f2, Z):
    a = symbols('a')
    b = symbols('b')
    print(f"{f1}")
    print(f"{f2}")
    print(f'{f1}/{f2} == {f1/f2}')
    print(f'{f1}%{f2} == {f1%f2}')


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
    pri_list = prime.primeFactors(N)
    if len(pri_list) > 0:
        print(f"{N} prime is {pri_list}")
        un = 1
        print(f"{N} unit = ", end="")
        for i in pri_list:
            if un != 1:
                print(f" x {i - 1}", end="")
            else:
                print(f"{i - 1}",end="")
            un *= i - 1
        print(f"= {un}")
        return un
    for n in range(N):
        if computeGCD(n, N) == 1:
            ord.append(n)
    return len(ord)


def decryption_exponent_d(N, e):
    print("Euclidean Algorithm")
    N = int(N)
    e = int(e)
    un = unit(N)
    remainder = int(un % e)
    sub = un
    div = e
    formula = []
    while remainder != 0:
        if div != 0:
            multiple = int((sub - remainder) / div)
            fun = [sub, multiple, div, remainder]
            formula.append(fun)
            print(f"{sub} = {multiple} x {div} + {remainder}")
            sub = div
            div = remainder
            remainder = int(sub % div)
    print("so")
    sum_mul = 0
    for i in range(len(formula)):
        sum_mul += formula[i][1]
    print(f"decryption exponent d = {sum_mul}")
    print("check")
    process_Q5(e, un)


def decipher_with_RSA():
    N = int(input("number of word: "))
    word_code = []
    print("Enter the multiplier and times in the formula one by one")
    print("Example 1: 29*a1^2 => input is: 29 2")
    print("Example 2: 29*a1 => input is: 29 1")
    print("Example 3: a1 => input is: 1 1")
    print("Example 4: 2 => input is 2 0 [that'll not multiple with others")
    print("[multiplier, times]")
    for n in range(N):
        word = [int(i) for i in input(f"a{n + 1}: ").split(" ")]
        word_code.append(word)
    letters = []
    letters_coding = {}
    print("input the number of letters and the encoding of every letter")
    print("Don't need [,] ==> only char and integer")
    num_letter = int(input("number of letters: "))
    if num_letter == 26:
        if int(input("Are there A-Z? YES[1] || NO [2]: ")) == 1:
            if int(input("Are there numbers are continue? YES[1] || NO[2]: ")) \
                    == 1:
                start, end = map(int, input("input the start, end number: "
                                            "").split(" "))
                for i in range(start, end + 1):
                    letters.append(i)
                    letters_coding[i] = chr(65 + abs(end - i - 25))
    if len(letters) != num_letter:
        for i in range(num_letter):
            input_let = [i for i in input(f"{i}: [letter, number]: ").split(" ")]
            num = int(input_let[1])
            letters.append(num)
            letters_coding[num] = input_let[1]
    print(f"{letters_coding}")
    letter_list = list(permutations(letters, N))
    c = int(input("Decipher the received ciphertext c = "))
    n = int(input("n = "))
    e = int(input("e = "))
    un = unit(n)
    d = process_Q5(e, un)
    # c_d = np.power(c, d)
    # remainder = int(np.remainder(c_d, n))
    c_d = 0
    remainder = 0
    print(f"c^d = {c}^{d} = {c_d} = {remainder} (mod {n})")
    for l in letter_list:
        finding = 0
        for i in range(len(l)):
            finding += math.pow(l[i], word_code[i][1]) * word_code[i][0]
        if remainder == finding:
            words = []
            print(f"c = {finding} = ", end="")
            for i in range(len(l)):
                if i + 1 != N:
                    print(f"{l[i]} * {word_code[i]} + ", end="")
                else:
                    print(f"{l[i]}^{word_code[i][0]} * {word_code[i][1]}")
                words.append(letters_coding[l[i]])
            print(f"So the {N}-word are {words}")
            
    
    
def remainder_mod(x, y):
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
    print("*"*80)
    for i in ql:
        print(i)
    t = input("Enter the question number: ")
    question(t)


def process_Q5(x, y):
    rem = inverseZ(int(x), int(y))
    if rem != 0:
        print(f"{x}^(-1) = {rem} (mod {y})")
    else:
        print(f'gcd({x}, {y}) = {math.gcd(int(x), int(y))}, '
              f'so {x} has no inverse in Z({y})')
    return rem


def question(t):
    try:
        if str(t) == 'q' or t == "" or t is None:
            print("exit the function")
        else:
            t = int(t)
            single = [2, 3, 6, 8]
            double = [1, 4, 5, 7, 10]
            functions = [9]
            if t in double:
                x, y = input("Enter two number (with space): ").split(" ")
                if t == 1:
                    gcd = computeGCD(int(x), int(y))
                    print("gcd is:")
                    print(gcd)
                if t == 4:
                    rem = remainder_mod(int(x), int(y))
                    print(f"{x}^{y} mod {y} = {rem}")
                if t == 5:
                    process_Q5(x, y)
                if t == 7:
                    result = primitive_Elem(int(x), int(y))
                    print(f"{x} is primitive element of Z({y}), result is")
                    print(result)
                if t == 10:
                    decryption_exponent_d(x, y)
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
            if t == 11:
                decipher_with_RSA()
            if t in functions:
                print('f1 (mod f2) in Z(n) [the symbol use a, b]')
                fun1 = input("function 1 [a or b]:")
                f2 = input("function 2 [a or b]:")
                z = int(input("Z(n) [integer]: "))
                modFunction(fun1, f2, z)
            input("Enter any bottom then go to next")
            questionList()
    except ValueError:
        print("exit the function")


if __name__ == "__main__":
    questionList()
    


