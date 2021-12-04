

def isPrime(n):
    flag = False
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                flag = False
                break
    return flag


def primeFactors(n):
    if n <= 2:
        return []
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
            
        else:
            if i not in factors:
                factors.append(int(i))
            n //= i
    
    if n > 2 and n not in factors:
        factors.append(int(n))
    return factors


# def revs_number(n):
#     if n == 0:
#         return
#     revs = 0
#     while n > 0:
#         remainder = n % 10
#         revs = revs * 10 + remainder
#         n = n // 10
    
#     return revs


def cal():
    n = input("Enter the number: ")
    if n == "q" or n == "" or n == " ":
        print("exit prime")
    else:
        factors = primeFactors(int(n))
        print('\n'.join(map(str, factors)))
        # revs = revs_number(int(n))
        # print(f"reverse number is {revs}")
        cal()
        

if __name__ == "__main__":
    cal()


    


