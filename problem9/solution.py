N = 1000
# a + b + c = N --> c = N - a - b
# a*2 + b*2 = c*2

for a in range(1,N):
    for b in range(a+1,N):
        c = N - a-b
        if a**2 + b**2 == c**2:
            print(a*b*c, (a,b,c))
            break