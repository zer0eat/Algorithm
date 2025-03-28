# 영수증_BOJ5565

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = int(input())      # 책 전체 가격을 input 받고
for book in range(9):   # 9권의 책을 반복해서
    ans -= int(input()) # 책 가격을 빼고
print(ans)              # 남은 책의 가격을 출력한다