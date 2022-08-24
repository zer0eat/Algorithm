# 회전문제_13971

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):                              # 테스트 케이스만큼 반복
    N, M = list(map(int, input().split()))      # N = lst 요소의 수 / M = 맨 앞의 숫자를 맨 뒤로 보내는 작업을 반복할 횟수
    lst = list(map(int, input().split()))       # N개의 요소가 들어있는 숫자열

    for i in range(M):                          # M만큼 반복할 때
        lst.append(lst.pop(0))                  # 맨앞의 숫자를 빼서 맨 뒤로 보냄

    print(f'#{t+1}', lst[0])                    # 작업을 M번 실행 후 맨 앞의 숫자 출력