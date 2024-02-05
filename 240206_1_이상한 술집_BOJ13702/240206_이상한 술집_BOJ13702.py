# 이상한 술집_BOJ13702

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())            # N 막걸리 주전자의 수 / K 친구들의 수를 input 받고
alcohol = [int(input()) for _ in range(N)]  # 주전자의 용량을 리스트로 input 받고
l = 1                                       # 주전자의 최소 용량을 저장하고
r = max(alcohol)                            # 주전자의 최대 용량을 저장해서
if r == 0:                                  # 주전자의 최대 용량이 0 이라면
    print(0)                                # 0을 출력하고
    quit()                                  # 종료한다
ans = 0                                     # 정답을 저장할 변수를 생성하고
while l <= r:                               # 주전자의 최소용량이 최대용량과 같거나 커질때까지 반복해서
    mid = (l+r)//2                          # 두 용량의 중간점을 저장하고
    tmp = 0                                 # 나눠줄 수 있는 수를 저장할 변수를 생성하고
    for al in alcohol:                      # 주전자의 용량을 반복해서
        tmp += al//mid                      # 나눠줄 수 있는 잔의 수를 tmp에 저장한다
    if tmp < K:                             # tmp가 K보다 작다면
        r = mid - 1                         # 최대용량을 줄이고
    else:                                   # tmp가 K와 같거나 작다면
        ans = max(ans, mid)                 # ans에 용량을 저장하고
        l = mid + 1                         # 최소용량을 늘린다
print(ans)                                  # K명에게 나눠줄 수 있는 최대 용량을 출력한다