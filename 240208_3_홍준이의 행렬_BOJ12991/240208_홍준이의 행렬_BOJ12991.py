# 홍준이의 행렬_BOJ12991

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())        # N 수열의 크기 / K 수열의 인덱스를 input 받고
lstA = list(map(int, input().split()))  # 수열 A를 리스트로 input 받고
lstA.sort()                             # 수열 A를 오름차순으로 정렬하고
lstB = list(map(int, input().split()))  # 수열 B를 리스트로 input 받는다
l = min(lstA) * min(lstB)               # 배열의 최소값을 저장하고
r = max(lstA) * max(lstB)               # 배열의 최대값을 저장한다
ans = 0                                 # 정답을 저장할 변수를 생성하고
while l <= r:                           # 최소값이 최대값 이상이 될 때까지 반복해서
    mid = (l+r)//2                      # 최대 최소 값의 중점을 저장하고
    tmp = 0                             # 중점 이하의 개수를 저장할 변수를 생성한다
    for b in lstB:                      # B 리스트를 반복해서
        num = mid//b                    # 중점을 b로 나눈 값을 num에 저장해서
        ll = 0                          # lstA의 왼쪽 인덱스를 생성하고
        rr = N-1                        # lstA의 오른쪽 인덱스를 생성해서
        while ll <= rr:                 # 왼쪽 인덱스가 오른쪽 인덱스 이상이 될때까지 반복한다
            mm = (ll+rr)//2             # 인덱스의 중점을 저장하고
            if lstA[mm] <= num:         # 인덱스의 중점이 num 이하라면
                ll = mm + 1             # 왼쪽 인덱스를 증가시키고
            else:                       # 인덱스의 중점이 num 미만이라면
                rr = mm - 1             # 오른쪽 인덱스를 감소시킨다
        else:                           # while문이 끝났다면
            tmp += (rr+1)               # b행의 num이하의 원소를 tmp에 더한다
    if tmp >= K:                        # tmp가 K개 이상이라면
        ans = mid                       # ans에 mid를 저장하고
        r = mid - 1                     # r을 감소시킨다
    else:                               # tmp가 K개 미만이라면
        l = mid + 1                     # l을 증가시킨다
print(ans)                              # N2 크기의 행렬에서 K번째로 작은 수의 값을 출력한다