import math


def cal():
    N = int(input("number input: "))
    t = int(input("input fraction[1] or num[2]:"))
    if t == 1:
        t1(N)
    else:
        t2(N)


def t1(N):
    store = 0.00
    for n in range(N):
        a, b, c = map(int, input("a/b, log(n): ").split(" "))
        store += hamInt(a, b, c)
    print(f"ham is {round(store, 5)}")
    lengths(store)


def t2(N):
    store = 0.00
    for n in range(N):
        a, b = map(float, input("num, log(n): ").split(" "))
        store += hamFra(a, b)
    print(f"ham is {round(store, 5)}")
    lengths(store)


def hamInt(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    return round(-a/b * math.log(a/b, c), 5)


def hamFra(a, b):
    a = round(a, 5)
    b = int(b)
    return round(-a * math.log(a, b), 5)


def lengths(store):
    print("Do you need different length Huffman codes calculation?")
    yes = input("yes(y)/no(n): ")
    if yes == "yes" or yes == "y":
        s = int(input("lengths(int): "))
        hamS(s, store)
    else:
        print("end")



def hamS(s, store):
    H = round(s*store, 5)
    print(f"H(S^{s}) = {s}H(S^1) around {H}")
    lengths(store)


if __name__ == "__main__":
    cal()