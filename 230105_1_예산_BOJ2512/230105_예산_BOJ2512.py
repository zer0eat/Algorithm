# 예산_BOJ2512

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline().strip())                   # 예산을 신청한 지방의 수
lst = list(map(int, sys.stdin.readline().split()))      # 지방마다 신청한 예산의 액수를 리스트로 input 받음
money = int(sys.stdin.readline().strip())               # 예산의 최대액

if sum(lst) > money:                                    # 신청한 예산의 액수가 배정된 예산을 초과하는 경우
    lst.sort()                                          # 예산을 오름차순으로 정렬하고
    while lst:                                          # lst를 반복해서
        if lst[0]*N > money:                            # 리스트의 첫번째 예산만큼 모든 지방에 배분했을 때 예산을 초과한다면
            print(money//N)                             # 남은 예산액을 남은 지방의 수로 나눈 값을 출력하고
            break                                       # while문을 break
        else:                                           # 리스트의 첫번째 예산만큼 모든 지방에 배분했을 때 예산을 초과하지 않는다면
            money -= lst[0]                             # 해당 지방에 예산을 제공하고, 전체 예산액에서 해당 값을 뺀 후
            N -= 1                                      # 지방의 수에서 제공한 지방은 제외한다
            lst.pop(0)                                  # 배정한 예산도 리스트에서 제외한다
else:                                                   # 신청한 예산의 액수가 배정된 예산을 초과하지 않는 경우
    print(max(lst))                                     # 모든 지방에 원하는 액수를 배정하고 가장 많이 배정한 액수를 출력한다