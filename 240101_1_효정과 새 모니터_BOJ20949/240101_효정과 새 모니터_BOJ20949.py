# 효정과 새 모니터_BOJ20949

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                        # 모니터의 개수를 input 받고
ans = []                                                # 모니터의 PPI를 저장할 리스트를 생성한다
for i in range(N):                                      # 모니터의 수를 반복해서
    W, H = map(int, input().split())                    # 가로의 픽셀과 세로의 픽셀을 input 받고
    ans.append([W**2+H**2, i+1])                        # ans에 [PPI, 모니터번호]를 append한다
ans.sort(reverse=True, key=lambda x: (x[0], -x[1]))     # ans의 0번 원소를 내림차순으로 정렬하고 같은 경우 1번 원소를 오름차순으로 정렬한다
for a in ans:                                           # 정답을 반복해서
    print(a[1])                                         # PPI가 높은 순으로 모니터 번호를 출력한다