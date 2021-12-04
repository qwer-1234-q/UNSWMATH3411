import math


def pseudo_prime(N, l):
    finding = True
    prime = 0
    n = 1
    while finding and n <= 1000:
        for i in l:
            if math.pow(i, n) % N == 1:
                finding = False
                prime = i
                break
        n += 1
    return prime


def strong_pseudo_prime(N, l):
    prime = pseudo_prime(N, l)
    t = 0
    if N % 2 == 0:
        t = N % 2
    else:
        t = int((N - 1) / 2)
    if math.pow(prime, t) % N == 1:
        return prime
    r = 0
    finding = True
    while finding and r <= 100:
        # s = 
        if math.pow(prime, math.pow(2, r) * t) % N == N - 1:
            return prime
        r += 1
    return None


def cal():
    N = input("Enter N: ")
    i = 0
    l = []
    try:
        while i < 5:
            n = int(input(f"Input {i + 1} option value: "))
            l.append(n)
            i += 1
    except ValueError:
        print("sorry, end for session")
    if len(l) == 5:
        prime = pseudo_prime(int(N), l)
        print(f"pseudo prime is {prime} ")
        strong = strong_pseudo_prime(int(N), l)
        print(f"strong pseudo prime is {strong} ")
    else:
        print("not enough")


if __name__ == "__main__":
    cal()
    


    


