# 학번을 찾아줘_BOJ29807

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 과목의 수를 input 받고
score = list(map(int, input().split())) # 점수를 리스트로 input 받아서
for _ in range(5-T):                    # 안본 시험의 수만큼 반복해서
    score.append(0)                     # 0점을 추가한다
a1, a2, a3 = 0, 0, 0                    # 변수를 생성해서
if score[0] > score[2]:                 # 국어를 영어보다 잘봤다면
    a1 = (abs(score[0] - score[2]))*508 # 점수차에 508을 곱하고
else:                                   # 그렇지 않다면
    a1 = (abs(score[0] - score[2]))*108 # 점수차에 108을 곱하고
if score[1] > score[3]:                 # 수학을 탐구보다 잘봤다면
    a2 = (abs(score[1] - score[3]))*212 # 점수차에 212을 곱하고
else:                                   # 그렇지 않다면
    a2 = (abs(score[1] - score[3]))*305 # 점수차에 305을 곱하고
if T == 5:                              # 제2외국어를 봤다면
    a3 = score[4]*707                   # 점수에 707을 곱하고
print((a1+a2+a3)*4763)                  # 학번을 출력한다다