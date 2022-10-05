# 나이순정렬_BOJ10814

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())               # 테스트 케이스
ans = []                                    # input 받은 값을 저장할 리스트
for t in range(T):                          # 테스트 케이스를 반복할 때
    a, b = sys.stdin.readline().split()     # a에 나이를 저장하고 b에 이름을 저장한 후
    a = int(a)                              # a를 int로 변환한다
    ans.append([a,t,b])                     # ans리스트에 [나이, 가입순서, 이름] 순으로 append 한 후
ans.sort()                                  # 오름차순으로 정렬한다

for n in ans:                               # 정렬한 것을 하나씩 출력할 때
    print(n[0], n[2])                       # 나이와 이름만 출력한다