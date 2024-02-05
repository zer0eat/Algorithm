# 나무자르기_BOJ2805

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())        # N 나무의 수 / M 가져갈 나무의 길이를 input 받고
woods = list(map(int, input().split())) # 나무의 길이를 리스트로 input 받는다
l = 1                                   # 나무의 최소 길이를 저장할 변수를 생성하고
r = max(woods)                          # 나무의 최대 길이를 저장할 변수를 생성한다
while l <= r:                           # 나무의 최소길이가 최대길이와 같거나 커질 때까지 반복해서
    mid = (l+r)//2                      # 나무 길이의 중점을 저장하고
    tmp = 0                             # 가져갈 수 있는 나무의 길이를 저장할 변수를 생성하고
    for wood in woods:                  # 나무의 길이를 반복해서
        if wood - mid > 0:              # 나무를 잘랐을 때 길이가 양수라면
            tmp += (wood - mid)         # tmp에 자른 나무 길이를 더한다
    if tmp == M:                        # tmp가 M만큼 잘렸다면
        print(mid)                      # 자른 길이를 출력하고
        quit()                          # 종료한다
    if tmp < M:                         # tmp가 M보다 짧다면
        r = mid - 1                     # 최대 길이를 줄여준다
    else:                               # tmp가 M보다 크다면
        l = mid + 1                     # 최소 길이를 늘려준다
print(r)                                # 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다