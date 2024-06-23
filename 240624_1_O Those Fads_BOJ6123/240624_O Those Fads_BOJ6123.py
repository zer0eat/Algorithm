# O Those Fads_BOJ6123

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, L, K = map(int, input().split())     # N 소의 수 / L 유행 지수 / K 유행 증가 값을 input 받고
cows = [int(input()) for _ in range(N)] # 소마다 유행의 역치를 input 받는다
ans = 0                                 # 정답을 저장할 변수를 생성하고
cows.sort()                             # 소들의 유행 저항 역치를 오름차순으로 정렬한다
for cow in cows:                        # 유행저항을 반복해서
    if L >= cow:                        # 소의 유행 저항이 유행 지수보다 같거나 작다면
        ans += 1                        # 유행에 참여하는 소의 수를 추가하고
        L += K                          # 유행저항을 K만큼 증가시킨다
    else:                               # 유행저항이 가능한 소가 나오면
        break                           # for문을 break한다
print(ans)                              # 유행에 참여하는 소의 수를 출력한다