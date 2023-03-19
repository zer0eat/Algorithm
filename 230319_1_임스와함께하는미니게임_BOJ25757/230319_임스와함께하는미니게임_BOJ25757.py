# 임스와함께하는미니게임_BOJ25757

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, game = input().split()           # N 플레이를 신청한 횟수 / game 플레이할 게임
N = int(N)                          # 플레이어 신청한 횟수를 int로 바꾸고
if game == 'Y':                     # 플레이할 게임이 윷놀이라면
    player = 1                      # 임스를 제외한 1명이 있어야 플레이가 가능하기 때문에 player를 1로 저장
elif game == 'F':                   # 플레이할 게임이 같은 그림 찾기 라면
    player = 2                      # 임스를 제외한 1명이 있어야 플레이가 가능하기 때문에 player를 2로 저장
else:                               # 플레이할 게임이 원카드라면
    player = 3                      # 임스를 제외한 1명이 있어야 플레이가 가능하기 때문에 player를 3로 저장

visited = dict()                    # 참여한 플레이어인지 확인할 딕셔너리를 생성하고
ans = 0                             # 임스가 플레이한 횟수를 저장할 변수 생성
tmp = 0                             # 플레이어가 모두 모였는지 확인할 변수 생성
for _ in range(N):                  # 플레이를 신청한 횟수를 반복해서
    id = input().strip()            # id를 input 받고
    if visited.get(id) == None:     # 참가자 명단에 아직 id가 없다면
        visited[id] = 1             # 참가자 명단에 참여표시를 하고
        tmp += 1                    # 플레이어의 수를 확인할 변수에 추가한다
        if tmp == player:           # 만약 플레이어가 모두 모였다면
            ans += 1                # 플레이한 횟수를 1 추가하고
            tmp = 0                 # 플레이어를 확인할 변수를 0으로 초기화한다
print(ans)                          # 플레이 신청한 횟수를 모두 탐색했다면 정답을 출력한다