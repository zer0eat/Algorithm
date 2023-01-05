# 중복빼고정렬하기_BOJ10867

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = input()                             # 요소의 개수
ans = set(map(int, input().split()))    # 요소를 set으로 input 받아 중복을 없앤 후
ans = list(ans)                         # set을 list로 변경 후
ans.sort()                              # 오름차순 정렬하고
print(*ans)                             # 정답을 출력한다
