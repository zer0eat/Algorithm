# 날카로운 눈_BOJ1637

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                            # 입력의 수를 input 받고
lst = [list(map(int, input().split())) for _ in range(N)]   # 정수더미를 나타낼 리스트를 input 받는다
l = 1                                                       # 가장 작은 수인 1을 나타낼 수를 저장하고
r = 2147483647                                              # 가장 큰 수인 2147483647을 나타낼 수를 저장한다
ans = -1                                                    # 정답을 저장할 변수를 생성하고
while l <= r:                                               # l이 r 이상이 될때까지 반복해서
    mid = (l+r)//2                                          # 두 수의 중점을 저장하고
    tmp = 0                                                 # mid까지 개수의 합을 저장할 변수를 생성한 후
    for n in lst:                                           # 정수더미 리스트를 반복해서
        A, C, B = n                                         # 정수더미를 A, C, B로 저장하고
        C = min(mid, C)                                     # C와 mid 중 더 큰수를 C에 저장한 후
        if A <= C:                                          # A가 C 이하라면
            tmp += (C-A)//B + 1                             # tmp에 C까지의 개수를 더해준다
    if tmp%2:                                               # tmp가 홀수개라면
        ans = mid                                           # ans에 mid를 저장하고
        r = mid-1                                           # 가장 큰 수를 줄여주고
    else:                                                   # tmp가 짝수개라면
        l = mid+1                                           # 가장 작은 수를 늘려준다
if ans == -1:                                               # 홀수개 존재하는 정수가 없으면
    print('NOTHING')                                        # NOTHING을 출력한다
else:                                                       # 홀수개 존재하는 정수가 있으면
    num1 = 0                                                # ans까지 개수를 저장할 변수를 생성하고
    num2 = 0                                                # ans-1까지 개수를 저장할 변수를 생성한 후
    for n in lst:                                           # 정수더미 리스트를 반복해서
        A, C, B = n                                         # 정수더미를 A, C, B로 저장하고
        C1 = min(ans, C)                                    # C와 ans 중 더 큰수를 C1에 저장한 후
        if A <= C1:                                         # A가 C1이하라면
            num1 += (C1-A)//B + 1                           # num1에 C1이하의 개수를 더해준다
        C2 = min(ans-1, C)                                  # C와 ans-1 중 더 큰수를 C2에 저장한 후
        if A <= C2:                                         # A가 C2이하라면
            num2 += (C2-A)//B + 1                           # num2에 C2이하의 개수를 더해준다
    print(ans, num1-num2)                                   # 홀수개 존재하는 정수를 출력하고, 몇 개 들어있는지 출력한다.