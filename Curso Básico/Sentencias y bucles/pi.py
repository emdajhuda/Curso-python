iter=int(input())
n=(range(0,iter))
print(n)
fracc=1.0
det=1.0
pi=1.0
for i in n:
    det = (i*2) + 3
    fracc = 1/det
    if (i%2) == 0:
        pi -= fracc
    else:
        pi += fracc
    print(pi)
pi*=4
print(pi)
