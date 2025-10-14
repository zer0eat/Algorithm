# 큰 수 구성하기_BOJ18511

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())    # 기준 숫자와 사용할 숫자를 input받고
L = list(map(int,input().split()))  # 사용할 숫자들의 리스트를 input받고
ans = 0                             # 정답을 저장할 변수를 생성한다

def dfs(num):                       # 함수를 선언하고
    global ans                      # 변수를 global로 만들고
    if num > N:                     # 현재 수가 기준 수를 넘는다면
        return                      # 함수를 return한다
    ans = max(ans, num)             # 정답과 현재 숫자중 더 큰 수를 저장하고
    for l in L:                     # 숫자리스트를 반복해서
        tmp = num*10+l              # 다음숫자를 만들어서
        dfs(tmp)                    # 다음 함수를 탐색한다

dfs(0)                              # 0부터 함수를 탐색해서
print(ans)                          # 정답을 출력한다