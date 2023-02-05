# 성적통계_BOJ5800

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline().strip())                                   # 반의 수를 입력반고
for i in range(N):                                                      # 반의 수를 반복해서
    lst = list(map(int, sys.stdin.readline().split()))                  # 학생의 수와 점수를 list로 input 받는다
    lst.pop(0)                                                          # 학생의 수를 pop 하고
    lst.sort()                                                          # 점수를 오름차순으로 정렬한 뒤
    gap = 0                                                             # 인접한 점수차이를 저장할 변수를 생성한다
    for l in range(len(lst)-1):                                         # 수학점수를 반복해서
        if lst[l+1] - lst[l] > gap:                                     # 두 점수의 차가 gap보다 크면
            gap = lst[l+1] - lst[l]                                     # gap을 해당 점수로 바꿔준 뒤
    print(f'Class {i+1}')                                               # 반을 출력하고
    print(f'Max {max(lst)}, Min {min(lst)}, Largest gap {gap}')         # 가장 높은 점수, 가장 낮은 점수, 가장 큰 인접한 점수차를 출력한다  