# 두수의합_BOJ9024

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):                              # 테스트 케이스를 반복해서
    N, K = map(int, input().split())            # N input 받을 정수의 개수 / K 두 수의 합이 가까워야하는 기준이 되는 수
    lst = list(map(int, input().split()))       # N개의 숫자를 input 받아 리스트로 저장
    lst.sort()                                  # input 받은 리스트를 오름차순으로 정렬
    
    minMix = 300000001                          # 두수의 합과 K와의 거리를 저장할 변수 생성
    ans = 0                                     # 두수의 합과 K의 거리가 최소가 되는 조합의 수를 저장할 변수 생성
    A = 0                                       # 리스트의 맨 앞을 가르키는 변수 생성
    B = N-1                                     # 리스트의 맨 뒤를 가르키는 변수 생성
    while A < B:                                # A가 B보다 작으면 반복해서
        mix = lst[A] + lst[B] - K               # 두수의 합과 K와의 거리를 계산해서 mix에 저장
        if abs(mix) < abs(minMix):              # mix의 절대값이 minMix의 절대값보다 작으면
            minMix = mix                        # minMix에 mix를 저장하고
            ans = 1                             # ans를 1로 저장한 후
            if mix > 0:                         # mix가 0보다 크면
                B -= 1                          # B를 오른쪽으로 한칸 이동하고
            else:                               # mix가 0보다 작거나 같다면
                A += 1                          # A를 왼쪽으로 한칸 이동한다
        elif abs(mix) == abs(minMix):           # mix의 절대값이 minMix의 절대값과 같다면
            ans += 1                            # ans에 1을 추가한다
            if mix > 0:                         # mix가 0보다 크면
                B -= 1                          # B를 오른쪽으로 한칸 이동하고
            else:                               # mix가 0보다 작거나 같다면
                A += 1                          # A를 왼쪽으로 한칸 이동한다
        elif mix > 0:                           # mix가 0보다 크면
            B -= 1                              # B를 오른쪽으로 한칸 이동하고
        else:                                   # mix가 0보다 작거나 같다면
            A += 1                              # A를 왼쪽으로 한칸 이동한다
    print(ans)                                  # A가 B와 같아지면 조합의 수를 출력한다
