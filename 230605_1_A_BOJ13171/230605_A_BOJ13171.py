# A_BOJ13171

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = int(input())                    # 거듭제곱의 밑을 input 받고
X = int(input())                    # 거듭제곱의 지수를 input 받는다
ans = 1                             # 정답을 저장할 변수를 생성하고

for i in bin(X)[2:][::-1]:          # 지수를 이진수로 바꾼후 뒤집에서 반복한다
    if i == '1':                    # 이진수의 해당 자리가 1인 경우
        ans = ans * A % 1000000007  # ans에 A를 곱한 후 나눠야하는 수로 나눈다
    A = A ** 2 % 1000000007         # A를 제곱하고 나눠야하는 수로 나눈 값을 A에 저장한다

print(ans)                          # 정답을 출력한다