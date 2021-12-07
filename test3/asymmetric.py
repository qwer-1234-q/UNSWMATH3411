import humman


def cal():
    s = "*" * 80
    print(s)
    print("asymmetric channel")
    print("plz retype if you type something wrong.")
    print("this function will not assume any errors")
    print("Only for A is unknown or B is unknown, could not both of A and B "
          "are unknown")
    print(s)
    print("plz enter one by one")
    N = int(input("number of input: "))
    source = addValue(N, "input", "", "a")
    M = int(input("number of output: "))
    output = addValue(M, "output", "", "b")
    print("input for P(bi|ai)")
    matrix = createM(N, M)
    source, output, matrix = fixValue(source, output, matrix, N, M)
    HA = Hvalue(source, N, "A")
    HB = Hvalue(output, M, "B")
    print(f"a = {source}")
    print(f"b = {output}")
    print(f"m = {matrix}")
    print(f"H(A) = {HA}")
    print(f"H(B) = {HB}")
    HBA = 0.0
    for i in range(len(source)):
        HCBA = conditonalEntropies(source, matrix, i, 'b', 'a')
        print(f'H(B|a{i + 1}) = {HCBA}')
        HBA += HCBA * source[i]
    print(f"H(B|A) = {round(HBA, 3)}")
    HAB = 0.0
    for i in range(len(output)):
        HCAB = conditonalEntropies(output, matrix, i, 'a', 'b')
        print(f'H(A|b{i + 1}) = {HCAB}')
        HAB += HCAB * output[i]
    print(f"H(A|B) = {round(HAB, 3)}")
    print(f'H(A, B) = H(B, A) = H(A) + H(B|A) = {round(HA + HBA, 3)} '
          f'= H(B) + H(A|B) = {round(HB + HAB, 3)}')
    
    
def addValue(N, s, k, t):
    empty = []
    l = []
    for n in range(N):
        a = input(f"P({t}{n + 1}{k}) = ")
        if a is not None and a != "":
            x, y = a.split("/")
            if x is not None and y is not None:
                a = int(x) / int(y)
            l.append(round(float(a), 5))
        else:
            empty.append(n)
            l.append(0.0)

    diff = 1
    if len(empty) == 1:
        for i in empty:
            for n in l:
                diff -= n
            l[i] = round(diff, 5)
        print(f"{s} done")
    elif len(empty) > 1:
        print(f"{s} more than one did not empty")
    else:
        print(f"put all the {s}")
    print(l)
    return l


def createM(row, col):
    m = []
    for r in range(row):
        a = f"|a{r + 1}"
        t = addValue(col, "matrix", a, "b")
        m.append(t)
    print(m)
    return m


def fixValue(source, output, matrix, N, M):
    sE, oE, mE = checkAllValue(source, output, matrix)
    if oE and mE == False:
        output = fixRow(output, matrix, source, N)
    if sE and mE == False:
        source = fixRow(source, matrix, output, M)

        
    sE, oE, mE = checkAllValue(source, output, matrix)
    if sE or oE or mE:
        return fixValue(source, output, matrix, N, M)
    return source, output, matrix


def fixRow(l, m, pro, N):
    for i in range(len(l)):
        if l[i]<= 0.0:
            b = 0.0
            for n in range(N):
                b += m[n][i] * pro[n]
            l[i] = round(b, 2)
    return l


def checkAllValue(source, output, matrix):
    sEmpty = checkEmpty(source)
    oEmpty = checkEmpty(output)
    mEmpty = False
    for N in matrix:
        a = checkEmpty(N)
        if a:
            mEmpty = a
    return sEmpty, oEmpty, mEmpty


def checkEmpty(l):
    for i in l:
        if i <= 0.0 or i is None or i == "":
            return True
    return False


def Hvalue(l, N, s):
    h = 0.0
    n = 0
    for i in l:
        fra = humman.hamFra(i, 2)
        h += fra
        print(f"H({s}){n + 1} is {fra}")
        n += 1
    return round(h, 3)


def conditonalEntropies(l, m, n, b, a):
    h = 0.0
    for i in range(len(l)):
        fra = humman.hamFra(m[n][i], 2)
        h += fra
        print(f"H({b}{i + 1}|{a}{n + 1}) is {fra}")
    return round(h, 3)


if __name__ == "__main__":
    cal()