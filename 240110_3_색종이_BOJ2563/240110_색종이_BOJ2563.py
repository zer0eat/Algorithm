# 색종이_BOJ2563

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 색종이의 수를 input 받고
visited = [[0]*100 for _ in range(100)]     # 도화지를 행렬로 생성한다
for n in range(N):                          # 색종이의 수를 반복해서
    x, y = map(int, input().split())        # 색종이의 왼쪽 아래의 점을 input 받고
    for i in range(x, x+10):                # 색종이의 세로의 크기를 반복하고
        for j in range(y, y+10):            # 색종이의 가로의 크기를 반복해서
            visited[i][j] = 1               # 도화지에 색종이가 붙은 곳에 표시를 한다
else:                                       # 모든 색종이를 반복한 후
    ans = 0                                 # 색종이가 붙은 면적을 저장할 변수를 생성하고
    for v in visited:                       # 도화지의 행을 반복해서
        ans += sum(v)                       # 색종이가 붙은 열의 수를 더해준 후
    print(ans)                              # 색종이가 붙은 영역의 넓이를 출력한다