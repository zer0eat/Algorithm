# 민석이의 과제 체크하기_5431

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스만큼 반복
    N, K = map(int, input().split())                # N = 전체 학생의 수 / K = 제출한 학생의 수
    homework = list(map(int, input().split()))      # 제출한 학생의 번호를 homework에 리스트로 저장

    check = [0] * N                                 # 과제 체크를 위한 빈 리스트

    for h in homework:                              # 제출 과제를 보면서
        check[h - 1] += 1                           # 제출 했으면 1로 표시한다

    not_push = []                                   # 제출하지 않은 번호를 담을 빈 리스트 생성
    for c in range(len(check)):                     # check 리스트를 돌면서
        if check[c] == 0:                           # 과제를 안냈으면
            not_push.append(c + 1)                  # 번호를 not_push에 append

    print(f'#{t+1}', *not_push)