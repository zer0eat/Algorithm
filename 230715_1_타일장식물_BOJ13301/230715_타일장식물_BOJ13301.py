# 타일장식물_BOJ13301

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                            # 직사각형 타일의 수
square = []                                                 # 타일의 한변의 길이를 저장할 리스트 생성
for i in range(N):                                          # 타일의 수를 반복해서
    if i == 0 or i == 1:                                    # 0, 1번째 원소인 경우에는
        square.append(1)                                    # 타일의 길이를 1로 append
    else:                                                   # 다른 원소의 경우에는
        square.append(square[i-1] + square[i-2])            # i-1, i-2번째 원소의 합을 append 한다
if N == 1:                                                  # N이 1인 경우에는
    print(4)                                                # 타일의 둘레가 4이므로 출력을 하고
else:                                                       # 그 이외의 경우는
    print(square[-1]*4 + square[-2]*2)                      # 둘레를 구해 출력한다