# 벌집_BOJ2292

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                # 벌집의 숫자를 입력받고
n = 0                           # 한칸 당 6의 배수씩 증가하므로

while 1:                        # break가 나올때까지 반복해서
    tmp = 1                     # n+1칸 이동 시 갈 수 있는 방의 번호를 tmp로 만들어준 후
    for a in range(1, n+1):     # n칸 이동을 반복했을 때
        tmp += 6*a              # tmp에 이동할 수 있는 방번호의 최대값까지 더한다
    else:                       # 최대값까지 계산했을때
        if N <= tmp:            # N이 최대값보다 같거나 작으면
           break                # 반복문을 종료하고
        else:                   # 그렇지 않다면
            n += 1              # n을 1 추가하여 다음칸 방번호를 반복하여 알아본다

print(n+1)