# 수정렬하기2_BOJ2751

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())               # 테스트 케이스
ans = []                                    # 정렬할 수를 저장할 리스트
for t in range(T):                          # 정렬할 수만큼 반복해서
    ans.append(int(sys.stdin.readline()))   # ans에 append
else:                                       # 모두 append 했으면
    ans.sort()                              # 정렬하고
    for a in ans:                           # 차례대로 출력
        print(a)
