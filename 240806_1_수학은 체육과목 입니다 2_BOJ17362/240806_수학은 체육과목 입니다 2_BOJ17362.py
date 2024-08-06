# 수학은 체육과목 입니다 2_BOJ17362

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 손가락을 접을 횟수를 input 받고
N %= 8              # 손가락 접을 횟수를 8로 나눈 나머지를 저장해서
if N == 1:          # 나머지가 1이라면
    print(1)        # 엄지손가락을 출력한다
elif N in [0,2]:    # 나머지가 0,2 라면
    print(2)        # 검지손가락을 출력한다
elif N in [3,7]:    # 나머지가 3,7 이라면
    print(3)        # 중지손가락을 출력한다
elif N in [4,6]:    # 나머지가 4,6 이라면
    print(4)        # 약지손가락을 출력한다
else:               # 나머지가 5라면
    print(5)        # 새끼손가락을 출력한다