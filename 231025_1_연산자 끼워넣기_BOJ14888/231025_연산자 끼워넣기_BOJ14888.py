# 연산자 끼워넣기_BOJ14888

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 연산할 숫자의 수를 input 받고
A = list(map(int, input().split()))                 # 연산할 숫자를 리스트로 저장하고
cal = list(map(int, input().split()))               # 연산할 연산자의 개수를 리스트(+,-,*,//)로 input 받는다

def dfs(idx, cul, ans):
    global maxans, minans                           # maxans, minans를 global 변수로 설정하고
    if visited[cul] + 1 > cal[cul]:                 # 연산의 개수가 주어진 연산의 수보다 많아지면
        return                                      # return 한다
    else:                                           # 연산의 개수가 주어진 연산의 수보다 같거나 작을 경우
        visited[cul] += 1                           # cul 연산의 수를 1 추가하고
        if cul == 0:                                # cul이 0인 경우
            ans2 = ans + A[idx+1]                   # ans2에 현재까지 연산결과에 다음 숫자를 더한 값을 저장한다
        elif cul == 1:                              # cul이 1인 경우
            ans2 = ans - A[idx + 1]                 # ans2에 현재까지 연산결과에 다음 숫자를 뺀 값을 저장한다
        elif cul == 2:                              # cul이 2인 경우
            ans2 = ans * A[idx + 1]                 # ans2에 현재까지 연산결과에 다음 숫자를 곱한 값을 저장한다
        else:                                       # cul이 3인 경우
            if ans < 0:                             # 현재까지 연산결과가 음수라면
                ans2 = -(abs(ans) // A[idx + 1])    # 현재까지 연산결과의 절대값에 다음 숫자를 나눈 몫을 음수로 만들어 ans2에 저장한다
            else:                                   # 현재까지 연산결과가 음수가 아니라면
                ans2 = ans // A[idx + 1]            # ans2에 현재까지 연산결과에 다음 숫자를 나눈 몫만 저장한다
        if visited == cal:                          # cal에 주어진 모든 연산을 수행했다면
            maxans = max(maxans, ans2)              # maxans에 연산값과 저장값 중 큰 값을 저장하고
            minans = min(minans, ans2)              # minans에 연산값과 저장값 중 작은 값을 저장하고
            visited[cul] -= 1                       # cul 연산의 수를 1 빼주고
            return                                  # return한다
        else:                                       # cal에 주어진 연산이 남아있다면
            for i in range(4):                      # 4가지 연산을 반복해서
                dfs(idx+1, i, ans2)                 # dfs 탐색을 통해 연산을 한다
            else:                                   # 4가지 연산을 모두 마쳤다면
                visited[cul] -= 1                   # cul 연산의 수를 1 빼주고
                return                              # return한다

visited = [0] * 4                                   # 연산한 연산자의 개수를 저장할 리스트를 생성하고
maxans = -1000000000                                # 연산의 최대값을 저장할 변수에 최소값인 -10억을 넣어 생성하고
minans = 1000000000                                 # 연산의 최소값을 저장할 변수에 최대값인 10억을 넣어 생성하고
ans = A[0]                                          # 연산 결과를 저장할 변수에 첫번째 숫자를 넣어 생성한다
for i in range(4):                                  # 4가지 연산을 반복해서
    dfs(0, i, ans)                                  # dfs 탐색을 통해 연산을 한다
print(maxans)                                       # 연산의 최대값을 출력하고
print(minans)                                       # 연산의 최소값을 출력한다