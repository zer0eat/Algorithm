# Cupcake Party_BOJ24568

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
R = int(input())        # 8개 짜리 컵케이크 세트를 input 받고
S = int(input())        # 3개 짜리 컵케이크 세트를 input 받고
cupcakes = R*8 + S*3    # 컵케이크의 개수를 저장한 후
print(cupcakes-28)      # 28명에게 컵케이크를 나눠주고 남은 수를 출력한다