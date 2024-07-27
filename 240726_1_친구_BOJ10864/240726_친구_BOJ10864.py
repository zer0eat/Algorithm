# 친구_BOJ10864

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())        # N 사람의 수 / M 친구의 수를 input 받고
ans = [0]*N                             # 정답을 저장할 리스트를 생성한다
for m in range(M):                      # 친구의 수를 반복해서
    a, b = map(int, input().split())    # 친구 사이인 두명을 input 받고
    ans[a-1] += 1                       # a의 친구의 수를 1 더하고
    ans[b-1] += 1                       # b의 친구의 수를 1 더한다
for a in ans:                           # 사람의 수를 반복해서
    print(a)                            # 각 사람의 친구의 수를 출력한다 