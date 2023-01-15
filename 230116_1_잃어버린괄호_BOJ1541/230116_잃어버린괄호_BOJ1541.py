# 잃어버린괄호_BOJ1541

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
num = sys.stdin.readline().strip()  # 계산식을 input 받음

ans = 0                             # 계산한 값을 저장할 변수 생성
tmp = ''                            # 숫자를 저장할 변수 생성
flag = True                         # + -를 결정할 flag를 ture로 생성
for n in num:                       # 계산식을 반복해서
    if n == '-':                    # -가 나왔다면
        A = int(tmp)                # tmp를 int로 바꾸고
        tmp = ''                    # tmp를 비워준다
        if flag == True:            # flag가 True라면
            ans += A                # ans에 A를 더해준다
            flag = False            # flag를 False로 바꿔 이후에 나오는 모든 연산을 빼기로 해준다
        else:                       # flag가 False라면
            ans -= A                # ans에서 A를 빼준다
    elif n == '+':                  # +가 나왔다면
        A = int(tmp)                # tmp를 int로 바꾸고
        tmp = ''                    # tmp를 비워준다
        if flag == True:            # flag가 True라면
            ans += A                # ans에 A를 더해준다
        else:                       # flag가 False라면
            ans -= A                # ans에서 A를 빼준다
    else:                           # 숫자가 나왔다면
        tmp += n                    # tmp에 str형태로 뒤에 붙여준다
else:                               # 반복을 마쳤다면
    if flag == False:               # flag가 False라면
        ans -= int(tmp)             # ans에서 tmp를 빼주고
    else:                           # flag가 True라면
        ans += int(tmp)             # ans에서 tmp를 더해준다

print(ans)                          # 결과값을 출력한다