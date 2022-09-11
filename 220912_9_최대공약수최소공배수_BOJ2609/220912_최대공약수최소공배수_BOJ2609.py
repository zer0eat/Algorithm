# 최대공약수최소공배수_BOJ2609

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
A, B = map(int, input().split())            # 두 숫자를 A,B에 input 받음

n = 2                                       # 두 숫자를 나눠줄 변수를 2로 만든 후
ans = []                                    # 공약수를 저장할 빈 리스트를 만듦
while 1:                                    # break가 나올때까지 반복할 때
    if A >= n and B >= n:                   # 두 숫자 모두 n보다 크면 
        if A % n == 0 and B % n == 0:       # n이 둘 다 나눠지는지 확인 후
            A = A // n                      # n으로 나눠주고
            B = B // n
            ans.append(n)                   # n을 ans에 append
        else:                               # 나눠지지 않으면
            n += 1                          # 다음 숫자로 나누기 위해 n에 1을 더함
    else:                                   # 두 숫자중 하나라도 n보다 작으면
        break                               # break

mini = 1                                    # 최대공약수를 계산하기 위한 변수
for a in ans:                               # 공약수를 반복하여
    mini *= a                               # 그 수를 곱해준 후

print(mini)                                 # 공약수와
print(mini*A*B)                             # 공배수를 출력한다