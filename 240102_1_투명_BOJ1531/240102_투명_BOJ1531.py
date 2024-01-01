# 투명_BOJ1531

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                # N 불투명한 종이의 수 / M 가려도 보이는 종이의 수
visited = [[0]*100 for _ in range(100)]         # 종이로 가려진 부분을 표시하기 위한 리스트를 생성하고
for n in range(N):                              # 불투명한 종이의 수를 반복해서
    x1, y1, x2, y2 = map(int, input().split())  # 종이의 왼쪽 상단과 오른쪽 하단의 좌표를 input 받고
    for i in range(x1-1, x2):                   # 종이의 행을 반복하고
        for j in range(y1-1, y2):               # 종이의 열을 반복해서
            visited[i][j] += 1                  # 가려진 부분을 표시한다
ans = 0                                         # 가려진 부분의 수를 셀 변수를 생성하고
for i in range(100):                            # 그림 전체의 행을 반복하고
    for j in range(100):                        # 그림 전체의 열을 반복해서
        if visited[i][j] > M:                   # 해당 부분이 종이에 가려져 보이지 않는다면
            ans += 1                            # 가려진 부분의 수를 1 추가한다
print(ans)                                      # 가려진 부분의 수를 출력한다