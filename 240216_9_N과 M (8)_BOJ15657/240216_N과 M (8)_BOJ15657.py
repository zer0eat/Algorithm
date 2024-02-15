# N과 M (8)_BOJ15657

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())        # N 자연수의 수 / M 수열의 길이
lst = list(map(int, input().split()))   # N개의 자연수를 리스트로 input 받고
lst.sort()                              # 오름차순으로 정렬한다
ans = []                                # 수열을 저장할 리스트를 생성하고

def recur(dep, start):
    if dep == M:                        # M 깊이가 되었다면
        print(*ans)                     # 수열을 출력하고
        return                          # return해서 종료한다
    for i in range(start, N):           # start부터 자연수의 인덱스를 반복해서
        ans.append(lst[i])              # 수열 리스트에 i번째 자연수를 append하고
        recur(dep+1, i)                 # dep를 하나 늘려 i 인덱스부터 recur 함수로 탐색한 후
        ans.pop()                       # 수열 리스트에 i번째 자연수를 pop한다

recur(0, 0)                             # 0의 깊이, 0인덱스부터 recur함수로 탐색한다