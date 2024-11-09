# 투표_BOJ10040

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # N 경기의 수 / M 심판의 수를 input 받고
score =[0]*N                        # 점수를 저장할 리스트를 생성하고
game = []                           # 비용을 저장할 리스트를 생성한다
for n in range(N):                  # 경기의 수를 반복해서
    game.append(int(input()))       # 게임별 비용을 input 받아 리스트에 append하고
for m in range(M):                  # 심판의 수를 반복해서
    judge = int(input())            # 비용 기준을 input 받고
    for n in range(N):              # 경기의 수를 반복해서
        if judge >= game[n]:        # 비용기준보다 낮은 게임이 나오면
            score[n] += 1           # 재미있는 게임으로 점수를 추가하고
            break                   # for문을 종료한다
print(score.index(max(score))+1)    # 가장 재미있는 게임의 번호를 출력한다