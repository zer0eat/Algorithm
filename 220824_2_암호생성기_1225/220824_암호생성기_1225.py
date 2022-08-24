# 암호생성기_1225

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 10                                              # 테스트 케이스
for t in range(T):                                  # 테스트 케이스만큼 반복
    case = int(input())                             # 테이스 케이스 번호
    code = list(map(int, input().split()))          # 암호문을 리스트로 받음

    secret = False                                  # 암호문이 풀리지 않았을 때 변수 지정

    while secret == False:                          # 암호문이 풀릴 때까지 반복
        for N in range(1, 6):                       # N이 1부터 5까지 반복할 때
            cycle = code.pop(0)                     # cycle에 code 리스트의 맨 앞의 수를 빼서 저장한다.
            if cycle - N > 0:                       # cycle - N이 양수면
                code.append(cycle - N)              # code 리스트의 맨 뒤에 append
            elif cycle - N <= 0:                    # cycle - N이 0보다 작거나 음수면
                secret = True                       # 암호문 해독완료로 표시로 바꾸고
                code.append(0)                      # code 리스트의 마지막에 0을 append 한다
                break                               # 반복문을 종료한 후

    print(f'#{case}', *code)                        # 해독된 암호를 출력한다