# 약수 구하기_BOJ2501

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())    # N 약수를 구할 수와 K 구하려는 약수의 순서를 input 받고
cnt = 0                             # 약수의 순서를 셀 변수를 생성하고
for n in range(1, N+1):             # 1부터 N까지 반복해서
    if N % n == 0:                  # N이 n으로 나누어 떨어진다면
        cnt += 1                    # 약수의 개수를 추가하고
    if cnt == K:                    # K번째 약수라면
        print(n)                    # K번째 약수를 출력하고
        quit()                      # 종료한다
print(0)                            # K번째 약수가 존재하지 않는다면 0을 출력한다