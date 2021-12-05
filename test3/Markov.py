import humman

store = []

def cal():
    print("2-symbol Markov source")
    print("plz retype if you type something wrong. "
                "this function will not assume any errors")
    s = ""
    for i in range(80):
        s += "*"
    print(s)
    print("plz enter one by one")
    print("transition matrix M:")
    m = []
    for i in range(2):
        a = []
        for j in range(2):
            num = float(input(f"m[{i}][{j}]: "))
            a.append(num)
        m.append(a)
    
    print("equilibrium distribution P")
    p = []
    for i in range(2):
        a, b = map(int, input(f"p[{i}]: ").split("/"))
        p.append(a/b)
    
    hm = 0.0
    for i in range(2):
        k = 0.0
        for j in range(2):
            print(f"-{m[j][i]} * log 2 {m[j][i]}")
            k += humman.hamFra(m[j][i], 2)
        print(f"p[{i}] = {p[i]}")
        k = k * p[i]
        hm += k
    
    print("result:")
    print(f"{hm}")



if __name__ == "__main__":
    cal()