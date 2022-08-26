# min_max_4828

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):                              # 테스트 케이스의 수만큼 반복
    N = int(input())                            # ai 요소의 개수
    ai = list(map(int, input().split()))        # 숫자카드가 들어 있는 리스트

    # max 값 구하기
    maxV = 0                                    # 가장 큰 값을 저장할 변수
    for a in ai:                                # ai의 요소를 반복할 때
        if a > maxV:                            # a가 기존 최대값보다 크면
            maxV = a                            # maxV를 a로 바꿔준다
    # min 값 구하기
    minV = 1000001                              # 가장 작은 값을 저장할 변수
    for b in ai:                                # ai 요소를 반복할 때
        if minV > b :                           # b가 기존 최소값 보다 작으면
            minV = b                            # minV를 b로 바꿔준다

    print(f'#{t+1}', maxV - minV)               # 두 값의 차를 출력한다