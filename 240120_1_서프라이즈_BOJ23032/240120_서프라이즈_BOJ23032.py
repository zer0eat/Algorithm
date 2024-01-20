# 서프라이즈~_BOJ23032

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 학생의 수를 input 받고
W = list(map(int, input().split()))     # 학생이 원하는 스테이크의 양을 리스트로 input 받는다
minN = 1e9                              # 두 그룹이 원하는 스테이크 양의 차를 저장할 변수를 생성하고
maxN = 0                                # 스테이크 양의 차가 최소가 되는 두 그룹이 원하는 스테이크 양의 합을 저장할 변수를 생성한다
for mid in range(1, N):                 # 그룹을 나눌 기준을 반복해서
    l = W[mid-1]                        # 왼쪽 그룹이 원하는 스테이크 양을 저장할 변수를 생성하고
    r = W[mid]                          # 오른쪽 그룹이 원하는 스테이크 양을 저장할 변수를 생성한다
    lpoint = mid-1                      # 왼쪽 그룹을 가르키는 포인터를 생성하고
    rpoint = mid                        # 오른쪽 그룹을 가르키는 포인터를 생성한다
    while 1:                            # break가 나올때 까지 반복해서
        if abs(l-r) < minN:             # 두 그룹의 차가 현재 저장된 최소값보다 작다면
            minN = abs(l-r)             # 새로운 두 그룹의 차를 저장하고
            maxN = l + r                # 두 그룹의 합을 저장한다
        elif abs(l-r) == minN:          # 두 그룹의 차가 현재 저장된 최소값과 같다면
            maxN = max(maxN, l + r)     # 두 그룹의 합과 저장된 합 중 더 큰 값으로 갱신한다
        if l-r < 0:                     # 왼쪽 그룹보다 오른쪽 그룹이 더 크다면
            lpoint -= 1                 # 왼쪽 포인터를 한칸 이동하고
            if lpoint < 0:              # 왼쪽 포인터가 0보다 작아지면
                break                   # while문을 종료한다
            l += W[lpoint]              # 이동된 지점의 무게를 왼쪽 그룹에 더한다
        else:                           # 왼쪽 그룹보다 오른쪽 그룹이 더 작거나 같다면
            rpoint += 1                 # 오른쩍 포인터를 한칸 이동하고
            if rpoint > N-1:            # 오른쪽 포인터가 학생수 밖을 가르키면
                break                   # while문을 종료한다
            r += W[rpoint]              # 이동된 지점의 무게를 오른쪽 그룹에 더한다
print(maxN)                             # 두 그룹의 차가 최소가 될 때 두 그룹의 합을 출력한다