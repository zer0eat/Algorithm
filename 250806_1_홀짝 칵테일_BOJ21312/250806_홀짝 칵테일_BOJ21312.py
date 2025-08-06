# 홀짝 칵테일_BOJ21312

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B, C = map(int, input().split())         # 칵테일의 맛을 input받고
cocktail = [A, B, C, A*B, A*C, B*C, A*B*C]  # 칵테일의 맛 종류를 반복해서
cocktail.sort(reverse=True)                 # 칵테일의 맛을 내림차순 정렬한다
ans = cocktail[0]                           # 가장 큰맛을 변수에 저장하고
for c in cocktail:                          # 칵테일을 반복해서
    if ans % 2:                             # 현재 맛이 홀수라면
        break                               # for문을 종료한다
    else:                                   # 현재 맛이 짝수라면
        if c % 2:                           # 다음 맛이 홀수인경우
            ans = c                         # 다음맛으로 저장하고
            break                           # for문을 종료한다
print(ans)                                  # 정답을 출력한다