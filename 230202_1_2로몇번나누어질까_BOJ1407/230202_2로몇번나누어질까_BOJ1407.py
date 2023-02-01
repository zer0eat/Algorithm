# 2로몇번나누어질까_BOJ1407

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
A, B = map(int, sys.stdin.readline().split())   # A 시작점 / B 끝점

ans = 0                                         # 정답을 저장하기 위한 변수 생성
tmp = 1                                         # 남은 수를 2로 나눈 값을 저장하고 있다가 나중에 연산하기 위한 변수 생성
while B > 0:                                    # B가 0보다 작아질때까지 반복해서
    if B % 2:                                   # B가 홀수라면
        ans += ((B//2) + 1)*tmp                 # 1부터 B까지 홀수의 수 X tmp를 ans에 더해준다
    else:                                       # B가 짝수라면
        ans += (B//2)*tmp                       # 1부터 B까지 홀수의 수 X tmp를 ans에 더해준다
    B //= 2                                     # B에서 홀수를 모두 뺐으므로 2로 나눠주고
    tmp *= 2                                    # 남은 수를 2로 나누면 처음 식이 반복되므로 tmp에 2를 곱해주어 다음 1의 개수에 곱해준다

A -= 1                                          # 1부터 B까지의 합에서 1부터 A-1의 합을 빼서 정답을 구하기 위해 A에서 1을 빼준다

tmp = 1                                         # 남은 수를 2로 나눈 값을 저장하고 있다가 나중에 연산하기 위한 변수 생성
while A > 0:                                    # A가 0보다 작아질때까지 반복해서
    if A % 2:                                   # A가 홀수라면
        ans -= ((A//2) + 1)*tmp                 # 1부터 A까지 홀수의 수 X tmp를 ans에 더해준다
    else:                                       # A가 짝수라면
        ans -= (A//2)*tmp                       # 1부터 A까지 홀수의 수 X tmp를 ans에 더해준다
    A //= 2                                     # A에서 홀수를 모두 뺐으므로 2로 나눠주고
    tmp *= 2                                    # 남은 수를 2로 나누면 처음 식이 반복되므로 tmp에 2를 곱해주어 다음 1의 개수에 곱해준다

print(ans)                                      # 정답을 출력한다