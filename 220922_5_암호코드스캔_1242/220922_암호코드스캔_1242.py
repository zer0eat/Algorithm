# 암호코드스캔_1242

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
T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    final_ans = []

    # 윗줄과 다른 줄만 모으기
    arr = []
    for a in range(N):
        A = input()
        if arr == []:
            arr.append(A)
        elif arr[-1] == A:
            pass
        elif arr[-1] != A:
            arr.append(A)

    # 코드만 잘라내기
    code_tmp = []
    code = []
    n = 1
    while n < len(arr):
        tmp = ''
        for a in range(M-1, -1, -1):
            if tmp == '' and arr[n-1][a] != arr[n][a]:
                tmp = arr[n][a] + tmp
            elif tmp != '' and arr[n-1][a] != arr[n][a]:
                tmp = arr[n][a] + tmp
            elif tmp != '' and arr[n-1][a] == arr[n][a]:

                if N >= 0:
                    if a-1 >= 0 and arr[n-1][a-1] != arr[n][a-1]:
                        tmp = arr[n][a] + tmp
                    elif 0<=a-3<M:
                        if arr[n][a-5:a+1] == '81C000':
                            code_tmp.append(tmp)
                            tmp = ''
                        if arr[n][a-3:a+1] == '0000':
                            code_tmp.append(tmp)
                            tmp = ''

                        elif arr[n-1][a-1] != arr[n][a-1] or arr[n-1][a-2] != arr[n][a-2] or arr[n-1][a-3] != arr[n][a-3] :
                            tmp = arr[n][a] + tmp
                        else:
                            pass
        else:
            code_tmp.append(tmp)
            n += 1
    else:
        for n in code_tmp:
            B = n.lstrip('0').rstrip('0')
            if B != '':
                B = '0000' + B
                code.append(B)

    # 16진수 암호 2진수로 바꾸기
    code2 = []
    for c in code:
        B_num = ''  # 16진수 숫자를 2진수로 바꿔 저장할 변수
        for a in c:  # 16진수의 숫자를 반복할 때
            try:  # 숫자가 나와서 int로 변환이 가능하면
                a = int(a)  # a를 int로 변환하고
                bb = binary(a)  # 2진수로 바꿔주는 함수를 돌려 bb에 저장한 후에
                B_num += bb  # B_num에 추가한다
            except:  # 문자가 나와서 int로 변환이 불가능하면
                if a == 'A':  # a가 'A'일 때
                    a = 10  # a = 10이다
                    bb = binary(a)  # 2진수로 바꿔주는 함수를 돌려 bb에 저장한 후에
                    B_num += bb  # B_num에 추가한다
                elif a == 'B':  # a가 'B'일 때
                    a = 11  # a = 11이다
                    bb = binary(a)
                    B_num += bb
                elif a == 'C':  # a가 'C'일 때
                    a = 12  # a = 12이다
                    bb = binary(a)
                    B_num += bb
                elif a == 'D':  # a가 'D'일 때
                    a = 13  # a = 13이다
                    bb = binary(a)
                    B_num += bb
                elif a == 'E':  # a가 'E'일 때
                    a = 14  # a = 14이다
                    bb = binary(a)
                    B_num += bb
                elif a == 'F':  # a가 'F'일 때
                    a = 15  # a = 15이다
                    bb = binary(a)
                    B_num += bb
        else:  # 2진수로 변환이 끝났으면 결과를 출력한다
            code2.append(B_num)
    # 코드 자르기
    code3 = []
    for c3 in range(len(code2)):
        qqq = c3
        c3 = code2[c3].rstrip('0')
        aaa = c3[:]
        while 1:
            if len(c3) % 56 != 0:
                c3 = c3[1:]
            elif len(c3) % 56 == 0:
                break
        code4 = []
        ccc = len(c3) // 8
        for a in range(8):
            barcode = []
            tmp0 = 0
            tmp1 = 0
            for b in range(ccc):
                if c3[ccc * a + b] == '0':
                    if tmp1 != 0:
                        barcode.append(tmp1)
                        tmp1 = 0
                        tmp0 += 1
                    else:
                        tmp0 += 1
                if c3[ccc * a + b] == '1':
                    if tmp0 != 0:
                        barcode.append(tmp0)
                        tmp0 = 0
                        tmp1 += 1
                    else:
                        tmp1 += 1
            else:
                if tmp0 != 0:
                    barcode.append(tmp0)
                elif tmp1 != 0:
                    barcode.append(tmp1)
                code4.append(barcode)
        else:
            # 공배수로 나누기
            nn = len(c3)//56
            if nn == 1:
                pass
            elif nn > 1:
                # print(nn)
                for c4 in range(len(code4)):
                    for c44 in range(4):
                        code4[c4][c44] = int(code4[c4][c44])//nn

            spy = []
            # 해독하기
            for ccc in code4:
                if ccc == [3, 2, 1, 1]:  # 0을 암호화 한다면 spy에 0을 append
                    spy.append(0)
                elif ccc == [2, 2, 2, 1]:  # 1을 암호화 한다면 spy에 1을 append
                    spy.append(1)
                elif ccc == [2, 1, 2, 2]:  # 2을 암호화 한다면 spy에 2를 append
                    spy.append(2)
                elif ccc == [1, 4, 1, 1]:  # 3을 암호화 한다면 spy에 3을 append
                    spy.append(3)
                elif ccc == [1, 1, 3, 2]:  # 4을 암호화 한다면 spy에 4를 append
                    spy.append(4)
                elif ccc == [1, 2, 3, 1]:  # 5을 암호화 한다면 spy에 5를 append
                    spy.append(5)
                elif ccc == [1, 1, 1, 4]:  # 6을 암호화 한다면 spy에 6을 append
                    spy.append(6)
                elif ccc == [1, 3, 1, 2]:  # 7을 암호화 한다면 spy에 7을 append
                    spy.append(7)
                elif ccc == [1, 2, 1, 3]:  # 8을 암호화 한다면 spy에 8을 append
                    spy.append(8)
                elif ccc == [3, 1, 1, 2]:  # 9을 암호화 한다면 spy에 9를 append
                    spy.append(9)

            # 유효숫자 검사
            confirm = 0
            for pp in range(len(spy)):
                if pp % 2 == 0:
                    confirm += spy[pp] * 3
                else:
                    confirm += spy[pp]

            else:
                if confirm % 10 == 0:
                    final_ans.append(sum(spy))
                else:
                    pass
    else:
        print(f'#{t + 1}', sum(final_ans))