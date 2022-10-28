# 네번째점_BOJ3009

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
x = []                                                  # x 좌표를 담을 리스트
y = []                                                  # y 좌표를 담을 리스트
for _ in range(3):                                      # 3 꼭지점의 좌표를 반복해서
    a, b = map(int, sys.stdin.readline().split())       # x 좌표를 a에 y 좌표를 b에 인풋받고
    for q in range(len(x)):                             # x 리스트를 반복해서
        if a == x[q]:                                   # a가 x에 있으면
            x.pop(q)                                    # a와 같은 숫자를 리스트에서 pop하고 반복문을 종료한다
            break
    else:                                               # 같은 숫자가 나오지 않았다면
        x.append(a)                                     # a를 x에 append 한다
    for q in range(len(y)):                             # y 리스트를 반복해서
        if b == y[q]:                                   # b가 y에 있으면
            y.pop(q)                                    # b와 같은 숫자를 리스트에서 pop하고 반복문을 종료한다
            break
    else:                                               # 같은 숫자가 나오지 않았다면
        y.append(b)                                     # b를 y에 append 한다
print(*x,*y)                                            # x와 y를 출력한다