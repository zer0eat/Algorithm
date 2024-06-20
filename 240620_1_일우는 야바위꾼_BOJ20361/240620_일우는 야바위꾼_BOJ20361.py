# 일우는 야바위꾼_BOJ20361

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, X, K = map(int, input().split())         # N 컵의 개수 / X 숨긴 컵의 위치 / K 섞은 횟수를 input받고
ans = [0]*N                                 # 컵의 개수만큼 리스트의 원소를 생성하고
ans[X-1] = 1                                # X번째에 숨김표시를 한다
for k in range(K):                          # 섞은 횟수를 반복해서
    a, b = map(int, input().split())        # 두 컵의 위치를 input 받고
    ans[a-1], ans[b-1] = ans[b-1], ans[a-1] # 두 컵의 위치를 바꿔주고
for n in range(N):                          # 컵의 순서를 반복해서
    if ans[n] == 1:                         # n번째 컵에 숨겨져 있다면
        print(n+1)                          # 공이 숨겨진 컵의 위치를 출력하고
        break                               # for문을 break한다