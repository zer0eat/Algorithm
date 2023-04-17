# 동전_BOJ9084

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):                              # 테스트 케이스를 반복해서
    N = int(input())                            # 동전의 수를 input
    coin = list(map(int, input().split()))      # 동전의 금액을 리스트 형태로 input
    M = int(input())                            # 동전의 합을 input

    visited = [0] * (M+1)                       # 방문표시할 리스트 생성
    visited[0] = 1                              # 동전이 아무것도 없을 경우의 수는 1이므로 인덱스 0에 1을 표시

    for c in coin:                              # 동전의 금액을 반복해서
        for i in range(M + 1):                  # 동전의 합까지 반복하여
            if i >= c:                          # 구하고자 하는 동전의 합이 c보다 같거나 커지면
                visited[i] += visited[i - c]    # 구하고자 하는 동전의 합을 인덱스로 하는 원소에 [동전의합 - 동전의 금액]에 적혀있는 경우의 수를 더한다
    print(visited[M])                           # 모든 반복을 마쳤다면 구하고자 하는 동전의 합의 경우의 수를 출력한다