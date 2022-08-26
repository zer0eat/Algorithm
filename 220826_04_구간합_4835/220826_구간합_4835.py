# 구간합_4835

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스만큼 반복
    N, M = map(int, input().split())                # N = ai에 들어있는 정수의 개수 /  M = 이웃한 요소를 더할 개수
    ai = list(map(int, input().split()))            # N개의 정수를 ai에 리스트로 저장

    maxV = 0                                        # 최대값을 구해서 저장할 변수
    minV = 1000000                                  # 최소값을 구해서 저장할 변수
    for a in range(len(ai) - M + 1):                # ai에서 더할 숫자의 시작점만큼 반복할 때
        tmp = 0                                     # M개의 숫자를 더한 값을 저장할 변수
        for m in range(M):                          # M만큼 반복할 때
             tmp += ai[a + m]                       # a부터 M개의 요소를 tmp에 더해준다
        else:                                       # for문이 끝나면
            if tmp > maxV:                          # tmp가 maxV보다 클 때
                maxV = tmp                          # maxV를 tmp로 바꿔주고
            if tmp < minV:                          # tmp가 minV보다 작을 때
                minV = tmp                          # minV를 tmp로 바꿔준다

    print(f'#{t+1}', maxV - minV)                   # 최대값과 최소값의 차를 출력