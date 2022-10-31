# 베르트랑공준_BOJ4948

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
while 1:                                        # break가 나올때까지 반복해서
    N = int(input())                            # N 초과 2N이하의 소수를 구하기 위해 N을 input 받는다
    if N == 0:                                  # N이 0일때 while을 break
        break
    else:                                       # N이 0이 아니라면
        ans = [0]*(2*N+1)                       # 인덱스가 2*N까지인 리스트를 생성하고
        for q in range(2, 2*N + 1):             # 2부터 2*N까지 반복할 때
            if ans[q] == 0:                     # ans[q]가 0으로 소수나 소수가 아니라는 표시가 되어있지 않다면
                ans[q] = 1                      # q는 소수이기 때문에 ans[q]를 1로 표시한다
                for p in range(q, 2*N + 1, q):  # q부터 찾고자 하는 수까지 q의 배수로 반복해서
                    if p == q:                  # q는 pass하고
                        pass
                    else:                       # 그 배수는
                        ans[p] = 2              # 소수가 아니므로 ans[q]는 2라고 표시한다

    cnt = 0                                     # 범위내 소수의 개수를 구하기 위해 변수를 생성하고
    for a in range(len(ans)):                   # ans를 반복해서
        if N < a and a <= 2*N:                  # 범위 내의 숫자인 경우
            if ans[a] == 1:                     # 소수라고 표시되어 있다면
                cnt += 1                        # 1을 추가하고
    print(cnt)                                  # 출력해준다

