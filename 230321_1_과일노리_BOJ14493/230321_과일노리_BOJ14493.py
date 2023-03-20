# 과일노리_BOJ14493

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 거쳐가야하는 구간의 수
ans = 0                                 # 접속하기 위해 필요한 최소 시간을 저장할 변수 생성
for _ in range(N):                      # 구간의 수를 반복해서
    a, b = map(int, input().split())    # a 쉬는 시간 / b 활동하는 시간
    tmp = ans                           # 현재 걸린 시간을 tmp에 저장하고
    while 1:                            # break가 나올때까지 반복해서
        if tmp < b:                     # tmp가 활동시간안에 있다면
            ans += (b-tmp+1)            # 활동이 남은 시간인 b-tmp만큼 더한 후 이동 시간 1초를 추가로 더하고 
            break                       # while문을 break
        else:                           # 현재 시간이 활동시간 이후라면 
            tmp -= b                    # tmp에서 b를 빼준다
        if tmp < a:                     # tmp가 휴식시간안에 있다면
            ans += 1                    # 이동 가능하므로 ans에 1초를 더하고
            break                       # while문을 break
        else:                           # 현재 시간이 휴식시간 이후라면 
            tmp -= a                    # tmp에서 a를 빼준다
print(ans)                              # 모든 구간을 통과한 후 ans를 출력한다