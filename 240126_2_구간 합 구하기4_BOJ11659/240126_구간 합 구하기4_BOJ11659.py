# 구간 합 구하기4_BOJ11659

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())        # N 수의 개수 / M 합을 구해야하는 횟수를 input 받고
lst = list(map(int, input().split()))   # 수를 리스트로 input 받는다
ans = [0]*(N+1)                         # 수들의 합을 저장할 리스트를 생성하고
for n in range(1, N+1):                 # 1부터 N까지 반복해서
    ans[n] = ans[n-1] + lst[n-1]        # n까지의 누적합을 ans의 n번 인덱스에 저장한다
for m in range(M):                      # 합을 구해야하는 수를 반복해서
    s, e = map(int, input().split())    # 합을 구하는 구간의 시작과 끝을 input 받고
    print(ans[e]-ans[s-1])              # s부터 e까지 합을 출력한다