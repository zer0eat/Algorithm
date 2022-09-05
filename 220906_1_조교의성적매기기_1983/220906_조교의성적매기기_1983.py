# 조교의성적매기기_1983

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                                                                        # 테스트 케이스
for t in range(T):                                                                                      # 테스트 케이스를 반복할 때
    N, K = map(int, input().split())                                                                    # N = 학생수 / K = 성적 확인을 하는 학생의 번호
    achievement = [list(map(int,input().split())) for _ in range(N)]                                    # 중간/기말/수행 평가를 리스트로 저장

    ABC = []                                                                                            # 환산 점수를 저장할 빈 리스트
    for a in range(len(achievement)):                                                                   # 성적 리스트를 반복할 때
        ABC.append([a, achievement[a][0]*0.35 + achievement[a][1]*0.45 + achievement[a][2]*0.2])        # 중간 35% / 기말 45% / 수행 20% 로 환산하여 ABC에 append

    for i in range(N-1):                                                                                # 내림차순으로 버블정렬
        for j in range(N-i-1):
            if ABC[j][1] < ABC[j+1][1]:
                ABC[j], ABC[j + 1] = ABC[j+1], ABC[j]

    n = N//10                                                                                           # n = 등급당 배정할 수 있는 인원 수
    m = n                                                                                               # m = 배정인원을 계산하기 위한 변수
    l = 0                                                                                               # l = 등급의 인덱스로 사용하기 위한 변수
    q = 0                                                                                               # q = ABC의 인덱스로 사용하기 위한 변수
    level = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']                                # 10가지 종류의 등급을 리스트로 저장

    while l < 10:                                                                                       # 모든 등급을 배정할 때까지 반복
        if m == 0:                                                                                      # 한 등급의 배정이 완료되면
            l += 1                                                                                      # 다음 등급으로 바꾸고
            m = n                                                                                       # 배정인원을 초기화 한다
        elif m != 0:                                                                                    # 배정인원이 남았다면
            ABC[q].append(level[l])                                                                     # 현재 순서에 등급을 부여하고
            q += 1                                                                                      # ABC의 다음 인덱스로 넘어가고
            m -= 1                                                                                      # 현재 등급의 배정인원을 1명 감소시킨다

    for abc in ABC:                                                                                     # 배정완료된 등급을 탐색할 때
        if abc[0] == K - 1:                                                                             # 찾고자하는 번호를 가진 학생의
            print(f'#{t + 1}', abc[2])                                                                  # 등급을 출력한다
            break




