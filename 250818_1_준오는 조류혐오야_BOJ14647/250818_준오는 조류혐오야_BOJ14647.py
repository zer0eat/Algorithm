# 준오는 조류혐오야_BOJ14647

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())            # 행과 열을 input받고
bingo = [list(map(int, input().split())) for n in range(N)] # 빙고 판을 Input받고
L = []                                      # 각 줄에 9의 수를 저장할 리스트를 생성하고
ans = 0                                     # 9의 개수를 저장할 변수를 생성한다
for n in range(N):                          # 행을 반복하고
    tmp = 0                                 # 각 행의 9의 수를 저장할 변수를 생성하고
    for m in range(M):                      # 열을 반복해서
        for j in list(str(bingo[n][m])):    # 해당 숫자를 반복해서
            if j == '9':                    # 9가 포함되어 있다면
                ans += 1                    # 전체 9의 개수를 추가하고
                tmp += 1                    # 행에 포함된 9의 개수를 추가한다
    L.append(tmp)                           # 행에 있는 9의 수를 리스트에 append한다
for m in range(M):                          # 열을 반복하고
    tmp = 0                                 # 각 열의 9의 수를 저장할 변수를 생성하고
    for n in range(N):                      # 행을 반복해서
        for j in list(str(bingo[n][m])):    # 해당 숫자를 반복해서
            if j == '9':                    # 9가 포함되어 있다면
                tmp += 1                    # 열에 포함된 9의 개수를 추가한다
    L.append(tmp)                           # 열에 있는 9의 수를 리스트에 append한다
print(ans-max(L))                           # 한줄을 제거했을 때 남아있는 9의 수를 출력한다