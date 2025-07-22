# 속도 위반_BOJ11971

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())        # 도로의 속도제한 수와 달린 구간의 수를 input받고
ans = 0                                 # 정답을 저장할 변수를 생성한다
D = [0]*100                             # 구간별 속도를 저장할 리스트를 생성하고
tmp = 0                                 # 구간의 길이를 표시할 변수를 생성한다
for n in range(N):                      # 도로 구간을 반복해서
    A, B = map(int, input().split())    # 길이와 속도제한을 input받고
    for a in range(A):                  # 도로 길이를 반복해서
        D[tmp+a] = B                    # 속도 제한을 리스트에 저장하고
    else:                               # 도로가 끝났다면
        tmp += A                        # 끝난 도로를 변수에 저장한다
tmp2 = 0                                # 구간의 길이를 표시할 변수를 생성하고
for m in range(M):                      # 달린 구간을 반복해서
    A, B = map(int, input().split())    # 길이와 달린속도를 input받고
    for a in range(A):                  # 도로 길이를 반복해서
        if B > D[tmp2+a]:               # 속도를 위반했다면
            ans = max(ans, B-D[tmp2+a]) # 최대 속도 위반 값을 저장하고
    else:                               # 달린 구간이 끝났다면
        tmp2 += A                       # 구간의 위치를 변수에 저장한다
print(ans)                              # 최대 초과한 속도를 출력한다