# 등차수열과 쿼리_BOJ23888

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, D = map(int, input().split())                # A 초항 / B 공차를 input 받고

def gcd(a, b):
    while b > 0:                                # b가 0이 될때까지 반복해서
        a, b = b, a % b                         # a에 b를 저장하고 b에 a를 b로 나눈 나머지를 저장한다
    return a                                    # b가 0일 때 최대공약수인 a를 return한다

Q = int(input())                                # 쿼리의 개수를 input 받고
for q in range(Q):                              # 쿼리의 개수를 반복해서
    ans = 0                                     # 정답을 저장할 변수를 생성하고
    query = list(map(int, input().split()))     # 쿼리를 리스트로 input 받는다
    if query[0] == 1:                           # 1번 임무가 주어졌다면
        ans += (query[2]-query[1]+1)*A          # 등차수열의 초항의 합을 더한 후
        ans += ((query[2])*(query[2]-1)- (query[1]-1)*(query[1]-2))*D//2    # 등차수열의 공차의 합을 더한 후
        print(ans)                              # 합을 출력한다
    else:                                       # 2번 임무가 주어졌다면
        if query[1] == query[2]:                # 최대공약수를 구하려는 원소가 한개라면
            print(A+D*(query[1]-1))             # 그대로 출력하고
        else:                                   # 최대공약수를 구하려는 원소가 여러개라면
            print(gcd(A, D))                    # 공차와 초항의 최대공약수를 출력한다