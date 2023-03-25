# 수고르기_BOJ2230

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())        # N 수열의 길이 / M 두 수의 차가 넘어야하는 수
lst = [int(input()) for _ in range(N)]  # lst에 수열의 숫자를 모두 input 받고
lst.sort()                              # 오름차순으로 정렬한다

A = 0                                   # 수열의 맨 앞의 정수를 가르킨 A
B = 0                                   # 수열의 맨 앞의 정수를 가르킨 B

ans = 2000000001                        # 두 수열의 차가 M 이상의 최소값을 저장할 변수 생성
while A < N and B < N:                  # A와 B가 모두 수열의 길이를 초과하지 않은경우
    tmp = lst[B] - lst[A]               # B와 A가 가르키는 두 정수의 차를 tmp로 저장하고
    if tmp >= M:                        # tmp가 M보다 같거나 큰 경우 
        A += 1                          # A를 왼쪽으로 한칸 이동 시키고
        ans = min(ans, tmp)             # ans와 tmp 중 작은 값을 ans에 저장한다
    else:                               # tmp가 M보다 작은 경우
        B += 1                          # B를 왼쪽으로 한 칸 이동시킨다
print(ans)                              # while문이 종료되었다면 ans에 저장된 M 이상의 최소값을 출력한다