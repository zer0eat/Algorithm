# 랜선자르기_BOJ1654

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
K, N = map(int, input().split())            # K 케이블의 수 / N 만들어야하는 케이블의 수를 input 받고
cable = [int(input()) for _ in range(K)]    # 케이블의 길이를 리스트로 input 받는다
ans = 0                                     # 정답을 저장할 변수를 생성하고
l = 1                                       # 케이블의 최소길이를 저장한 변수를 생성하고
r = max(cable)                              # 케이블의 최대길이를 저장한 변수를 생성한다
while l <= r:                               # 최소 길이가 최대 길이보다 같거나 커질때까지 반복해서
    mid = (l+r)//2                          # 최대와 최소의 중점을 저장하고
    tmp = 0                                 # 만들 수 있는 케이블의 수를 저장할 변수를 생성한다
    for i in cable:                         # 케이블의 수를 반복해서
        tmp += i//mid                       # mid길이로 만들 수 있는 케이블의 수를 더해준다
    if tmp >= N:                            # 만들 수 있는 케이블의 수가 N개 이상이라면
        ans = max(ans, mid)                 # 현재 길이와 저장된 길이 중 더 큰 값을 저장하고
        l = mid + 1                         # 최소길이를 늘려준다
    else:                                   # 만들 수 있는 케이블의 수가 N개 미만이라면
        r = mid - 1                         # 최대길이를 줄여준다
print(ans)                                  # N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다