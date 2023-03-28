# 세용액_BOJ2473

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                # N 전체 용액의 수
solution = list(map(int, input().split()))                      # 전체 용액의 특성을 리스트로 input
solution.sort()                                                 # 전체 용액을 오름차순으로 정렬

ans = 3000000001                                                # 세 용액의 합이 0과 가장 가까운 값을 저장할 변수 생성
ans3 = [-1, -1, -1]                                             # 세 용액의 합이 0과 가장 가까운 세 용액을 저장할 리스트 생성

for i in range(N-2):                                            # 맨 앞에서 뒤에서 세번째 용액까지 반복해서
    A = i + 1                                                   # A는 i 용액 다음을 가르키고
    B = N - 1                                                   # B는 맨 뒤의 용액을 가르킨다
    while A < B:                                                # A가 B보다 작으면 반복해서
        mix = solution[i] + solution[A] + solution[B]           # 세용액의 합을 mix에 저장한다
        if abs(ans) > abs(mix):                                 # mix의 절대값이 ans의 절대값보다 작으면
            ans = mix                                           # ans를 mix로 바꿔 저장하고
            ans3 = [solution[i], solution[A], solution[B]]      # ans3에 세용액의 특성을 저장한다
        elif mix == 0:                                          # 세 용액의 합이 0이면
            print(solution[i], solution[A], solution[B])        # 세 용액의 특성을 출력하고
            quit()                                              # 종료한다
        elif mix > 0:                                           # 세 용액의 합이 0보다 크면
            B -= 1                                              # B를 왼쪽으로 한칸 이동시킨다
        else:                                                   # 세 용액의 합이 0보다 작으면
            A += 1                                              # A를 오른쪽으로 한칸 이동시킨다
print(*ans3)                                                    # 모든 용액의 탐색을 마쳤다면 ans3에 저장된 세 용액의 특성을 출력한다