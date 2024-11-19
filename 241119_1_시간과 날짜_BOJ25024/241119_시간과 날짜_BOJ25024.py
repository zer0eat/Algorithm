# 시간과 날짜_BOJ25024

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                # 테스트 케이스를 input 받고
for t in range(T):                              # 테스트 케이스를 반복해서
    x, y = map(int, input().split())            # x,y를 input 받고
    ans = []                                    # 정답을 저장할 리스트를 생성하고
    if x <= 23 and y <= 59:                     # 시간으로 읽을 수 있다면
        ans.append('Yes')                       # Yes를 append한다
    else:                                       # 시간으로 읽을 수 없다면
        ans.append('No')                        # No를 append한다
    if x in [1,3,5,7,8,10,12] and 1 <= y and y <= 31:   # 31일이 있는 달로 읽을 수 있다면
        ans.append('Yes')                       # Yes를 append한다
    elif x in [4,6,9,11] and 1 <= y and y <= 30:        # 30일이 있는 달로 읽을 수 있다면
        ans.append('Yes')                       # Yes를 append한다
    elif x == 2 and 1 <= y and y <= 29:                 # 29일이 있는 달로 읽을 수 있다면
        ans.append('Yes')                       # Yes를 append한다
    else:                                       # 달로 읽을 수 없다면
        ans.append('No')                        # No를 append한다
    print(*ans)                                 # 정답을 출력한다