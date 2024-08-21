# 두 개의 손_BOJ16675

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
m1, m2, t1, t2 = input().split()        # 민성이와 태경이의 가위바위보를 input 받고
if m1 == m2:                            # 민성이가 같은 것을 냈을 때
    if m1 == 'R' and 'P' in [t1, t2]:   # 민성이가 바위 일때 태경이가 보를 냈다면
        print('TK')                     # 태경이의 승리를 출력하고
        quit()                          # 종료한다
    elif m1 == 'S' and 'R' in [t1, t2]: # 민성이가 가위 일때 태경이가 바위를 냈다면
        print('TK')                     # 태경이의 승리를 출력하고
        quit()                          # 종료한다
    elif m1 == 'P' and 'S' in [t1, t2]: # 민성이가 보 일때 태경이가 가위를 냈다면
        print('TK')                     # 태경이의 승리를 출력하고
        quit()                          # 종료한다
if t1 == t2:                            # 태경이가 같은 것을 냈을 때
    if t1 == 'R' and 'P' in [m1, m2]:   # 태경이가 바위 일때 민성이가 보를 냈다면
        print('MS')                     # 민성이의 승리를 출력하고
        quit()                          # 종료한다
    elif t1 == 'S' and 'R' in [m1, m2]: # 태경이가 가위 일때 민성이가 바위를 냈다면
        print('MS')                     # 민성이의 승리를 출력하고
        quit()                          # 종료한다
    elif t1 == 'P' and 'S' in [m1, m2]: # 태경이가 보 일때 민성이가 가위를 냈다면
        print('MS')                     # 민성이의 승리를 출력하고
        quit()                          # 종료한다
print('?')                              # 승부를 알 수 없으므로 ?를 출력한다