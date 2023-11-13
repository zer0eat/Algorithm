# 골드바흐 파티션_BOJ17103

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
prime = [0]*1000001                         # 소수를 저장할 리스트를 생성하고
for i in range(2, 1000001):                 # 2부터 1000000까지 반복해서
    if prime[i] == 0:                       # i가 표시가 없다면
        prime[i] = 1                        # 소수표시를 하고
        for j in range(i+i, 1000001, i):    # i보다 큰 i의 배수를 반복해서
            prime[j] = 2                    # 소수가 아닌 표시를 한다
T = int(input())                            # 테스트 케이스를 input 받고
for t in range(T):                          # 테스트케이스를 반복해서
    N = int(input())                        # 골드바흐 파티션의 수를 구할 정수를 input 받고
    ans = 0                                 # 골드바흐 파티션의 수를 저장할 변수를 생성한 뒤
    for i in range(2, N//2+1):              # 두 수의 합이 N이 될 수 중 작은 수를 반복해서
        if prime[i] == 1:                   # i가 소수라면
            if prime[N-i] == 1:             # N-i가 소수일 때
                ans += 1                    # 골드바흐 파티션이 되므로 1 추가한다
    else:                                   # 모든 숫자를 탐색했다면
        print(ans)                          # 골드바흐 파티션의 수를 출력한다