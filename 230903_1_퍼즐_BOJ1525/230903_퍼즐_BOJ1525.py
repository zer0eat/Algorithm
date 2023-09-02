# 퍼즐_BOJ1525

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
def bfs():
    while q:                                            # q가 빌 때까지 반복해서
        now = q.popleft()                               # q에 저장된 puzzle 상태를 popleft로 꺼내서
        if now == "123456780":                          # 123456780으로 정렬된 상태라면
            return cnt[now]                             # 현재 횟수를 return 한다
        loc = now.index("0")                            # 0의 인덱스를 저장하고
        i = loc // 3                                    # 0의 행과
        j = loc % 3                                     # 0의 열을 저장한다
        for k in range(4):                              # 4방향으로 이동하여
            x = i + d[k][0]                             # 이동할 퍼즐의 행을 저장하고
            y = j + d[k][1]                             # 이동할 퍼즐의 열을 저장한다
            if 0 <= x < 3 and 0 <= y < 3:               # 이동할 퍼즐이 퍼즐 내에 위치한다면
                switch_loc = x * 3 + y                  # 바꿀 위치를 문자열의 인덱스로 바꿔준다
                puzzle_move = list(now)                 # 현재 상태를 리스트로 만들고
                puzzle_move[switch_loc], puzzle_move[loc] = puzzle_move[loc], puzzle_move[switch_loc]   # 0과 바꿀 퍼즐을 교환해주고
                puzzle_move = "".join(puzzle_move)      # 바꾼 상태를 문자열로 바꿔준다
                if cnt.get(puzzle_move) == None:        # 바꾼 퍼즐 상태가 방문 전이라면
                    q.append(puzzle_move)               # q에 바꾼 퍼즐 상태를 append 한다
                    cnt[puzzle_move] = cnt[now] + 1     # 바꾼 퍼즐까지 이동 횟수를 cnt에 1을 더해 저장한다
puzzle = ""                                     # 퍼즐을 저장할 변수를 생성하고
for _ in range(3):                              # 퍼즐의 행을 반복해서
    puzzle += ''.join(list(input().split()))    # 퍼즐의 행을 input받아 저장한다
d = [[0,1], [0,-1], [1,0], [-1,0]]              # 우좌상하 이동을 하기위한 리스트를 생성하고
q = deque()                                     # deque를 생성하여
q.append(puzzle)                                # input받은 퍼즐을 q에 저장한다
cnt = dict()                                    # 이동 횟수를 저장할 딕셔너리를 생성하고
cnt[puzzle] = 0                                 # puzzle 상태일 때 이동 횟수를 0으로 저장한다
ans = bfs()                                     # bfs 탐색으로 퍼즐을 정렬한다
if ans == None:                                 # ans가 없다면
    print(-1)                                   # 퍼즐을 완성할 수 없으므로 -1을 출력하고
else:                                           # ans가 있다면
    print(ans)                                  # 최소 이동 횟수를 출력한다