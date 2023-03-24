# 용액_BOJ2467

# input.txt 열기 
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # N 용액의 수
fluid = list(map(int, input().split()))     # 용액의 특성을 list 형태로 input받는다

A = 0                                       # A는 fluid 리스트의 맨 앞 원소의 인덱스를 저장한다
B = N-1                                     # B는 fluid 리스트의 맨 뒤 원소의 인덱스를 저장한다
ans = 2000000000                            # 두 용액의 합을 저장할 변수 생성
ab = [0, 0]                                 # 두용액의 위치를 저장할 리스트 생성

while A < B:                                # A가 B와 같거나 커질 때까지 반복해서
    mix = fluid[A] + fluid[B]               # A와 B용액의 합을 mix에 저장하고
    if abs(mix) < ans:                      # mix의 절대값이 ans에 저장된 최소값보다 작다면
        ans = abs(mix)                      # 최소값을 ans에 저장하고
        ab[0] = fluid[A]                    # A용액을 ab의 0번 인덱스에 저장하고
        ab[1] = fluid[B]                    # B용액을 ab의 1번 인덱스에 저장한다
    elif mix > 0:                           # mix의 합이 양수라면
        B -= 1                              # B를 오른쪽으로 한칸 이동한다
    else:                                   # mix의 합이 음수라면
        A += 1                              # A를 왼쪽으로 한칸 이동한다

print(*ab)                                  # ab에 저장된 두 용액을 출력한다