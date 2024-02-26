# 도미노 찾기_BOJ1553

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
domino = [list(input().strip()) for _ in range(8)]      # 격자의 상태를 리스트로 input 받고
visited = [[0]*7 for _ in range(8)]                     # 방문표시를 할 리스트를 생성한다
ans = 0                                                 # 정답을 저장할 변수를 생성하고
dic = dict()                                            # 도미노의 사용여부를 확인할 딕셔너리를 생성하고
for i in range(7):                                      # 시작 숫자를 반복하고
    for j in range(i, 7):                               # 끝 숫자를 반복해서
        dic[str(i)+str(j)] = 0                          # 두숫자를 key로하는 원소를 생성한다
d = [[0,1], [1,0]]                                      # 오른쪽과 아래쪽으로 델타 탐색을 하기 위한 리스트를 생성한다

def recur(i, j):
    global ans                                          # ans를 global 변수로 선언하고
    if i == 8 and j == 0:                               # 도미노의 끝까지 탐색하여 모두 놓았다면
        ans += 1                                        # 정답을 1 추가하고
        return                                          # return한다
    if visited[i][j]:                                   # 방문표시가 되어 있다면
        if j == 6:                                      # i, j가 마지막 열에 있다면
            recur(i+1, 0)                               # 다음행으로 넘어가서 탐색을 진행하고
        else:                                           # i, j가 마지막 열에 있지 않다면
            recur(i, j+1)                               # 다음열로 넘어가서 탐색을 진행한다
    else:                                               # 방문표시가 되어있지 않다면
        for t in range(2):                              # 가로 세로 델타 탐색을 진행해서
            x = i + d[t][0]                             # 도미노의 행의 위치를 저장하고
            y = j + d[t][1]                             # 도미노의 열의 위치를 저장해서
            if 0<=x<8 and 0<=y<7:                       # 격자 안에 있다면
                if visited[x][y] == 0:                  # x,y가 방문 전이라면
                    tmp = [domino[i][j], domino[x][y]]  # 도미노의 숫자를 tmp에 저장하고
                    tmp.sort()                          # 오름차순으로 정렬한 뒤
                    if dic[tmp[0]+tmp[1]]:              # tmp[0]+tmp[1]의 도미노가 사용한 적이 있다면
                        pass                            # pass하고
                    else:                               # tmp[0]+tmp[1]의 도미노가 사용된 적이 없다면
                        visited[i][j] = 1               # i,j를 방문표시하고
                        visited[x][y] = 1               # x,y를 방문표시하고
                        dic[tmp[0]+tmp[1]] = 1          # tmp[0]+tmp[1]의 도미노를 사용표시하고
                        if j == 6:                      # i, j가 마지막 열에 있다면
                            recur(i+1, 0)               # 다음행으로 넘어가서 탐색을 진행하고
                        else:                           # i, j가 마지막 열에 있지 않다면
                            recur(i, j+1)               # 다음열로 넘어가서 탐색을 진행한다
                        visited[i][j] = 0               # i,j를 방문표시 해제하고
                        visited[x][y] = 0               # x,y를 방문표시 해제하고
                        dic[tmp[0]+tmp[1]] = 0          # tmp[0]+tmp[1]의 도미노를 사용표시를 해제한다

recur(0,0)                                              # 0,0 부터 도미노의 탐색을 시작한다
print(ans)                                              # 놓을 수 있는 경우의 수를 출력한다