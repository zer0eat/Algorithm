# 용액합성하기_BOJ14921

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # N input 받을 용액의 수
solution = list(map(int, input().split()))      # 용액의 특성을 list로 input
solution.sort()                                 # 용액의 특성을 오름차순으로 정렬

A = 0                                           # 수열의 맨 앞의 정수를 가르킨 A
B = N-1                                         # 수열의 맨 앞의 정수를 가르킨 B
ans = 200000001                                 # 두 용액의 합이 최소가 되는 값을 저장할 변수 생성
while A < B:                                    # A가 B보다 작다면 반복해서
    mix = solution[A] + solution[B]             # A가 가르키는 수와 B가 가르키는 수를 더해 mix에 저장한다
    if abs(mix) < abs(ans):                     # mix의 절대값이 ans의 절대값보다 작다면
        ans = mix                               # ans를 mix로 변경하고
    elif mix > 0:                               # mix가 양수일 때는
        B -= 1                                  # B를 왼쪽으로 한 칸 이동한다
    elif mix < 0:                               # mix가 음수일 때는
        A += 1                                  # A를 오른쪽으로 한 칸 이동한다
    else:                                       # mix가 0일 때는
        print(0)                                # 0을 출력하고
        quit()                                  # 종료한다
print(ans)                                      # A가 B와 같거나 커졌다면 저장되어 있는 두수의 합이 최소가 되는 값을 출력한다