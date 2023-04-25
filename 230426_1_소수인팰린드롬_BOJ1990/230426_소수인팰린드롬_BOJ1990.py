# 소수인팰린드롬_BOJ1990

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
a, b = map(int, input().split())                # a 시작점 / b 끝점을 input 받고
if b > 10000000:                                # 끝점이 10000000 보다 크다면
    b = 10000000                                # 10000000 이후에는 소수인 펠린드롬이 없으므로 b를 10000000로 바꾼다
ans = []                                        # 정답을 저장할 리스트를 생성하고
for i in range(a, b+1):                         # 시작부터 끝까지 반복해서
    A = str(i)                                  # A를 string으로 변경 후
    if A == A[::-1]:                            # 펠린드롬이라면
        for j in range(2, int(i**0.5) + 1):     # 2부터 제곱근까지 반복해서
            if i % j == 0:                      # 해당 숫자로 나누어 떨어지면 소수가 아니므로
                break                           # for문을 break
        else:                                   # 모두 나누어떨어지지 않았다면
            ans.append(i)                       # 소수이므로 ans에 append

for n in ans:                                   # ans를 반복해서
    print(n)                                    # 원소를 하나씩 출력한 후
else:                                           # 반복을 마치면
    print(-1)                                   # -1을 출력한다