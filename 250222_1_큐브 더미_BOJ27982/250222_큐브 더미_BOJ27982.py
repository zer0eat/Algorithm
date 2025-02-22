# 큐브 더미_BOJ27982

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())            # N 입체공간의 크기 / M 큐브의 수를 input 받고
ans = 0                                     # 정답을 저장할 변수를 생성한다
dic = dict()                                # 큐브의 위치를 저장할 딕셔너리를 생성하고
for m in range(M):                          # 큐브의 수를 반복해서
    i, j, k = map(int, input().split())     # 큐브의 위치를 input 받고
    dic[(i,j,k)] = 1                        # 큐브의 위치를 저장한다
for d in dic:                               # 큐브의 위치를 반복해서
    if dic.get((d[0]+1,d[1],d[2])) != 1:    # 큐브의 옆에 위치가 없다면
        continue                            # 넘어간다
    if dic.get((d[0]-1,d[1],d[2])) != 1:    # 큐브의 옆에 위치가 없다면
        continue                            # 넘어간다
    if dic.get((d[0],d[1]+1,d[2])) != 1:    # 큐브의 옆에 위치가 없다면
        continue                            # 넘어간다
    if dic.get((d[0],d[1]-1,d[2])) != 1:    # 큐브의 옆에 위치가 없다면
        continue                            # 넘어간다
    if dic.get((d[0],d[1],d[2]+1)) != 1:    # 큐브의 옆에 위치가 없다면
        continue                            # 넘어간다
    if dic.get((d[0],d[1],d[2]-1)) != 1:    # 큐브의 옆에 위치가 없다면
        continue                            # 넘어간다
    ans += 1                                # 큐브의 옆에 모두 있다면 개수를 추가한다
print(ans)                                  # 조건을 만족하는 큐브의 수를 출력한다