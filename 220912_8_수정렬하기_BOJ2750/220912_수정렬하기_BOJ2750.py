# 수정렬하기_BOJ2750

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                # 비교할 숫자의 개수를 저장하고
ans = []                        # input 받을 숫자를 저장할 빈 리스트를 생성 후
for n in range(N):              # N만큼 반복하여
    ans.append(int(input()))    # ans에 input 받은 숫자를 append 한다
ans.sort()                      # ans를 크기순으로 정렬한 후
for a in ans:                   # 하나씩 출력한다
    print(a)