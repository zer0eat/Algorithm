# 괄호검사_13807

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):
    N = list(input())                           # 판독할 문장을 받음
    test = []                                   # 괄호를 담을 빈 리스트 생성
    for n in N:                                 # N 리스트를 반복할 때
        if n == '(':                            # '(' 나오면 1을 test에 append
            test.append(1)
        elif n == ')':                          # ')' 나오면 2을 test에 append
            test.append(2)
        elif n == '{':                          # '{' 나오면 3을 test에 append
            test.append(3)
        elif n == '}':                          # '}' 나오면 4을 test에 append
            test.append(4)
    G = len(test)                               # test의 길이를 G에 저장
    n = 0                                       # test를 반복할 때 인덱스
    k = 0                                       # test에서 지운 숫자의 수
    while n + k < G - 1:                        # test를 반복, 맨뒤에서 한칸 앞자리 까지
        if test[n] == 1 and test[n+1] == 2:     # n이 1일 때 뒤에 바로 2가 나오면
            del test[n+1]                       # n+1의 자리와
            del test[n]                         # n의 자리 모두 삭제
            k += 2                              # 지운숫자 추가
            n = 0                               # 인덱스 처음으로 초기화
        elif test[n] == 3 and test[n+1] == 4:   # n이 3일 때 뒤에 바로 4가 나오면
            del test[n + 1]                     # n+1의 자리와
            del test[n]                         # n의 자리 모두 삭제
            k += 2                              # 지운숫자 추가
            n = 0                               # 인덱스 처음으로 초기화
        else:
            n += 1                              # 위와 같은 조건이 없을 땐 인덱스를 다음으로 한칸 이동
    if len(test) == 0:                          # test가 비어서 짝이 맞다면 1을 출력
        print(f'#{t+1}', 1)
    elif len(test) != 0:                        # test가 남아서 짝이 맞지 않는다면 0을 출력
        print(f'#{t+1}', 0)