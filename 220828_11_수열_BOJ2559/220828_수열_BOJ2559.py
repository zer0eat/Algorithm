# 수열_BOJ2559

# input.txt 열기
import sys
sys.stdin = open('input2.txt')

# input 받기
N, K = map(int, input().split())                                # N = 온도를 측정한 전체 날짜의 수 / K = 연속적인 날짜의 수
temperature = list(map(int, input().split()))                   # 매일 측정한 온도

# 시간초과
# tempK = 0
# for i in range(N - K + 1):
#     tmp = 0
#     for j in range(K):
#         tmp += temperature[i + j]
#     else:
#         if tempK < tmp:
#             tempK = tmp
#         else:
#             pass
# print(tempK)

tmp = 0                                                         # K개의 온도를 더한 값
for i in range(K):                                              # K만큼 반복해서
    tmp += temperature[i]                                       # tmp에 처음 K일 온도의 합을 저장해줌

tempK = tmp                                                     # 기온의 합의 최고값을 찾기 위한 변수

ts = 0                                                          # tmp에서 뺄 온도의 인덱스
te = K                                                          # tmp에 더할 온도의 인덱스
while ts < N-K:                                                 # K일의 온도의 합을 모두 탐색할때 까지 반복
    if tempK < tmp - temperature[ts] + temperature[te]:         # 최고기온 tempK 보다 새로운 K일의 합이 높을 때
        tmp = tmp - temperature[ts] + temperature[te]           # tmp를 새로운 K일의 합으로 바꿔주고
        tempK = tmp                                             # tempK도 새로운 최대값으로 바꿔준다
    else:                                                       # 최고기온보다 낮다면
        tmp = tmp - temperature[ts] + temperature[te]           # tmp를 새로운 K일의 합으로 바꿔준다
    ts += 1                                                     # 뺄 온도의 인덱스를 다음으로 옮겨주고
    te += 1                                                     # 더할 온도의 인덱스를 다음으로 옮겨준다

print(tempK)                                                    # K일 온도의 합중 제일 높은 것을 출력한다