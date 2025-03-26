# 체스 초보 브실이_BOJ29725

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
white, black = 0, 0         # 점수를 저장할 변수를 생성하고
for c in range(8):          # 체스판을 반복해서
    chess = input().strip() # 체스의 상태를 input 받고
    for c in chess:         # 체스의 상태를 반복해서
        if c == 'K':        # 백 킹이라면
            white += 0      # 백팀에 0점을 추가한다
        elif c == 'k':      # 흑 킹이라면
            black += 0      # 흑팀에 0점을 추가한다
        elif c == 'Q':      # 백 퀸이라면
            white += 9      # 백팀에 9점을 추가한다
        elif c == 'q':      # 흑 퀸이라면
            black += 9      # 흑팀에 9점을 추가한다
        elif c == 'R':      # 백 룩이라면
            white += 5      # 백팀에 5점을 추가한다
        elif c == 'r':      # 흑 룩이라면
            black += 5      # 흑팀에 5점을 추가한다
        elif c == 'B':      # 백 비숍이라면
            white += 3      # 백팀에 3점을 추가한다
        elif c == 'b':      # 흑 비숍이라면
            black += 3      # 흑팀에 3점을 추가한다
        elif c == 'N':      # 백 나이트라면
            white += 3      # 백팀에 3점을 추가한다
        elif c == 'n':      # 흑 나이트라면
            black += 3      # 흑팀에 3점을 추가한다
        elif c == 'P':      # 백 폰이라면
            white += 1      # 백팀에 1점을 추가한다
        elif c == 'p':      # 흑 폰이라면
            black += 1      # 흑팀에 1점을 추가한다
print(white-black)          # 백팀과 흑팀의 점수 차를 출력한다