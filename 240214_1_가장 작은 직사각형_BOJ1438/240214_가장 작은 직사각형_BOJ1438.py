# 가장 작은 직사각형_BOJ1438

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 점의 개수를 input 받고
dot = dict()                                # 점을 저장할 딕셔너리를 생성하고
dotx = set()                                # x의 값을 저장할 set을 생성한다
for _ in range(N):                          # 점의 개수를 반복해서
    a = list(map(int, input().split()))     # 점의 좌표를 input 받고
    if dot.get(a[0]) == None:               # x축이 key인 원소가 없을 때
        dot[a[0]] = [a[1]]                  # x가 key y가 value인 원소를 생성하고
    else:                                   # x축이 key인 원소가 있을 때
        dot[a[0]].append(a[1])              # y를 value에 append한다
    dotx.add(a[0])                          # x를 set에 add한다
dotx = sorted(list(dotx))                   # x를 오름차순으로 정렬한 후
ans = 1e9                                   # 정답을 저장할 변수를 생성한다
for s in range(len(dotx)):                  # x의 시작점을 반복하고
    for e in range(s, len(dotx)):           # x의 끝점을 반복해서
        tmp = []                            # x의 범위 안에 있는 점의 y값을 저장할 리스트를 생성한다
        for y in range(s, e+1):             # x의 범위를 반복해서
            tmp += dot[dotx[y]]             # 범위 안에 y값을 tmp에 모두 더해준다
        if len(tmp) == N//2:                # 점의 개수가 N//2개라면
            ans = min(ans, (dotx[e]-dotx[s]+2)*(max(tmp)-min(tmp)+2))               # ans와 tmp의 모든 점을 포함하는 사각형 중 작은 값을 저장한다
        elif len(tmp) > N//2:               # 점의 개수가 N//2개보다 크다면
            tmp.sort()                      # tmp를 오름차순으로 정렬한 후
            for t in range(len(tmp)-N//2+1):# N//2씩 반복할 때 맨 앞 인덱스를 반복해서
                ans = min(ans, (dotx[e]-dotx[s]+2)*(-(tmp[t])+(tmp[t+N//2-1])+2))   # ans와 t번부터 t+N//2-1까지 점을 포함하는 사각형 중 작은 값을 저장한다
print(ans)                                  # 직사각형 중 가장 넓이가 가장 작은 것의 넓이를 출력한다