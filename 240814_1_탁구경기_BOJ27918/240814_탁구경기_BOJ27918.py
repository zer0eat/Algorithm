# 탁구경기_BOJ27918

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 경기의 수를 input 받고
dal = 0                         # 달포의 점수를 저장할 변수를 생성하고
pho = 0                         # 포닉스의 점수를 저장할 변수를 생성한다
for n in range(N):              # 경기 수를 반복해서
    if input().strip() == 'D':  # 경기의 승자가 달포라면
        dal += 1                # 달포의 점수를 1 추가하고
    else:                       # 경기의 승자가 포닉스라면
        pho += 1                # 포닉스의 점수를 1 추가한다
    if abs(dal-pho) >= 2:       # 두 사람의 점수차가 2점 이상이라면
        break                   # 게임을 종료한다
print(f'{dal}:{pho}')           # 두 사람의 점수를 출력한다