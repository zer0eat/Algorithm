# Q-인덱스_BOJ13333

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 논문의 수
quote = list(map(int, input().split()))             # 인용된 횟수를 리스트로 input 받고
quote.sort()                                        # 오름차순으로 정렬한다

for k in range(N, -1, -1):                          # Q 인덱스를 N부터 내림차순으로 반복해서
    try:                                            # Q 인덱스가 N보다 작은 경우
        if quote[-k] >= k and quote[-k-1] <= k:     # k번째 적게 인용된 논문이 k개 이상이고 k+1번째 적게 인용된 논문이 k개 이하일 때
            print(k)                                # Q 인덱스는 k가 되므로 k를 출력하고
            break                                   # for문을 종료한다
    except:                                         # Q 인덱스가 N인 경우
        if quote[-k] >= k:                          # k번째 적게 인용된 논문이 k개 이상인 경우 / k+1번째 적게 인용된 논문은 없으므로 고려하지 않는다
            print(k)                                # Q 인덱스는 k가 되므로 k를 출력하고
            break                                   # for문을 종료한다