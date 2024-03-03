# 색종이 붙이기_BOJ17136

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import copy

# input 받기
paper = [list(map(int, input().split())) for _ in range(10)]    # 10개의 줄에 종이의 각 칸에 적힌 수를 input 받고
ans = 1e9                                                       # 정답을 저장할 변수를 생성하고
dic = {1:0, 2:0, 3:0, 4:0, 5:0}                                 # 색종이의 수를 저장할 딕셔너리를 생성한다

def recur(dep, x, y, tmp):
    global ans                                                  # ans를 global 변수로 선언하고
    if dep >= ans:                                              # dep이 ans이상이 되면
        return                                                  # return한다
    if x == 10:                                                 # x가 10이면
        ans = min(ans, dep)                                     # ans와 dep 중 작은 값을 저장하고
        return                                                  # return한다
    if tmp[x][y] == 1:                                          # x,y에 1이 있다면
        for n in range(5, 0, -1):                               # 스티커의 크기를 5부터 1까지 반복해서
            if dic[n] == 5:                                     # 스티커를 5개 모두 사용했다면
                continue                                        # continue로 넘어간다
            if x+n > 10 or y+n > 10:                            # 스티커를 붙이면 종이를 넘어가게 된다면
                continue                                        # continue로 넘아간다
            flag = False                                        # flag를 False로 생성하고
            for i in range(n):                                  # 스티커의 행 크기를 반복해서
                if flag:                                        # flag가 True라면
                    break                                       # for문을 break한다
                for j in range(n):                              # 스티커의 열 크기를 반복해서
                    if tmp[x+i][y+j] == 0:                      # 해당 부붙에 스티커를 붙일 수 없다면
                        flag = True                             # flag를 True로 만들고
                        break                                   # for문을 break한다
            if flag == False:                                   # flag가 False일 때
                tmp2 = copy.deepcopy(tmp)                       # tmp를 복사한 리스트를 생성해서
                for i in range(n):                              # 행을 반복하고
                    for j in range(n):                          # 열을 반복해서
                        tmp2[x+i][y+j] = 0                      # 스티커를 붙인 표시를 하고
                if y != 9:                                      # y가 마지막 열이 아니라면
                    dic[n] += 1                                 # n 크기의 스티커를 1 추가하고
                    recur(dep+1, x, y + 1, tmp2)                # dep+1 깊이로 x,y+1 위치를 탐색한다
                    dic[n] -= 1                                 # n 크기의 스티커를 1 뺀다
                else:                                           # y가 마지막 열이라면
                    dic[n] += 1                                 # n 크기의 스티커를 1 추가하고
                    recur(dep+1, x + 1, 0, tmp2)                # dep+1 깊이로 x+1,0 위치를 탐색한다
                    dic[n] -= 1                                 # n 크기의 스티커를 1 뺀다
    else:                                                       # x,y에 0이 있다면
        if y != 9:                                              # y가 마지막 열이 아니라면
            recur(dep, x, y+1, tmp)                             # dep 깊이로 x,y+1 위치를 탐색한다
        else:                                                   # y가 마지막 열이라면
            recur(dep, x+1, 0, tmp)                             # dep 깊이로 x+1,0 위치를 탐색한다

recur(0, 0, 0, paper)                                           # 0 깊이로 0,0 위치를 탐색한다
if ans == 1e9:                                                  # ans가 1e9라면
    print(-1)                                                   # 스티커를 붙일 수 없으므로 -1을 출력하고
else:                                                           # ans가 1e9가 아니라면
    print(ans)                                                  # 스티커를 붙일 수 있으므로 필요한 최소 색종이 수를 출력한다