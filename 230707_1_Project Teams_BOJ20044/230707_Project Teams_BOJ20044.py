# Project Teams_BOJ20044

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 팀의 수
lst = list(map(int, input().split()))   # 학생의 코딩 역량을 리스트로 input 받고
lst.sort()                              # 오름차순으로 정렬한다
ans = 500000001                         # 팀의 코딩역량의 합을 저장할 변수를 생성하고
for i in range(N):                      # 팀의 수를 반복해서
    tmp = lst[i] + lst[-i-1]            # 정렬된 리스트에서 가운데를 기준으로 대칭으로 코딩역량의 합을 tmp에 더한 후
    ans = min(ans, tmp)                 # ans와 tmp 중 더 작은 값을 ans에 저장한다
print(ans)                              # 모든 팀을 구성 후 가장 낮은 코딩역량의 합을 출력한다