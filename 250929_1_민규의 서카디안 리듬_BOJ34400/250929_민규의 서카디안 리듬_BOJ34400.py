# 민규의 서카디안 리듬_BOJ34400

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())            # 테스트 케이스를 input받고
for t in range(T):          # 테스트 케이스를 반복해서
    t = int(input())        # 시간을 input받고
    t %= 25                 # 생체리듬을 계산해서 
    if t < 17:              # 생체리듬이 17시간 이내라면
        print('ONLINE')     # 깨어 있다고 출력하고
    else:                   # 생체리듬이 17시간 이후라면
        print('OFFLINE')    # 자고 있다고 출력한다