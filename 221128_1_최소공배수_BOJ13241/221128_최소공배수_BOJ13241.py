# 최소공배수_BOJ13241

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
lst = list(map(int, sys.stdin.readline().split()))      # 최소공배수를 구하고자 하는 두 숫자를 lst에 넣어 저장한다
lst.sort()                                              # lst를 오름차순으로 정렬하고
n = lst[0]                                              # 두 숫자 중 작은 숫자를 n에 저장한다

ans = []                                                # 공배수를 저장할 빈 리스트를 만들고
while n > 1:                                            # n이 1이 될때까지 반복해서
    if lst[0] % n == 0 and lst[1] % n == 0:             # 두 숫자가 모두 n으로 나누어 떨어질 때
        lst[0] = lst[0] // n                            # 두 숫자를 모두 n으로 나누고
        lst[1] = lst[1] // n
        ans.append(n)                                   # 공배수를 ans에 append 한 후
        n = lst[0]                                      # n으로 나눈 두 숫자 중 작은 수로 n을 업데이트 해준다
    else:                                               # 만약 나누어 떨어지지 않는 경우는
        n -= 1                                          # n에서 1을 빼준다
else:                                                   # n이 1에 도달했을 경우
    num = lst[0] * lst[1]                               # 최종적으로 남은 두 숫자를 곱하고
    for a in ans:                                       # 공배수의 리스트를 반복해서
        num *= a                                        # 공배수를 모두 곱해준 후
    else:                                               # 반복을 마쳤으면
        print(num)                                      # 최소 공배수를 출력한다