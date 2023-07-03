# 벚꽃이 정보섬에 피어난 이유_BOJ17127

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 벚꽃나무 수
cherry_blossom = list(map(int, input().split()))    # 벚꽃나무에 핀 꽃의 수를 리스트로 input
ans = 0                                             # 가장 많은 수를 저장할 변수 생성
for i in range(4):                                  # 4구역으로 나누기 위해 4번 반복해서
    tmp = 0                                         # 4구역으로 나눴을 때 수를 저장하기 위한 변수 생성
    mul = 1                                         # 4구역중 그룹내 벚꽃의 수를 곱해서 저장할 변수 생성
    lst = [a for a in range(i, N-3+i)]              # 그룹화한 나무의 인덱스를 저장한 리스트 생성
    for n in range(N):                              # 벚꽃나무의 수를 반복해서
        if n in lst:                                # 해당 벚꽃나무가 lst에 포함되어 있다면
            mul *= cherry_blossom[n]                # 꽃의 수를 mul에 곱하고
        else:                                       # lst에 포함되어 있지 않다면
            tmp += cherry_blossom[n]                # tmp에 꽃의 수를 tmp에 더한다
    else:                                           # 모든 나무를 반복했다면
        tmp += mul                                  # tmp에 mul을 더해 전채 꽃의 수를 저장하고
        if tmp > ans:                               # tmp가 ans보다 큰 경우
            ans = tmp                               # ans를 tmp로 갱신한다
print(ans)                                          # 가장 많은 꽃의 수를 출력한다