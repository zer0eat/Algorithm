# coins_BOJ3067

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                            # 테스트 케이스
for t in range(T):                          # 테스트 케이스를 반복해서
    N = int(input())                        # N 동전의 개수
    coin = list(map(int, input().split()))  # 동전의 종류를 리스트로 input 받는다
    M = int(input())                        # M 동전의 합으로 만들어야할 액수
    check = [0]*(M+1)                       # 0부터 M까지 인덱스를 갖는 리스트 생성 
    check[0] = 1                            # 동전의 합이 0이 되는 경우의 수는 1개이므로 표시를한다

    for c in coin:                          # coin의 종류를 반복해서
        for m in range(M+1):                # 동전의 합을 0부터 M까지 반복한다
            if m >= c:                      # 동전의 합이 c 코인 이상이 되면
                check[m] += check[m-c]      # 동전의 합 원소에 c동전을 더하기 전 경우의 수를 더해준다
    print(check[-1])                        # M원이 되는 경우의 수를 출력한다