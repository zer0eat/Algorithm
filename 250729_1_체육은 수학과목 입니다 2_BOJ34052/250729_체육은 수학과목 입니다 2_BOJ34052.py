# 체육은 수학과목 입니다 2_BOJ34052

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 300               # 정답을 저장할 변수를 생성하고
for n in range(4):      # 4바퀴를 반복해서
    ans += int(input()) # 변수에 각 바퀴의 시간을 더해주고
if ans <= 1800:         # 총 시간이 1800초 이하라면
    print('Yes')        # Yes를 출력하고
else:                   # 총 시간이 1800초 초과라면
    print('No')         # No를 출력한다