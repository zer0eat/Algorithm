# 최후의승자는누구_BOJ12760

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())            # N 플레이어의 수 / M 카드의 수

game = []                                   # 플레이어가 가지고 있는 카드를 저장할 리스트 생성
for _ in range(N):                          # 플레이어의 수를 반복해서
    A = list(map(int, input().split()))     # A에 카드의 번호를 리스트 형태로 input 받고
    A.sort(reverse=True)                    # A를 내림차순으로 정렬한 후
    game.append(A)                          # game에 A를 append

score = [0]*N                               # 일등한 게임을 저장할 리스트 생성
for j in range(M):                          # 카드의 수를 반복해서
    maxscore = 0                            # 해당 게임에서 가장 큰 점수를 저장할 변수 생성
    player = []                             # 해당 게임에서 가장 큰 점수를 낸 player를 저장할 list 생성
    for i in range(N):                      # 플레이어의 수를 반복해서
        if game[i][j] > maxscore:           # 해당 플레이어가 낸 카드가 maxscore보다 크다면
            maxscore = game[i][j]           # maxscore를 해당 플레이어가 낸 카드로 갱신
            player = [i]                    # player에 해당 플레이어를 넣은 리스트로 저장
        elif game[i][j] == maxscore:        # 해당 플레이어가 낸 카드가 maxscore와 같다면
            player.append(i)                # player에 해당 플레이어를 append
    else:                                   # 모든 플레이어가 카드를 냈다면
        for p in player:                    # player 리스트를 반복해서
            score[p] += 1                   # score에 일등한 게임의 수를 추가한다
else:                                       # 모든 게임을 마쳤다면
    maxscore = 0                            # 가장 많이 이긴 게임의 수를 저장할 변수를 생성
    ans = []                                # 가장 많이 이긴 플레이어를 저장할 리스트를 생성
    for s in range(N):                      # 플레이어의 수를 반복해서
        if score[s] > maxscore:             # 해당 플레이어가 maxscore보다 많이 이겼다면
            maxscore = score[s]             # maxscore를 해당 플레이어가 이긴 횟수로 저장하고
            ans = [s+1]                     # ans에 플레이어 넘버를 넣은 list로 저장
        elif score[s] == maxscore:          # 해당 플레이어가 maxscore만큼 이겼다면
            ans.append(s+1)                 # ans에 플레이어의 넘버를 append
    else:                                   # 플레이어의 수를 모두 반복했다면
        print(*ans)                         # ans를 출력한다