# 스네이크버드_BOJ16435

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, L = map(int, sys.stdin.readline().split())           # N 과일의 수 / L 스네이크버드의 길이
fruit = list(map(int, sys.stdin.readline().split()))    # 과일의 높이를 리스트로 input 받음

fruit.sort()                                            # 과일의 높이를 오름차순으로 정렬해서

ans = L                                                 # 스네이크버드의 길이를 ans에 저장하고
for f in fruit:                                         # 과일의 높이를 반복해서
    if ans >= f:                                        # 과일의 높이가 스네이크버드의 길이보다 같거나 작다면
        ans += 1                                        # 스네이크버드의 길이를 늘리고
    else:                                               # 과일의 높이가 더 높다면
        break                                           # for문을 종료한다
print(ans)                                              # 스네이크 버드의 길이를 출력한다