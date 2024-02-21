# N-Queen_BOJ9663

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # Queen의 개수를 input 받고
chess = [0]*N               # 체스를 놓을 수를 저장할 리스트를 생성하고
ans = 0                     # 정답을 저장할 변수를 생성한다

def queen(dep):
    for i in range(dep):    # dep까지 행을 반복해서
        if chess[i] == chess[dep] or abs(chess[i]-chess[dep]) == abs(i-dep):    # 열이 겹치거나 대각선으로 겹치면
            return False    # False를 return하고
    return True             # 겹치는게 없다면 True를 return한다

def recur(dep):
    global ans, N           # ans와 N을 global로 선언하고
    if dep == N:            # 깊이가 N이 되면
        ans += 1            # 정답을 1개 추가하고
        return              # return한다
    for j in range(N):      # 체스를 놓을 열을 반복해서
        chess[dep] = j      # dep 행에 j 열에 놓았다고 저장하고
        if queen(dep):      # 겹치는지 확인하여 겹치지 않는 경우
            recur(dep+1)    # 다음 행의 체스를 놓는 경우를 탐색한다
    
recur(0)                    # 0번 열부터 체스말을 놓으면서 N개의 queen을 놓을 수 있는 경우를 탐색한다
print(ans)                  # N개의 queen을 서로 공격할 수 없게 놓을 수 있는 경우를 출력한다