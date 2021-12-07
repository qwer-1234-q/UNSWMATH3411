import math
import prime


def pseudo_prime(N, l):
    for a in l:
        print(f"\t{a}^{N -1} % {N} = {math.pow(a, N - 1) % N}")
        if math.gcd(N, a) == 1 and math.pow(a, N - 1) % N == 1:
            return a
    return None
    # finding = True
    # prime = 0
    # n = 1
    # while finding and n <= 1000:
    #     for i in l:
    #         if math.pow(i, n) % N == 1:
    #             finding = False
    #             prime = i
    #             break
    #     n += 1
    # return prime


def strong_pseudo_prime(n, l):
    s, t = find_s_t(n)
    r_list = [int(i) for i in range(s)]
    print(f"\ts = {s} t = {t} r = {r_list}")
    for a in l:
        if math.gcd(a, n) == 1 and a > 1:
            if math.pow(a, t) % n == 1:
                print(f"\t{a}^{t} = {math.pow(a, t)} = "
                      f"{math.pow(a, t) % n} = 1 (mod {n})")
                return a
            else:
                print(f"\t{a}^{t} = {math.pow(a, t)} = "
                      f"{math.pow(a, t) % n} != 1 (mod {n})")
            for r in r_list:
                d = math.pow(2, r) * t
                if math.pow(a, d) % n == (n - 1):
                    print(f"\t{a}^(2^{r} * {t}) = "
                          f"{math.pow(a, d)} = {math.pow(a, d) % n} "
                          f"= -1 (mod {n})")
                    return a
                else:
                    print(f"\t{a}^(2^{r} * {t}) = "
                          f"{math.pow(a, d)} = {math.pow(a, d) % n} "
                          f"!= -1 (mod {n})")

    return None


def find_s_t(n):
    prime_factors = prime.primeFactors(n - 1)
    print(prime_factors)
    s = 0
    t = 1
    for p in prime_factors:
        if p % 2 != 0:
            t *= p
    div = (n - 1) / t
    if div % 2 == 0:
        for i in range(n):
            if math.pow(2, i) == div:
                s = i
                break
    
    return s, t

def cal():
    N = input("Enter pseudo-prime N: ")
    num_base = int(input("number of base input: "))
    i = 0
    l = []
    try:
        while i < num_base:
            n = int(input(f"Input {i + 1} option value: "))
            l.append(n)
            i += 1
    except ValueError:
        print("sorry, end for session")
    if len(l) == num_base:
        pri = pseudo_prime(int(N), l)
        print(f"pseudo prime is {pri} ")
        strong = strong_pseudo_prime(int(N), l)
        print(f"strong pseudo prime is {strong} ")
    else:
        print("not enough")


if __name__ == "__main__":
    cal()
    


    


