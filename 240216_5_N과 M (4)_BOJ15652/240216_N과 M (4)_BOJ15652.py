# N과 M (4)_BOJ15652

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # N 자연수의 수 / M 수열의 길이
ans = []                            # 수열을 저장할 리스트를 생성한다

def recur(dep, start):
    if dep == M:                    # M 깊이가 되었다면
        print(*ans)                 # 수열을 출력하고
        return                      # return해서 종료한다
    for i in range(start, N+1):     # start부터 자연수를 반복해서
        ans.append(i)               # 수열 리스트에 i를 append하고
        recur(dep+1, i)             # dep를 하나 늘려, i부터 recur 함수로 탐색한 후
        ans.pop()                   # 수열 리스트에 i를 pop한다

recur(0, 1)                         # 0의 깊이, 1부터 recur함수로 탐색한다