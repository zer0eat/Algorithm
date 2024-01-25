# 정렬_BOJ17074

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 배열의 크기를 input 받고
A = list(map(int, input().split()))     # 배열의 원소를 리스트로 input 받는다
A = [-10000000000] + A + [10000000000]  # 배열의 앞뒤에 가장 큰수와 가장 작은 수를 더해주고
ans = 0                                 # 정답을 저장할 변수를 생성하고
cnt = 0                                 # 정렬이 되지 않은 수를 셀 변수를 생성하고
tmp = 0                                 # 정렬이 되지 않은 수를 저장할 변수를 생성한다
for i in range(1, N+1):                 # 1부터 N까지 반복해서
    if A[i] < A[i-1]:                   # i번째 수가 이전 수보다 작다면
        cnt += 1                        # 정렬이 되지 않은 수를 1 추가하고
        tmp = i                         # i의 인덱스를 tmp에 저장한다
if cnt == 0:                            # 정렬 되지 않은 숫자가 없다면
    print(N)                            # N을 출력하고
elif cnt > 1:                           # 정렬 되지 않은 숫자가 2 이상이라면
    print(0)                            # 0을 출력한다
else:                                   # 정렬 되지 않은 숫자가 1개라면
    if A[tmp-2] <= A[tmp]:              # 정렬되지 않은 숫자가 2개 앞의 숫자보다 크다면
        ans += 1                        # 정답에 1을 추가하고
    if A[tmp-1] <= A[tmp+1]:            # 정렬되지 않은 숫자 앞뒤가 증가한다면
        ans += 1                        # 정답에 1을 추가한 후
    print(ans)                          # ans를 출력한다