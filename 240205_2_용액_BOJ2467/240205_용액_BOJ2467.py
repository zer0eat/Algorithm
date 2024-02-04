# 용액_BOJ2467

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 용액의 수를 input 받고
solution = list(map(int, input().split()))          # 용액의 특성을 리스트롤 input 받는다
ans = 10000000000                                   # 정답을 저장할 변수를 생성하고
ans2 = [0, 0]                                       # 두 용액을 저장할 리스트를 생성하다
for n in range(N-1):                                # 두 용액 중 하나를 반복해서
    l = n+1                                         # n+1을 왼쪽 포인터로 생성하고
    r = N-1                                         # N-1을 오른쪽 포인터로 생성한다
    while l <= r:                                   # l이 r보다 커질때 까지 반복해서
        mid = (l+r)//2                              # l과 r의 중간점을 mid에 저장한다
        if abs(solution[n] + solution[mid]) < ans:  # 두 용액의 합의 절대값이 ans보다 작다면
            ans = abs(solution[n] + solution[mid])  # ans를 두 용액의 합으로 저장하고
            ans2 = [solution[n], solution[mid]]     # ans2에 두 용액의 특성을 저장한다
        if solution[n] + solution[mid] < 0:         # 두 용액의 합이 음수라면
            l = mid+1                               # l을 mid+1로 저장한다
        elif solution[n] + solution[mid] > 0:       # 두용액의 합이 양수라면
            r = mid-1                               # r을 mid-1로 저장한다
        else:                                       # 두용액의 합이 0이라면
            print(*ans2)                            # 두 용액을 출력하고
            quit()                                  # 종료한다
print(*ans2)                                        # 두 용액을 출력한다