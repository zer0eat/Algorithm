# 좋은 날 싫은 날_BOJ17211

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, now = map(int, input().split())          # N 날짜 / now 현재 기분을 input 받고
feels = list(map(float, input().split()))   # 기분에 따른 다음날 기분을 확률로 input 받는다
if now:                                     # 현재 기분이 나쁘다면
    good, bad = 0, 1                        # good을 0 bad를 1로 변수를 생성한다
else:                                       # 현재 기분이 좋다면
    good, bad = 1, 0                        # good을 1 bad를 0으로 변수를 생성한다
for n in range(N):                          # N일간을 반복해서
    y_good = good                           # 좋은 날일 확률을 새로운 변수에 저장하고
    good = y_good*feels[0] + bad*feels[2]   # good에 내일 기분이 좋을 확률을 저장하고
    bad = y_good*feels[1] + bad*feels[3]    # bad에 내일 기분이 좋지 않을 확률을 저장한다
print(int(good*1000))                       # 기분이 좋은 날일 확률에 1000을 곱해 출력하고
print(int(bad*1000))                        # 기분이 싫은 날일 확률에 1000을 곱해 출력한다