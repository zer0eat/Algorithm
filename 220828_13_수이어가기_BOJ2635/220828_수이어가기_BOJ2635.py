# 수이어가기_BOJ2635

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())
i = 1
maxV = 0
maxlst = []
while i <= N:
    s = 0
    e = 1
    lst = [N, i]
    while lst[s] - lst[e] >= 0:
        lst.append(lst[s] - lst[e])
        s += 1
        e += 1
    else:
        i += 1
        if maxV < len(lst):
            maxV = len(lst)
            maxlst = lst

print(maxV)
print(*maxlst)

