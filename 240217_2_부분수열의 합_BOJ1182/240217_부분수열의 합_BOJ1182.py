# 부분수열의 합_BOJ1182

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, S = map(int, input().split())        # N 정수의 수 / S 부분 수열의 합을 input 받고
lst = list(map(int, input().split()))   # 정수를 리스트로 input 받는다
ans = 0                                 # 합이 S가 되는 부분 수열을 저장할 변수를 생성한다

def recur(dep, start, tmp):
    global ans                          # global 변수로 선언하고
    if tmp and sum(tmp) == S:           # tmp가 비어있지 않고 합이 S라면
        ans += 1                        # 부분수열의 수를 1 추가한다
    if dep == N:                        # 깊이가 N이라면
        return                          # return한다
    for i in range(start, N):           # start부터 정수를 반복해서
        tmp.append(lst[i])              # i번째 정수를 append하고
        recur(dep+1, i+1, tmp)          # 깊이를 dep+1, i+1번째부터 탐색하고
        tmp.pop()                       # i번째 정수를 pop한다

recur(0, 0, [])                         # 깊이를 0, 0번째 색부터 탐색해서 합이 S가 되는 부분수열을 탐색한다
print(ans)                              # 합이 S가 되는 부분수열의 개수를 출력한다