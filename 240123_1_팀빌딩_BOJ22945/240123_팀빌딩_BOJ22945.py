# 팀빌딩_BOJ22945

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 개발자의 수를 input 받고
X = list(map(int, input().split()))         # 개발자의 능력치를 리스트로 input 받는다
ans = 0                                     # 정답을 저장할 변수를 생성하고
l = 0                                       # 왼쪽 개발자를 가르킬 포인터를 생성하고
r = N-1                                     # 오른쪽 개발자를 가르킬 포인터를 생성한다
while l < r:                                # 두 포인터가 같은 사람을 가르킬 때까지 반복해서
    people = r-l-1                          # 두 포인터 사이의 사람의 수를 저장하고
    ans = max(ans, min(X[l], X[r])*people)  # ans에 저장된 값과 현재 능력치 중 더 큰 값을 저장하고
    if X[l] < X[r]:                         # 오른쪽 개발자가 더 능력치가 크다면
        l += 1                              # 왼쪽 개발자를 한칸 이동하고
    else:                                   # 왼쪽 개발자가 더 능력치가 크다면
        r -= 1                              # 오른쪽 개발자를 한칸 이동한다
print(ans)                                  # 팀의 능력치 최댓값을 출력한다