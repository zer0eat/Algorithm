# 크면서 작은 수_BOJ2992

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
X = input().strip()                     # 정수를 input받고
lst = list(X)                           # 정수의 각 자리수를 원소로 리스트로 저장한다
visited = [0]*len(X)                    # 원소의 방문표시를 할 리스트를 생성하고
X = int(X)                              # X를 int로 저장한 후
ans = 1e9                               # 정답을 저장할 변수를 생성한다

def recur(dep, tmp):
    global ans                          # ans를 global 변수로 선언하고
    if dep == len(lst):                 # 모든 수를 조합했다면
        if X < int(tmp):                # X보다 큰 수가 나왔을 경우에
            ans = min(int(tmp), ans)    # ans에 X보다 큰 가장 작은 수를 저장하고
        return                          # return 한다
    for i in range(len(lst)):           # X의 수를 반복해서
        if visited[i]:                  # i를 사용했다면
            continue                    # continue로 넘어간다
        visited[i] = 1                  # i번째 원소를 방문표시하고
        recur(dep+1, tmp+lst[i])        # 깊이 dep+1부터 X보다 큰 수를 탐색한다
        visited[i] = 0                  # i번째 원소를 방문표시하고

recur(0, '')                            # 깊이 0부터 X보다 큰 수를 탐색한다
if ans == 1e9:                          # X보다 큰 가장 작은 수가 없다면
    print(0)                            # 0을 출력한다
else:                                   # X보다 큰 가장 작은 수가 있다면
    print(ans)                          # X보다 큰 가장 작은 수를 출력한다