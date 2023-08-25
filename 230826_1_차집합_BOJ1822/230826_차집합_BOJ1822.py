# 차집합_BOJ1822

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())            # A A집합의 원소 수 / B B집합의 원소 수
gA = set(map(int, input().split()))         # A 집합의 원소를 set으로 저장한다
gB = set(map(int, input().split()))         # B 집합의 원소를 set으로 저장한다
ans = gA - gB                               # ans에 A와 B의 차집합을 구해 저장하고
print(len(ans))                             # 차집합의 원소의 수를 출력한다
ans = list(ans)                             # 집합을 리스트형식으로 바꿔주고
ans.sort()                                  # 오름차순 정렬한 뒤
print(*ans)                                 # 차집합의 원소를 출력한다