# 합구하기_BOJ11441

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 수의 개수
lst = list(map(int, input().split()))   # 수를 lst에 리스트 형태로 input 받고
lst = [0] + lst                         # lst의 맨 앞 원소에 0을 넣어준다

for i in range(1, N+1):                 # lst의 원소를 반복해서
    lst[i] += lst[i-1]                  # 현재 원소에 이전 원소를 더해준다

M = int(input())                        # 누적합을 구할 수를 input 받고
for _ in range(M):                      # 누적합을 구할 수를 반복해서
    a, b = map(int, input().split())    # a 시작점 b 끝점의 수를 input 받고 
    print(lst[b]- lst[a-1])             # a와 b사이의 합을 출력한다