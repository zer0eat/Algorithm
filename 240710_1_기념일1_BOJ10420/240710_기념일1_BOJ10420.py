# 기념일1_BOJ10420

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 기념하려는 날을 input 받고
ans = [2014, 4, 1]                  # 기념일을 계산할 기준일을 설정한다
for n in range(N):                  # 기념하려는 날을 반복해서
    ans[2] += 1                     # 기념하려는 날을 하나 세고
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]            # 월별 일수를 저장한 리스트를 생성하고
    if (ans[0] % 400 == 0) or (ans[0] % 100 != 0 and ans[0] % 4 == 0):  # 윤년이라면
        month[1] = 29               # 2월의 일수를 29로 저장한다
    if ans[2] > month[ans[1] - 1]:  # 매월 일수가 모두 지났다면
        ans[2] = 1                  # 다음달 1일로 돌아가고
        ans[1] += 1                 # 달을 하나 추가한다
    if ans[1] > 12:                 # 12월 달이 넘었다면
        ans[1] = 1                  # 1월로 돌아가고
        ans[0] += 1                 # 년을 하나 추가한다
for i in range(3):                  # 기념일을 반복해서
    tmp = ans[i]                    # i번째 원소를 tmp에 저장한 후
    if tmp < 10:                    # 한자리 정수라면
        tmp = '0' + str(tmp)        # 앞에 0을 붙여준다
    if i == 2:                      # 일을 출력한다면
        print(tmp)                  # 일만 출력하고
    else:                           # 년과 월을 출력한다면
        print(tmp, end='-')         # 출력후 -를 붙여준다