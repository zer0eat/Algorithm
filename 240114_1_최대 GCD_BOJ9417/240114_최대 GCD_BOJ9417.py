# 최대 GCD_BOJ9417

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                        # 테스트 케이스를 input 받고

def euclidean(a, b):
    while b > 0:                                        # b가 0이 될때까지 반복해서
        a, b = b, a%b                                   # a를 b로 b를 a를 b로 나눈 나머지로 저장한다
    return a                                            # b가 0이 되면 최대 공약수 a를 return한다

for n in range(N):                                      # 테스트 케이스를 반복해서
    ans = 0                                             # 정답을 저장할 변수를 생성하고
    lst = list(map(int, input().split()))               # 정수 리스트를 input 받는다
    for i in range(len(lst)):                           # 모든 정수를 반복하고
        for j in range(i+1, len(lst)):                  # i+1번째 부터 끝까지 반복해서
            ans = max(ans, euclidean(lst[i], lst[j]))   # i번째와 j번째의 최대 공약수를 현재 저장된 ans와 비교해서 더 큰 값을 저장한다
    print(ans)                                          # 모든 두 수의 쌍의 최대공약수 중 가장 큰 값을 출력한다