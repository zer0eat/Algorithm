# 색종이 만들기_BOJ2630

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                # 종이의 한변의 길이를 input 받고
paper = [list(map(int, input().split())) for _ in range(N)]     # 종이의 색상을 input 받는다
visited = [[0]*N for _ in range(N)]                             # 색종이의 개수를 센 곳을 방문표시할 리스트를 생성하고
w, b = 0, 0                                                     # 햐얀색과 파란색 색종이의 개수를 저장할 변수를 생성하고
l = N                                                           # 색종이의 크기를 l에 저장한다
while l > 0:                                                    # l이 0이 될때까지 반복해서
    for i in range(0, N, l):                                    # 색종이의 행의 크기를 l만큼 건너뛰며 반복하고
        for j in range(0, N, l):                                # 색종이의 열의 크기를 l만큼 건너뛰며 반복해서
            if visited[i][j] == 0:                              # 색종이의 왼쪽 상단 모서리가 방문 전이라면
                s = paper[i][j]                                 # 왼쪽 상단 모서리의 색을 s에 저장한다
                flag = False                                    # 잘라진 색종이 여부를 체크할 변수를 생성하고
                for p in range(l):                              # 자른 색종이의 크기만큼 행을 반복하고
                    if flag:                                    # flag가 Ture일 때
                        break                                   # for문을 break 하고
                    for q in range(l):                          # 자른 색종이의 크기만큼 열을 반복해서
                        if s != paper[i+p][j+q]:                # 해당 위치가 s와 색이 다르다면 제대로 잘린 색종이가 아니므로
                            flag = True                         # flag를 True로 바꾸고
                            break                               # for문을 break한다
                if flag == False:                               # flag가 False라면 i,j에서 시작하는 l크기의 색종이가 있으므로
                    if s == 0:                                  # s가 0일 때는
                        w += 1                                  # 흰색을 추가하고
                    else:                                       # s가 1일 때는
                        b += 1                                  # 파랜색을 추가한다
                    for x in range(l):                          # 자른 색종이의 크기만큼 행을 반복하고
                        for y in range(l):                      # 자른 색종이의 크기만큼 열을 반복해서
                            visited[i+x][j+y] = 1               # 개수를 센 색종이를 방문표시한다
    else:                                                       # 색종이의 행의 크기를 l만큼씩 모두 반복했다면
        l //= 2                                                 # l의 크기를 반으로 줄인다
print(w)                                                        # 햐얀색 색종이의 개수를 출력하고
print(b)                                                        # 파란색 색종이의 개수를 출력한다