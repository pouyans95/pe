def solution(limit):
    return sum([x for x in range(limit) if x%3 == 0 or x%5 == 0])

limit = 1000
print (solution(limit))