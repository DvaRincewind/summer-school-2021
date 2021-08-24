def task0():
    print(""*(int(bool(exec("s=input()"))) + int(bool(exec("setS=set()"))) + int(bool([setS.add(i) for i in s if s.count(i) > 1]))), len(set(s) - setS), "\n", "".join(list(set(s) - setS)), sep="")

def task2():
    p = sorted([int(input()) for j in range(3)])
    print(p[-1], p[0], p[1], sep="\n")

def task3():
    d = {i: 0 for i in range(7, -1, -1)}
    s = [int(i) for i in input().split()]
    for i in range(2, len(s)):
        o = ''
        for j in [2, 1, 0]:
            k = '+' if s[i-j] >= 0 else '-'
            o = 0 + k
        d[o] = d[o] + 1
    for key, val in d.items():
        print(key+':', val)

while 1:
    task0()
