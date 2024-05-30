# 사장님 도박은 재미로 하셔야 합니다_BOJ23795

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 0                 # 잃은 돈을 저장할 변수를 생성하고
while 1:                # break가 나올 때까지 반복한다
    m = int(input())    # 베팅한 돈을 input 받고
    if m == -1:         # 돈이 -1이라면
        break           # while문을 break하고
    else:               # 베팅한 돈이 양수라면
        ans += m        # ans에 베팅한 돈을 더한다
print(ans)              # 도박판에서 버린 돈의 총 합을 출력한다