# 문자열비교_13753

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())
for t in range(T):
    N = list(input()) # 기준 문자열
    M = list(input()) # 비교할 문자열

    # N의 첫번째 문자가 M의 몇 번째 순서에 있는지 확인
    for i in range(len(M)):
        if M[i] == N[0]:
            # 첫 번째 문자열부터 끝까지 전부 다있으면 1을 출력하고 반복을 끝냄
            if N[0:len(N)] == M[i:i+len(N)]:
                print(f'#{t+1} 1')
                break
    # N이 M안에 없으면 0을 출력
    else:
        print(f'#{t + 1} 0')

