# 정식이의은행업무_4366

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 이진수 숫자를 한개만 바꿀 경우를 모두 구할 함수
def switch2(arr):
    a = 0                                           # 이진수 숫자의 인덱스로 사용할 변수
    ans = []                                        # 이진수 숫자를 한개만 바꾼 결과를 저장할 리스트
    while a < len(arr):                             # 바꿀 숫자를 처음부터 끝까지 반복할 때
        if arr[a] == '0':                           # 만약 바꿀 인덱스의 요소가 '0' 이라면
            arr[a] = '1'                            # '1'로 바꿔준 후
            n = 0                                   # 지수로 사용할 변수
            cal = 0                                 # 이진수를 십진수로 변환하여 저장할 변수
            for w in range(len(arr) - 1, -1, -1):   # 바꾼 이진수 숫자를 뒤에서부터 반복할 때
                cal += int(arr[w]) * (2 ** n)       # cal에 십진수로 변환해서 저장하고
                n += 1                              # 지수를 하나씩 증가시킨다
            else:                                   # 십진수로 변환을 완료 했다면
                ans.append(cal)                     # ans에 변환 값을 append
                arr[a] = '0'                        # 변환한 인덱스의 요소를 원래대로 돌려준다
                a += 1                              # 다음 인덱스 탐색으로 넘어가기 위해 a를 1 증가시킨다

        elif arr[a] == '1':                         # 만약 바꿀 인덱스의 요소가 '1' 이라면
            arr[a] = '0'                            # '0'으로 바꿔준 후
            n = 0                                   # 지수로 사용할 변수
            cal = 0                                 # 이진수를 십진수로 변환하여 저장할 변수
            for w in range(len(arr) - 1, -1, -1):   # 바꾼 이진수 숫자를 뒤에서부터 반복할 때
                cal += int(arr[w]) * (2 ** n)       # cal에 십진수로 변환해서 저장하고
                n += 1                              # 지수를 하나씩 증가시킨다
            else:                                   # 십진수로 변환을 완료 했다면
                ans.append(cal)                     # ans에 변환 값을 append
                arr[a] = '1'                        # 변환한 인덱스의 요소를 원래대로 돌려준다
                a += 1                              # 다음 인덱스 탐색으로 넘어가기 위해 a를 1 증가시킨다
    else:                                           # 바꾼 이진수를 모두 탐색했다면
        return ans                                  # ans를 리턴한다

# 삼진수 숫자를 한개만 바꿀 경우를 모두 구할 함수
def switch3(arr):
    a = 0                                           # 이진수와 같은 방식으로 모두 탐색한다
    ans = []
    while a < len(arr):
        if arr[a] == '0':
            arr[a] = '1'
            n = 0
            cal = 0
            for w in range(len(arr) - 1, -1, -1):
                cal += int(arr[w]) * (3 ** n)
                n += 1
            else:
                ans.append(cal)
                arr[a] = '0'
            arr[a] = '2'
            n = 0
            cal = 0
            for w in range(len(arr) - 1, -1, -1):
                cal += int(arr[w]) * (3 ** n)
                n += 1
            else:
                ans.append(cal)
                arr[a] = '0'
                a += 1

        elif arr[a] == '1':
            arr[a] = '0'
            n = 0
            cal = 0
            for w in range(len(arr) - 1, -1, -1):
                cal += int(arr[w]) * (3 ** n)
                n += 1
            else:
                ans.append(cal)
                arr[a] = '1'
            arr[a] = '2'
            n = 0
            cal = 0
            for w in range(len(arr) - 1, -1, -1):
                cal += int(arr[w]) * (3 ** n)
                n += 1
            else:
                ans.append(cal)
                arr[a] = '1'
                a += 1

        elif arr[a] == '2':
            arr[a] = '0'
            n = 0
            cal = 0
            for w in range(len(arr) - 1, -1, -1):
                cal += int(arr[w]) * (3 ** n)
                n += 1
            else:
                ans.append(cal)
                arr[a] = '2'
            arr[a] = '1'
            n = 0
            cal = 0
            for w in range(len(arr) - 1, -1, -1):
                cal += int(arr[w]) * (3 ** n)
                n += 1
            else:
                ans.append(cal)
                arr[a] = '2'
                a += 1
    else:
        return ans

# input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복할 때
    two = list(input())                             # two에 이진수를 리스트형태로 받고
    three = list(input())                           # three에 삼진수를 리스트형태로 받는다

    twoans = switch2(two)                           # 이진수를 한개씩 변환해서 나온결과를 확인하는 함수의 결과를 twoans에 저장하고
    threeans = switch3(three)                       # 삼진수를 한개씩 변환해서 나온결과를 확인하는 함수의 결과를 threeans에 저장하고

    find = 0                                        # 바꾼 결과를 저장할 변수
    for tans in twoans:                             # twoans를 반복해서
        if tans in threeans:                        # threeans에 같은 값이 나온다면
            find = tans                             # 같은값을 find에 저장하고 break
            break

    print(f'#{t+1}', find)