# 220919_2_단순2진암호코드_1240

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복할 때
    N, M = map(int, input().split())                # N은 세로의 길이 / M은 가로의 길이
    code = [list(input()) for _ in range(N)]        # code에 영상물을 행렬로 저장

    # 영상물에서 코드 찾기
    f = True                                        # 코드를 찾았을 때 반복문을 종료할 변수 생성
    for i in range(N):                              # code의 행을 반복하고
        if f == False:                              # f가 False라면 반복문을 종료한다
            break
        for j in range(M-1, 0, -1):                 # code의 열을 맨뒤에서부터 앞으로 반복할 때
            if code[i][j] == '1':                   # 영상 안에서 1이 나온다면
                ans = code[i][j - 55: j + 1]        # 그 부분부터 앞으로 56칸을 슬라이싱해서 ans에 저장한다
                f = False                           # f를 False로 바꿔 반복문을 종료한다
                break

    spy = []                                        # 암호를 해독한 숫자를 저장할 리스트를 만들고
    for q in range(8):                              # 56개의 암호문을 8개로 나눠 반복하고
        tmp = ''                                    # 암호문을 7개로 잘라 저장할 변수를 생성하고
        for p in range(7):                          # q번째의 7개 암호문을 차례대로 tmp에 저장한다
            tmp += ans[7 * q + p]
        else:                                       # tmp에 암호를 잘라 넣었을 때
            if tmp == '0001101':                    # 0을 암호화 한다면 spy에 0을 append
                spy.append(0)
            elif tmp == '0011001':                  # 1을 암호화 한다면 spy에 1을 append
                spy.append(1)
            elif tmp == '0010011':                  # 2을 암호화 한다면 spy에 2를 append
                spy.append(2)
            elif tmp == '0111101':                  # 3을 암호화 한다면 spy에 3을 append
                spy.append(3)
            elif tmp == '0100011':                  # 4을 암호화 한다면 spy에 4를 append
                spy.append(4)
            elif tmp == '0110001':                  # 5을 암호화 한다면 spy에 5를 append
                spy.append(5)
            elif tmp == '0101111':                  # 6을 암호화 한다면 spy에 6을 append
                spy.append(6)
            elif tmp == '0111011':                  # 7을 암호화 한다면 spy에 7을 append
                spy.append(7)
            elif tmp == '0110111':                  # 8을 암호화 한다면 spy에 8을 append
                spy.append(8)
            elif tmp == '0001011':                  # 9을 암호화 한다면 spy에 9를 append
                spy.append(9)
    else:                                           # 암호해독이 끝났다면
        confirm = 0                                 # 유효한 암호문인지 확인하기 위한 변수 생성
        for y in range(len(spy)):                   # 해독된 spy를 반복할 때
            if y % 2 == 0:                          # 짝수번째 암호는
                confirm += spy[y] * 3               # 3배를 해서 더하고
            else:                                   # 홀수번째 암호는
                confirm += spy[y]                   # 그냥 더했을 때
        else:
            if confirm % 10 == 0:                   # 10의 배수라면 유효한 암호이므로
                print(f'#{t + 1}', sum(spy))        # 해독된 암호의 합을 출력
            else:                                   # 10의 배수가 아니라면 유효한 암호가 아니므로
                print(f'#{t + 1}', 0)               # 0을 출력