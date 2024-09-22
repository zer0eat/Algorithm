# 정보섬의 대중교통_BOJ28113

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, A, B = map(int, input().split()) # N 지하철까지 걷는시간 / A 버스가 오는 시간 / B 지하철이 오는 시간을 input 받고
if A < B:                           # 버스가 지하철보다 먼저오면
    print('Bus')                    # 버스를 출력하고
elif B < A:                         # 지하철이 버스보다 먼저오면
    print('Subway')                 # 지하철을 출력하고
else:                               # 동시에 오면 
    print('Anything')               # Anything을 출력한다