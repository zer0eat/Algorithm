# 약수들의 합_BOJ9506

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                                            # break가 나올때까지 반복해서
    N = int(input())                                # 숫자를 input 받는다
    if N == -1:                                     # 숫자가 -1이라면
        break                                       # while문을 종료한다
    ans = []                                        # 약수를 저장할 리스트를 생성하고
    for n in range(1, N):                           # 1부터 N-1까지 반복해서
        if N%n == 0:                                # n이 N의 약수라면
            ans.append(n)                           # ans에 n을 append한다
    else:                                           # 모든 약수를 구했다면
        if N == sum(ans):                           # 약수의 합이 N과 같다면
            print(N, end=' ')                       # N을 출력하고
            for a in range(len(ans)):               # 약수를 반복해서
                if a == 0:                          # 맨 처음 약수라면
                    print(f'= {ans[a]}', end=' ')   # = 약수 를 출력하고
                elif a == len(ans)-1:               # 맨 마지막 약수라면
                    print(f'+ {ans[a]}')            # 약수만 출력하고
                else:                               # 중간에 나오는 약수라면
                    print(f'+ {ans[a]}', end=' ')   # + 약수 를 출력한다
        else:                                       # 약수의 합이 N과 다르다면
            print(f'{N} is NOT perfect.')           # N is NOT perfect. 를 출력한다.