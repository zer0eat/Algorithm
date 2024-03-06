# 알파벳_BOJ1987

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
R, C = map(int, input().split())                                    # R 행의 길이 / C 열의 길이를 input 받고
board = [list(map(lambda x:ord(x)-65, input())) for _ in range(R)]  # 보드를 input 받고 알파벳을 숫자로 변경에서 저장한다
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]                              # 델타 탐색을 위한 리스트를 생성하고
ans = 0                                                             # 정답을 저장할 변수를 생성하고
tmp = {board[0][0] : 1}                                             # 시작점을 넣은 딕셔너리를 생성한다

def recur(dep, x, y):
    global ans                                                      # ans를 global 변수로 선언하고
    ans = max(dep, ans)                                             # 최대 칸수를 ans에 저장한다
    for t in range(4):                                              # 4방향 탐색을 반복해서
        r = x + d[t][0]                                             # 이동한 행을 저장하고
        c = y + d[t][1]                                             # 이동한 열을 저장해서
        if 0<=r<R and 0<=c<C and tmp.get(board[r][c]) == None:      # 이동한 곳이 보드 내에 있고 이동한 곳의 알파벳이 방문 전이라면
            tmp[board[r][c]] = 1                                    # 이동한 곳의 알파벳을 방문표시하고
            recur(dep+1, r, c)                                      # 이동한 곳부터 탐색하고
            tmp[board[r][c]] = None                                 # 이동한 곳의 알파벳을 방문표시 해제한다

recur(1, 0, 0)                                                      # 0,0 부터 지나갈 수 있는 칸을 탐색하고
print(ans)                                                          # 말이 지날 수 있는 최대의 칸 수를 출력한다