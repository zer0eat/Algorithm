# GCD합_BOJ9613

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def gcd(a, b):                              # 유클리드 호제법을 사용한 gcd함수
    while b > 0:                            # b가 0보다 크면 반복해서
        a, b = b, a%b                       # a에 b를 저장하고 b에 a를b로 나눈 나머지를 저장한다
    return a                                # b가 0일 때 a를 리턴해서 gcd를 구한다

T = int(input())                            # 테스트 케이스를 input 받고
for t in range(T):                          # 테스트 케이스를 반복해서
    N = list(map(int, input().split()))     # 숫자의 개수와 수 정보를 input받고
    ans = 0                                 # gcd의 합을 저장할 변수를 생성한다
    for a in range(1, N[0]+1):              # 수 정보를 반복하고
        for b in range(a+1, N[0]+1):        # a보다 큰 수를 반복해서
            ans += gcd(N[a], N[b])          # 두 수의 gcd를 구해 ans에 더한다
    print(ans)                              # gcd의 합을 출력한다