# AC_BOJ5430

# input.txt 열기
import sys
sys.stdin = open('input.txt')
import re
from collections import deque

# input 받기
T = int(sys.stdin.readline())                       # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복해서
    P = sys.stdin.readline().rstrip()               # 뒤집기와 popleft를 할 함수를 input 받음
    N = int(sys.stdin.readline())                   # 리스트 내 요소의 개수를 input 받음
    Q = re.findall(r'\d+', sys.stdin.readline())    # Q에 숫자만 str 타입으로 input 받고
    Q = deque(Q)                                    # Q를 deque로 만들어준다

    flag = True                                     # 뒤집기를 표시할 flag를 생성하고
    for p in P:                                     # 뒤집기와 popleft를 할 함수를 반복해서
        if p == 'R':                                # 뒤집기가 나오면
            if flag == True:                        # 뒤집혀있지 않았을 때(T)
                flag = False                        # flag를 False로 만들어 뒤집힌 표시를 해준다
            elif flag == False:                     # 뒤집혀있을 때(F)
                flag = True                         # flag를 True로 만들어 뒤집히지 않은 표시를 해준다
        elif p == 'D':                              # popleft가 나오면
            if len(Q) == 0:                         # Q가 빈 배열일 땐
                print('error')                      # error를 출력하고 반복문을 종료
                break
            else:                                   # Q가 빈배열이 아니라면
                if flag == True:                    # 뒤집히지 않은 배열일 땐
                    Q.popleft()                     # popleft로 제거하고
                elif flag == False:                 # 뒤집힌 배열일 땐
                    Q.pop()                         # pop으로 제거한다
    else:                                           # 뒤집기와 popleft를 할 함수의 반복을 모두 마쳤다면
        if flag == False:                           # flag가 False로 뒤집혀져 있는 상황이면
            Q.reverse()                             # Q를 뒤집어준 후
        if len(Q) == 0:                             # 빈 배열일 땐
            print([])                               # []를 출력하고
        else:                                       # 비어있지 않은 배열일 땐
            ans = '['                               # [ 가 들어있는 ans에
            for q in range(len(Q)):                 # Q의 요소를 반복해서
                if q != len(Q)-1:                   # 마지막 요소가 아닐 땐
                    ans += Q[q]                     # 요소를 더하고
                    ans += ','                      # ,를 더한다
                elif q == len(Q) - 1:               # 마지막 요소일 땐
                    ans += Q[q]                     # 요소를 더하고
                    ans += ']'                      # ]를 더한다
            print(ans)                              # 완성된 ans를 출력한다