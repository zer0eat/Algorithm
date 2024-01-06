# 2017 연세대학교 프로그래밍 경시대회_BOJ14568

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 사탕의 개수를 input 받고
ans = 0                         # 나누어 줄 수 있는 수를 저장할 변수를 생성하고
for i in range(1, N-1):         # 남규에게 줄 사탕을 1부터 N-2개까지 반복하고
    for j in range(1, N-1):     # 영훈이에게 줄 사탕을 1부터 N-2개까지 반복해서
        if i + j > N-1:         # 둘에게 나눠준 후 택희한테 나눠줄 사탕이 없다면
            break               # for문을 break한다
        if i >= j + 2:          # 남규가 영훈이보다 2개이상 받고
            if not (N-i-j)%2:   # 택희가 짝수개 받았다면
                ans += 1        # 나눠줄 수 있는 수를 1 추가한다
print(ans)                      # 규칙에 맞게 분배하는 방법의 수를 출력한다