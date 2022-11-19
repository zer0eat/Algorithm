# 약수_BOJ1037

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                           # 약수의 개수
A = list(map(int, sys.stdin.readline().split()))        # 약수를 리스트로 받음

print(max(A)*min(A))                                    # A의 모든 숫자를 약수로 갖는 숫자 출력