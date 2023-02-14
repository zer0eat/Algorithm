# 숫자빈도수_BOJ14912

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
n, d = map(int, sys.stdin.readline().split())   # n 1부터 차례대로 반복한 수 중 끝 수 / d 빈도수를 찾기 위한 특정수

ans = 0                                         # 빈도수를 저장할 변수를 생성하고
for i in range(1, n+1):                         # 1부터 n까지 반복해서
    for a in str(i):                            # n을 구성하는 숫자를 반복해서
        if a == str(d):                         # n을 구성하는 숫자가 d와 같다면
            ans += 1                            # ans에 1을 추가한다
else:                                           # 모든 반복을 마쳤다면
    print(ans)                                  # 빈도수를 출력한다