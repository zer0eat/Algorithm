# K번째 수_BOJ1300

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 배열의 크기를 input 받고
K = int(input())                # 인덱스를 input 받는다
l = 1                           # 배열의 최소 수를 저장한 변수를 생성하고
r = N**2                        # 배열의 최대 수를 저장한 변수를 생성한다
ans = 0                         # 정답을 저장할 변수를 생성한다
while l <= r:                   # 최소수가 최대수 이상이 될 때까지 반복해서
    mid = (l+r)//2              # 최소 최대의 중점을 저장하고
    tmp = 0                     # mid 이하의 수를 저장할 변수를 생성한다
    for i in range(1, N+1):     # 행을 반복해서
        tmp += min(mid//i, N)   # i번째 행의 원소중 mid보다 작은수를 tmp에 더해준다
    if tmp >= K:                # tmp가 K개 이상이라면
        ans = mid               # K번째 인덱스가 될 수를 ans에 저장한다
        r = mid - 1             # 최대 수를 이동한다
    else:                       # tmp가 K개 미만이라면
        l = mid + 1             # 최소 수를 이동한다
print(ans)                      # B[k]를 출력한다