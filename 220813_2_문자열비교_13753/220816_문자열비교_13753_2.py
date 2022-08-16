# 문자열비교_13753_슬라이싱 없이 풀기

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())
for t in range(T):
    N = list(input()) # 기준 문자열
    M = list(input()) # 비교할 문자열

    # N의 첫번째 문자가 M의 몇 번째 순서에 있는지 확인
    x = 0
    v = 0
    i = 0
    while i < len(M) - len(N) + 1:
        if N[v] != M[i + v]:
            x = 0
            v = 0
            i += 1
        elif N[v] == M[i + v]:
            x += 1
            v += 1
            if len(N) == x:
                print(f'#{t + 1} 1')
                break

    # N이 M안에 없으면 0을 출력
    else:
        print(f'#{t + 1} 0')

