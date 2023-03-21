# 두용액_BOJ2470

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # N 용액의 수
fluid = list(map(int, input().split()))         # 용액의 특성을 list 형태로 input받는다
fluid.sort()                                    # fluid를 오름차순으로 정렬한 후

A = 0                                           # A는 fluid 리스트의 맨 앞 원소의 인덱스를 저장한다
B = N-1                                         # B는 fluid 리스트의 맨 뒤 원소의 인덱스를 저장한다
ans = [2000000000,-1,-1]                        # 두 용액의 합이 최소가 되는 용액의 합과 인덱스를 저장할 리스트를 생성

while 1:                                        # break가 나올 때까지 반복해서
    if A == B:                                  # A와 B가 같은 원소를 가르키면
        break                                   # while문을 break
    mix = fluid[A] + fluid[B]                   # A와 B용액의 합을 mix에 저장하고
    if abs(mix) < ans[0]:                       # mix의 절대값이 ans에 저장된 최소값보다 작다면
        ans[0] = abs(mix)                       # ans의 최소값을 ans의 0번 인덱스에 저장하고
        ans[1] = A                              # A용액의 인덱스를 ans의 1번 인덱스에 저장하고
        ans[2] = B                              # B용액의 인덱스를 ans의 2번 인덱스에 저장한다
    if mix > 0:                                 # 두용액의 합이 양수라면
        B -= 1                                  # B를 앞으로 한칸 이동하고
    else:                                       # 두용액의 합이 음수라면
        A += 1                                  # A를 뒤로 한칸 이동한다

print(fluid[ans[1]], fluid[ans[2]])             # while문이 끝났다면 ans에 저장된 A와 B의 용액을 출력한다