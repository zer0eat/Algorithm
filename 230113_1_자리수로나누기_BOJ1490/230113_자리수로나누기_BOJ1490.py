# 자리수로나누기_BOJ1490

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = sys.stdin.readline().strip()        # 숫자를 input qkerh

tmp = set()                             # set을 생성한 후
for n in N:                             # input 받은 숫자의 각 자리 숫자를 반복해서
    if n != '0':                        # 각 자리의 숫자가 0이 아니라면
        tmp.add(int(n))                 # set에 int형식으로 더해준다

N = int(N)                              # input 받은 숫자를 int 형식으로 바꾸고
tmp = list(tmp)                         # set도 list로 바꿔준다

Q = 1                                   # Q를 1이라고 변수를 생성해준 후
while 1:                                # quit이 나올 때까지 반복해서
    for n in range(10**Q):              # 10**Q만큼 반복해서
        if n == 0:                      # n이 0 이라면
            for t in tmp:               # 각 자리 숫자를 저장해 놓은 list를 반복해서
                if N % t == 0:          # N을 각자리의 숫자로 나눴을 때 나눠떨어진다면
                    pass                # 패스하고
                else:                   # 나눠 떨어지지 않으면
                    break               # for문을 break한다
            else:                       # 각 자리 숫자를 저장해 놓은 list를 반복이 모두 끝났다면 각 자리 숫자로 모두 나누어지는 수이므로
                print(N)                # N을 출력하고
                quit()                  # 종료한다
            N *= 10                     # N이 나누어 떨어지지 않으므로 10을 곱해준 후
            for t in tmp:               # 각 자리 숫자를 저장해 놓은 list를 반복해서
                if N % t == 0:          # N을 각자리의 숫자로 나눴을 때 나눠떨어진다면
                    pass                # 패스하고
                else:                   # 나눠 떨어지지 않으면
                    break               # for문을 break한다
            else:                       # 각 자리 숫자를 저장해 놓은 list를 반복이 모두 끝났다면 각 자리
                print(N)                # N을 출력하고
                quit()                  # 종료한다
        else:                           # n이 0이 아니라면
            N += 1                      # N이 나누어 떨어지지 않으므로 1을 더해준 후
            for t in tmp:               # 각 자리 숫자를 저장해 놓은 list를 반복해서
                if N % t == 0:          # N을 각자리의 숫자로 나눴을 때 나눠떨어진다면
                    pass                # 패스하고
                else:                   # 나눠 떨어지지 않으면
                    break               # for문을 break한다
            else:                       # 각 자리 숫자를 저장해 놓은 list를 반복이 모두 끝났다면 각 자리
                print(N)                # N을 출력하고
                quit()                  # 종료한다
    else:                               # 10**Q만큼 반복해도 나눠 떨어지는 수를 찾지 못했다면
        N = N - (10**Q) + 1             # (10**Q-1)을 빼주어 초기로 돌린 후
        Q += 1                          # Q에 1을 더해서 한자리 더 커진 수를 탐색한다