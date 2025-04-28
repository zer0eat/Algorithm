# Speed fines are not fine_BOJ6763

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
limit = int(input())        # 제한 속도를 input 받고
speed = int(input())        # 현재 속도를 input 받고
X = speed - limit           # 초과된 속도를 계산헤서
if 0 < X and X <= 20:       # 20키로까지 초과하면
    print('You are speeding and your fine is $100.')    # 100달러의 벌금을 청구하고
elif 20 < X and X <= 30:    # 30키로까지 초과하면
    print('You are speeding and your fine is $270.')    # 270달러의 벌금을 청구하고
elif X > 30:                # 30보다 더 초과하면
    print('You are speeding and your fine is $500.')    # 500달러의 벌금을 청구하고
else:                       # 제한 속도를 지킨다면
    print('Congratulations, you are within the speed limit!')   # 축하내용을 출력한다