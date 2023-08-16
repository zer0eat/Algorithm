# 막대기_BOJ1094

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
X = int(input())                # 만드려는 막대기의 길이를 input 받고
N = [64, 32, 16, 8, 4, 2, 1]    # 만들 수 있는 막대의 길이를 담은 리스트를 생성한다
cnt = 0                         # 막대기의 개수를 셀 변수를 생성하고
for i in N:                     # 막대기 리스트를 반복해서
    if X >= i:                  # 만드려는 막대기보다 비교하는 막대기가 작거나 같다면
        cnt += 1                # 개수를 하나 추가하고
        X -= i                  # 길이를 i만큼 빼준다
    if X == 0:                  # 만드려는 막대기의 길이를 모두 충족했다면
        print(cnt)              # 개수를 출력하고
        break                   # for문을 break한다