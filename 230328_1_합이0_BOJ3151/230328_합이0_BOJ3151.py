# 합이0_BOJ3151

# imput.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import Counter


# input 받기
N = int(input())                                        # N 학생 수
student = list(map(int, input().split()))               # 학생의 코딩 실력을 리스트로 input 받고
student.sort()                                          # 오름차순으로 정렬한다
cnt = Counter(student)                                  # 해당학생과 같은 점수의 학생의 수를 찾기 위해 사용

ans = 0                                                 # 팀의 수를 저장할 변수 생성
for n in range(N-2):                                    # 3명 중 한명을 반복해서
    A = n + 1                                           # 나머지 두명 중 한명을 가르킬 포인터를 n 뒤에
    B = N - 1                                           # 나머지 두명 중 한명을 가르킬 포인터를 N-1에 둔다
    while A < B:                                        # A가 B보다 작으면 반복해서
        team = student[n] + student[A] + student[B]     # team에 세사람의 합을 저장한다
        if team == 0:                                   # 세사람의 합이 0이 되면
            if student[A] == student[B]:                # A와 B의 점수가 같다면
                ans += B - A                            # ans에 B - A를 뺀 수를 더한다
            else:                                       # A와 B의 점수가 다르다면
                ans += cnt[student[B]]                  # ans에 B와 같은 점수인 학생의 수를 더한다
            A += 1                                      # A를 오른쪽으로 한 칸 이동한다
        elif team < 0:                                  # 세사람의 합이 0보다 작다면
            A += 1                                      # A를 오른쪽으로 한 칸 이동한다
        else:                                           # 세사람의 합이 0보다 크다면
            B -= 1                                      # B를 왼쪽으로 한 칸 이동한다
print(ans)                                              # ans에 저장된 경우의 수를 출력한다
