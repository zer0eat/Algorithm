# 치즈버거 만들기_BOJ30017

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # A 패티의 수와 B 치즈의 수를 input 받고
if A <= B+1:                        # 패티 수보다 치즈+1 수가 같거나 크다면 
    print(2*A-1)                    # 패티 수의 두배에 치즈를 하나 뺀 크기를 출력한다
else:                               # 치즈가 패티에 비해 부족하다면
    print(2*B+1)                    # 치즈 수의 두배에 패티를 하나 더한 크기를 출력한다