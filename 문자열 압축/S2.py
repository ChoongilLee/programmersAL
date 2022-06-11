
from tkinter import N


def solution(s):
    length_s = len(s)
    for i in range(1, length_s//2+1):
        n= i
        list_a = [0]
        k = 0
        while n < length_s-i+1:
            if s[n:n+i] == s[n-i:n]:
                list_a[k] += 1
                n += i
            else:
                n+=1
                k+=1
                list_a += [0]
    print(list_a)

test = input()
solution(test)


