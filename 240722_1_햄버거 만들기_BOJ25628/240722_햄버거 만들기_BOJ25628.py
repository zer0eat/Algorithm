# 햄버거 만들기_BOJ25628

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
a, b = map(int, input().split())    # a 빵의 수 b 패티의 수를 input 받고
print(min(a//2, b))                 # 만들 수 있는 햄버거의 수를 출력한다