# 화물도크_14176

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                # 테스트케이스
for t in range(T):                              # 테스트케이스를 반복할 때
    N = int(input())                            # 화물차가 작업의 숫자
    truck = []                                  # 작업시간을 저장할 빈 리스트
    for n in range(N):                          # 화물차가 들어올 때마다
        a, b = map(int, input().split())        # a 시작시간 / b 마감시간
        truck.append([b,a])                     # truck에 [마감시간, 시작시간]으로 append

    truck.sort()                                # 오름차순으로 정렬한 뒤

    ans = 1                                     # 작업할 트럭의 대수를 저장할 변수를 생성하고
    finish = truck[0][0]                        # 첫차의 마감시간을 finish에 저장한다

    for r in range(1, len(truck)):              # 두번째 차부터 스케줄을 확인할 때
        if truck[r][1] >= finish:               # 이전 차의 마감시간보다 시작 시간이 더 늦은 작업차가 들어오면
            finish = truck[r][0]                # 그 차를 배정하고 finish를 새로 들어온 차의 마감시간으로 바꿔줌
            ans += 1                            # 차의 대수를 추가한다

    print(f'#{t+1}', ans)



