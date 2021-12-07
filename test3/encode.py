

def matrix(row, store):
    m = []
    for r in range(row):
        a = []
        N = store[r]
        if r != 0:
            pre = store[r - 1]
        else:
            pre = 0
        a = code(m, pre, N, r)
        if a is None:
            m = None
            print("not coding")
            break
        m.append(a)

    print(m)
    k = []
    if m is not None:
        for r in range(row):
            N = store[r]
            s = ""
            for n in range(N):
                s += str(m[r][n])
            print(f'p{r + 1} -- {s}')
            k.append(s)
    return k


def code(m, pre, N, r):
    a = []
    change = True
    for n in range(N):
        if pre == 0:
            a.append(0)
        elif change:
            if pre == n + 1 and m[r - 1][n] == 0:
                a.append(1)
                change = False
            elif pre == n + 1 and m[r - 1][n] == 1:
                if m[r - 1][0] != 1:
                    a = []
                    a.append(1)
                    change = False
                    for i in range(1, N):
                        a.append(0)
                else:
                    a = None
                    break
            elif pre < n + 1:
                change = False
                a.append(0)
            else:
                a.append(m[r - 1][n])
        else:
            a.append(0)
    
    return a


def matrix_Shannon(row, store, logg):
    m = []
    for r in range(row):
        a = []
        N = store[r]
        if r != 0:
            pre = store[r - 1]
        else:
            pre = 0
        a = code_Shannon(m, pre, N, r, logg)
        if a is None:
            m = None
            print("not coding")
            break
        m.append(a)
    
    print(m)
    k = []
    if m is not None:
        for r in range(row):
            N = store[r]
            s = ""
            for n in range(N):
                s += str(m[r][n])
            print(f'p{r + 1} -- {s}')
            k.append(s)
    return k


def code_Shannon(m, pre, N, r, logg):
    a = []
    change = True
    for n in range(N):
        if pre == 0:
            a.append(0)
        elif change:
            if pre == n + 1:
                b = m[r - 1][n]
                if b + 1 < logg:
                    a.append(b + 1)
                elif b + 1 == logg:
                    if m[r - 1][0] + 1 < logg:
                        a = []
                        a.append(m[r - 1][0] + 1)
                        change = False
                        for i in range(1, N - 1):
                            a.append(0)
                    else:
                        a = None
                        break
            elif pre < n + 1:
                change = False
                a.append(0)
            else:
                a.append(m[r - 1][n])
        else:
            a.append(0)
    
    return a
