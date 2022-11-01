# 카잉달력_BOJ6064

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())                               # 테스트 케이스
for t in range(T):                                          # 테스트 케이스를 반복해서
    M, N, x, y = map(int, sys.stdin.readline().split())     # M 카잉달력의 앞 2자리 / N 카잉달력의 뒤 2자리 / x 찾고자하는 해의 카잉달력의 앞 / y 찾고자하는 해의 카잉달력의 뒤

    cnt = x                                                 # x:y가 몇번째 해 일지 비교할 변수에 x를 넣어 생성
    while cnt <= M*N:                                       # 종말의 해인 M*N까지 반복할 때
        if cnt == y or cnt % N == y:                        # 앞자리가 일치했을 때 뒷자리가 cnt이거나 cnt를 N으로 나눈 나머지일 때
            print(cnt)                                      # 찾고자하는 해를 찾았으므로 cnt를 출력하고
            break                                           # while 문을 break한다
        elif cnt % N == 0:                                  # cnt를 N으로 나눴을 때 0이라면 뒷자리가 N인 해를 나타내므로
            if N == y:                                      # 앞자리가 일치했을 때 뒷자리가 N인 경우
                print(cnt)                                  # 찾고자하는 해를 찾았으므로 cnt를 출력하고
                break                                       # while 문을 break한다
            else:                                           # 뒷자리가 일치하지 않는다면
                cnt += M                                    # cnt에 M을 더해 다음 앞자리가 일치하는 해로 넘어간다
        else:                                               # 뒷자리가 일치하지 않는다면
            cnt += M                                        # cnt에 M을 더해 다음 앞자리가 일치하는 해로 넘어간다
    else:                                                   # 반복문의 조건을 초과하여 종말의 해 이전에 찾고자 하는 해가 없다면
        print(-1)                                           # -1을 출력한다