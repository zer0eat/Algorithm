# 양념 반 후라이드 반_BOJ16917

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B, C, X, Y = map(int, input().split())   # 치킨의 가격과 사야하는 치킨의 수를 input 받고
if A+B < C*2:                               # 반반치킨이 더 비싸다면
    print(X*A+B*Y)                          # 각각 사는 비용을 출력하고
else:                                       # 반반치킨이 더 싸다면
    if X < Y:                               # 후라이드 치킨이 더 적은 경우
        if B > 2*C:                         # 양념치킨보다 반반 치킨 두마리가 더 싸면
            print(C*Y*2)                    # 반반치킨으로 사는 방법을 출력하고
        else:                               # 양념치킨보다 반반치킨 두마리가 더 비싸면
            print(X*C*2+(Y-X)*B)            # 반반치킨과 양념치킨으로 사는 방법을 출력한다
    else:                                   # 양념 치킨이 더 적은 경우
        if A > 2*C:                         # 후라이드치킨보다 반반 치킨 두마리가 더 싸면
            print(C*X*2)                    # 반반치킨으로 사는 방법을 출력하고
        else:                               # 후라이드치킨보다 반반치킨 두마리가 더 비싸면
            print(Y*C*2+(X-Y)*A)            # 반반치킨과 양념치킨으로 사는 방법을 출력한다