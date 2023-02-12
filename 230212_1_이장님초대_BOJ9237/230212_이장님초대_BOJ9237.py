# 이장님초대_BOJ9237

# input.txt 열기
import sys
sys.stdin = open("input.txt")

# input 받기
N = int(sys.stdin.readline().strip())                   # 묘목의 개수를 input 받고
seed = list(map(int, sys.stdin.readline().split()))     # 묘목이 자라는 시간을 input 받는다

seed.sort(reverse=True)                                 # 내림차순으로 정렬한 뒤

ans = 0                                                 # 정답을 저장할 변수를 생성하고
for i in range(N):                                      # N만큼 반복해서
    A = i + seed[i]                                     # A에 씨를 심은 날짜와 자라는 시간을 저장한 뒤
    if A > ans:                                         # A가 ans보다 오래걸린다면
        ans = A                                         # ans를 A로 바꾸고
else:                                                   # 모든 반복을 마쳤다면
    print(ans+2)                                        # ans에 씨를 심는 날과 모두 자란 다음날 이장님을 부르는 날을 더하여 출력한다