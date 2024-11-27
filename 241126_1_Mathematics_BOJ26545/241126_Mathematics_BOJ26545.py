# Mathematics_BOJ26545

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 정수의 개수를 input 받고
ans = 0                     # 정답을 저장할 변수를 생성한다
for n in range(N):          # 정수의 개수를 반복해서
    ans += int(input())     # 정답에 정수 값을 더하고
print(ans)                  # 정수의 합을 출력한다