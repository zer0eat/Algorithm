# 스타후르츠_BOJ17496

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, T, C, P = map(int, input().split())  # N 여름의 일수 / T 스타후르츠가 자라는데 걸리는 시간 / C 스타후르츠를 심을 수 있는 칸의 수 / P 스타후르츠 개당 가격을 input 받고
cnt = 0                                 # 키운 스타후르츠의 개수를 저장할 변수를 생성한다
n = 1                                   # 시작 일을 생성하고
while n < N:                            # 여름이 지나갈 때까지 반복해서
    if n + T <= N:                      # n일째 스타후르츠를 키워 수확할 수 있다면
        cnt += C                        # 수확한 스타후르츠의 수를 추가하고
        n += T                          # 수확한 날로 이동한다
    else:                               # 스타후르츠를 수확할 수 없다면
        break                           # while문을 break한다
print(cnt*P)                            # 스타후르츠를 팔아 벌 수 있는 수익을 출력한다