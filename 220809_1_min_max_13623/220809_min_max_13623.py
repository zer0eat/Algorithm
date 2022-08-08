# min/max_13623

# imput.txt 받기
import sys
sys.stdin = open('input.txt')

#input 리스트로 만들기
N = int(input())
for n in range(N):
    T = int(input())
    lst = list(map(int, input().split()))

    #최소 구하기
    mini = 1000000
    for t in range(T):
        if lst[t] < mini :
            mini = lst[t]
        else:
            pass
    #최대 구하기
    maxi = 0
    for t in range(T):
        if lst[t] > maxi:
            maxi = lst[t]
        else:
            pass
    print(f'#{n+1} {maxi-mini}')

