# Crop Circles_BOJ5959

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                            # 소의 수를 input 받고
cows = [list(map(int, input().split())) for _ in range(N)]  # 소의 영역을 리스트 input 받고
ans = [0] * N                                               # 정답을 저장할 리스트를 생성한다
for n in range(N):                                          # N마리의 소를 반복하고
    for m in range(n+1, N):                                 # n 이후의 소를 반복해서
        if abs(cows[n][0]-cows[m][0])**2 + abs(cows[n][1]-cows[m][1])**2 <= abs(cows[n][2]+cows[m][2])**2:  # 두소의 영역이 겹친다면
            ans[n] += 1                                     # n번째 소에 겹치는 소를 추가하고
            ans[m] += 1                                     # m번째 소에 겹치는 소를 추가한다
for a in ans:                                               # 정답을 저장한 리스트를 반복해서
    print(a)                                                # 겹치는 소의 수를 출력한다