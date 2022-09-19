# 이진수_14141

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 16진수의 숫자를 2진수로 만들기
def binary(a):                          # 이진수로 만드는 함수를 정의하고
    ans = ''                            # 이진수를 저장할 변수 ans를 만든 후
    for i in range(4):                  # 16진수는 4자리의 2진수로 표현되므로 4번 반복해서
        ans = str(a % 2) + ans          # ans에 2로 나눈 나머지를 맨 앞에 추가하고
        a = a // 2                      # a를 2로 나눈 몫으로 바꾼다
    else:                               # 반복이 완료되면
        return ans                      # ans를 return 한다

# input 받기
T = int(input())                        # 테스트케이스
for t in range(T):                      # 테스트 케이스를 반복할 때
    N, arr = input().split()            # N = 16진수의 자리 / arr = 16 진수로 표현된 숫자

    B_num = ''                          # 16진수 숫자를 2진수로 바꿔 저장할 변수
    for a in arr:                       # 16진수의 숫자를 반복할 때
        try:                            # 숫자가 나와서 int로 변환이 가능하면
            a = int(a)                  # a를 int로 변환하고
            bb = binary(a)              # 2진수로 바꿔주는 함수를 돌려 bb에 저장한 후에
            B_num += bb                 # B_num에 추가한다
        except:                         # 문자가 나와서 int로 변환이 불가능하면
            if a == 'A':                # a가 'A'일 때
                a = 10                  # a = 10이다
                bb = binary(a)          # 2진수로 바꿔주는 함수를 돌려 bb에 저장한 후에
                B_num += bb             # B_num에 추가한다
            elif a == 'B':              # a가 'B'일 때
                a = 11                  # a = 11이다
                bb = binary(a)
                B_num += bb
            elif a == 'C':              # a가 'C'일 때
                a = 12                  # a = 12이다
                bb = binary(a)
                B_num += bb
            elif a == 'D':              # a가 'D'일 때
                a = 13                  # a = 13이다
                bb = binary(a)
                B_num += bb
            elif a == 'E':              # a가 'E'일 때
                a = 14                  # a = 14이다
                bb = binary(a)
                B_num += bb
            elif a == 'F':              # a가 'F'일 때
                a = 15                  # a = 15이다
                bb = binary(a)
                B_num += bb
    else:                               # 2진수로 변환이 끝났으면 결과를 출력한다
        print(f'#{t + 1}', B_num)