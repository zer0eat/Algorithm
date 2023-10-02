# 3의배수_BOJ1769

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
X = input().strip()         # 자연수 X를 input 받고
ans = 0                     # 변환 횟수를 저장할 변수를 생성한다
while 1:                    # break가 나올때까지 반복해서
    if len(X) == 1:         # X가 1자리 수가 되었다면
        print(ans)          # 변환 횟수를 출력하고
        if int(X) % 3:      # 3으로 나누어 떨어지지 않는다면
            print('NO')     # NO를 출력하고
        else:               # 3으로 나누어 떨어진다면
            print('YES')    # YES를 출력한다
        break               # while문을 break한다
    tmp = 0                 # 변환 후 숫자를 저장할 변수를 생성하고
    for x in X:             # X를 반복하여
        tmp += int(x)       # 각자리의 숫자를 tmp에 더한다
    else:                   # X를 모두 반복했다면
        X = str(tmp)        # tmp를 string으로 변환하여 X에 저장한 후
        ans += 1            # 변환 횟수를 1 추가한다