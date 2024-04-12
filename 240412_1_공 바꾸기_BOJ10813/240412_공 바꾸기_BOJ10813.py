# 공 바꾸기_BOJ10813

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                # N 바구니의 수 / M 공을 바꿀 번호를 input 받고
ball = []                                       # 공을 넣을 리스트를 생성한다
for n in range(1, N+1):                         # 1부터 N까지 반복해서
    ball.append(n)                              # 리스트에 공 번호를 append한다
for m in range(M):                              # 공을 바꿀 번호를 반복해서
    a, b = map(int, input().split())            # 교환할 공의 번호를 input 받고
    ball[a-1], ball[b-1] = ball[b-1], ball[a-1] # 두 공의 위치를 바꾼다
print(*ball)                                    # 바구니에 들어있는 공의 번호를 출력한다