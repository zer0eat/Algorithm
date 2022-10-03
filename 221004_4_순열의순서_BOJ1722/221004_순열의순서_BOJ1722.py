# 순열의순서_BOJ1722

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def permutation1(a):
    global cnt1, flag1
    if flag1 == True:
        return
    if a == N:
        cnt1 += 1
        if cnt1 == inarr[0]:
            flag1 = True
            print(*arr[:])
        return
    for i in range(a,N):
        arr[i], arr[a] = arr[a], arr[i]
        permutation1(a+1)
        arr[i], arr[a] = arr[a], arr[i]

def permutation2(a):
    global flag2, cnt2
    if flag2 == True:
        return
    if a == N:
        cnt2 += 1
        if arr[:] == inarr:
            flag2 = True
            print(cnt2)
        return
    for i in range(a,N):
        arr[i], arr[a] = arr[a], arr[i]
        permutation2(a+1)
        arr[i], arr[a] = arr[a], arr[i]


# input 받기
N = int(sys.stdin.readline())
inarr = list(map(int, sys.stdin.readline().split()))

arr = [i for i in range(1, 1+N)]

A = inarr.pop(0)

if A == 1:
    cnt1 = 0
    flag1 = False
    permutation1(0)
else:
    cnt2 = 0
    flag2 = False
    permutation2(0)




