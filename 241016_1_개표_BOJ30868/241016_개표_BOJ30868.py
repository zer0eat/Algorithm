# 개표_BOJ30868

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                # 테스트 케이스를 input 받고
for t in range(T):              # 테스트 케이스를 반복해서
    num = int(input())          # 숫자를 input 받고
    ans = ''                    # 정답을 저장할 변수를 생성한다
    if num >= 5:                # 숫자가 5보다 크면
        ans += '++++ '*(num//5) # 5보다 큰 수만큼 ++++를 저장하고
        num %= 5                # 5로 나눈 나머지를 저장한다
    ans += '|'*num              # 남은 수를 |만큼 더해준다
    print(ans)                  # num을 표시한 수를 출력한다