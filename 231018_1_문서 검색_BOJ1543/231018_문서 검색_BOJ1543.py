# 문서 검색_BOJ1543

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = input().strip()                 # 문서의 정보를 input 받고
B = input().strip()                 # 검색하고 싶은 단어를 input 받는다
ans = 0                             # 문서에 등장하는 단어의 수를 저장할 변수를 생성하고
idx = 0                             # 문서 검색의 위치를 나타낼 변수를 생성한다
while idx < len(A)-len(B)+1:        # 문서의 맨 앞에서 마지막까지 단어를 반복할 때
    if A[idx:idx+len(B)] == B:      # idx에서 시작한 len(B) 길이의 단어가 B와 같다면
        ans += 1                    # 등장하는 수를 1 추가하고
        idx += len(B)               # 문서에서 단어를 검색하는 위치를 len(B)만큼 이동하고
    else:                           # idx에서 시작한 len(B) 길이의 단어가 B가 아니라면
        idx += 1                    # 문서에서 단어를 검색하는 위치를 1 이동한다
print(ans)                          # 중복되지 않게 등장하는 최대 수를 출력한다