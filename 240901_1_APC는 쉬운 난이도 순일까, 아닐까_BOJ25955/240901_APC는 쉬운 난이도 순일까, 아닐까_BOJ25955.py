# APC는 쉬운 난이도 순일까, 아닐까_BOJ25955

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 문제의 수를 input 받고
level = list(input().split())                       # 문제의 레벨을 리스트로 input 받는다
tier = {'B':0, 'S':1, 'G':2, 'P':3, 'D':4}          # 문제 난이도를 딕셔너리로 생성하고
ans = []                                            # 난이도가 잘못 설정된 문제를 저장할 리스트를 생성한다
for n in range(N-1):                                # N-1개의 문제를 반복해서
    if tier[level[n][0]] > tier[level[n+1][0]]:     # 문제의 티어가 뒤집혔다면
        if ans:                                     # 잘못된 문제가 있다면
            ans.pop()                               # 마지막 문제를 pop하고
            ans.append(level[n+1])                  # 잘못된 문제를 넣는다
        else:                                       # 잘못된 문제가 없다면
            ans.append(level[n])                    # 앞 문제를 넣고
            ans.append(level[n+1])                  # 뒷 문제를 넣는다
    elif tier[level[n][0]] == tier[level[n+1][0]]:  # 문제의 티어가 같을 때
        if int(level[n][1:]) < int(level[n+1][1:]): # 문제의 등급이 뒤집혔다면
            if ans:                                 # 잘못된 문제가 있다면
                ans.pop()                           # 마지막 문제를 pop하고
                ans.append(level[n+1])              # 잘못된 문제를 넣는다
            else:                                   # 잘못된 문제가 없다면
                ans.append(level[n])                # 앞 문제를 넣고
                ans.append(level[n+1])              # 뒷 문제를 넣는다
if ans:                                             # 잘못된 문제가 있다면
    print('KO')                                     # KO를 출력하고
    print(*reversed(ans))                           # 잘못된 문제를 정렬한다
else:                                               # 잘못된 문제가 없다면
    print('OK')                                     # OK를 출력한다