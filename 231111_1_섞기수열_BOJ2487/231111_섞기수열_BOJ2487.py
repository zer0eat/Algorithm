# 섞기수열_BOJ2487

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 순열의 길이를 input 받고
A = list(map(int, input().split()))                 # 섞기 수열을 리스트로 input 받는다

def gcd(a, b):                                      # 유클리드 호제법으로 최대공약수를 구하기 위해
    while b:                                        # b가 0이 될때까지 반복해서
        a, b = b, a % b                             # a에는 b를 b에는 a를 b로 나눈 나머지를 저장하고
    return a                                        # b가 0일 때 a의 값을 return한다

def solve():
    global ans                                      # ans를 global변수로 선언하고
    for i in range(1, N+1):                         # 1부터 N까지 반복해서
        if visited[i] == 0:                         # i번째 수가 방문 전이라면
            cnt = 0                                 # 사이클을 돌 숫자를 셀 변수를 생성하고
            j = i                                   # j에 i를 저장하고
            while visited[j] == 0:                  # j가 방문한 곳이 나올 때까지 반복해서
                visited[j] = 1                      # j를 방문 표시하고
                cnt += 1                            # 사이클에 들어갈 숫자를 1 추가하고
                j = A[j-1]                          # j를 A[j-1]로 저장해서 다음 이동할 숫자로 바꿔준다
            else:                                   # 방문 표시한 j가 나왔다면
                ans = ans * cnt // gcd(ans, cnt)    # ans와 cnt를 곱한 후 두 수의 최대공약수로 나눠 두 수의 최대 공배수를 구한다

ans = 1                                             # 정답을 저장할 변수를 생성하고
visited = [0] * (N+1)                               # 방문기록을 할 리스트를 생성하고
solve()                                             # solve를 통해 궤적을 구하고
print(ans)                                          # 수열의 궤적을 출력한다