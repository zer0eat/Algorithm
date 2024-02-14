# 최대공약수 하나 빼기_BOJ14476

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def gcd(a,b):
    while b > 0:                        # b가 0이 될때까지 반복해서
        a, b = b, a%b                   # a를 b로 b를 a를 b로 나눈 나머지로 저장한다
    return a                            # b가 0이 되면 최대 공약수 a를 return한다

N = int(input())                        # 정수의 개수를 inpur 받고
lst = list(map(int, input().split()))   # 정수를 리스트로 input 받는다
left = [0]*N                            # 왼쪽부터 최대공약수를 저장하기 위한 리스트를 생성하고
left[0] = lst[0]                        # 처음 인덱스는 자기 자신과 공약수이므로 그대로 저장한다
right = [0]*N                           # 오른쪽부터 최대공약수를 저장하기 위한 리스트를 생성하고
right[-1] = lst[-1]                     # 마지막 인덱스는 자기 자신과 공약수이므로 그대로 저장한다
for i in range(1, N):                   # 두번째 원소부터 끝까지 반복해서
    left[i] = gcd(lst[i], left[i-1])    # i번째 원소와 그전까지 최대 공약수의 최대 공약수를 left 리스트에 저장한다
for j in range(N-2,-1,-1):              # 뒤에서 두번째 원소부터 맨 앞까지 반복해서
    right[j] = gcd(lst[j], right[j+1])  # j번째 원소와 그전까지 최대 공약수의 최대 공약수를 right 리스트에 저장한다
ans = []                                # 정답을 저장할 리스트를 생성하고
for i in range(N):                      # 정수의 개수를 반복해서
    if i == 0:                          # 맨 앞 정수를 뺀 최대공약수를 구한다면
        l = 0                           # 맨 앞보다 더 앞 최대공약수는 없으므로 0을 저장하고
        r = right[1]                    # 맨 왼쪽을 뺀 최대공약수를 저장한다
    elif i == N-1:                      # 맨 뒤 정수를 뺀 최대공약수를 구한다면
        l = left[-2]                    # 맨 오른쪽을 뺀 최대공약수와
        r = 0                           # 맨 뒤보다 더 뒤 최대공약수는 없으므로 0을 저장한다
    else:                               # i번째 정수를 뺀 최대공약수를 구한다면
        l = left[i-1]                   # 왼쪽부터 i-1까지 최대공약수와
        r = right[i+1]                  # 오른쪽부터 i+1까지 최대공약수를 저장하고
    res = gcd(l, r)                     # i번째 원소를 뺀 두 수의 최대공약수를 구하고
    if lst[i] % res != 0:               # i번째 원소가 두 최대공약수로 나누어지지 않는다면
        ans.append([res, lst[i]])       # ans에 최대공약수와 i번째 원소를 저장한다
ans.sort()                              # 정답을 오름차순으로 정렬하고
if ans:                                 # 정답이 있다면
    print(*ans[-1])                     # 가장 큰 최대공약수와 뺀 원소를 출력한다
else:                                   # 정답이 없다면
    print(-1)                           # -1을 출력한다