# 여행가자_BOJ1976

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # N 도시의 수
M = int(input())                            # M 여행지의 수

city = dict()                               # 도시를 저장할 딕셔너리 생성
for i in range(1, N+1):                     # 1부터 N까지 반복해서
    city[i] = i                             # key value를 해당 도시 번호로 딕셔너리 원소를 생성한다

def find(x):                                
    if city[x] == x:                        # key와 value가 같다면
        return x                            # x를 return
    city[x] = find(city[x])                 # 다르다면 x의 value값으로 다시 find 함수를 통해 key, value가 같은 값이 되는 숫자를 찾아 value로 저장한다
    return city[x]                          # 새로 저장된 value의 값을 return

def union(x, y):
    x = find(x)                             # x가 key일 때 value 값을 x에 저장하고
    y = find(y)                             # y가 key일 때 value 값을 y에 저장한다
    if x > y:                               # x가 y보다 크다면
        city[x] = y                         # x가 key y가 value가 되고
    else:                                   # 그렇지 않다면
        city[y] = x                         # x가 value y가 key가 된다

for i in range(1, N+1):                     # 1부터 N까지 반복해서
    A = list(map(int, input().split()))     # i번 도시와 연결된 도시의 리스트를 input 받고
    for j in range(i+1, N+1):               # i 다음도시부터 N번 도시까지 반복해서
        if A[j-1] == 1:                     # i와 j 도시가 연결되어 있다면
            union(i, j)                     # union 함수로 연결해준다

travel = list(map(int, input().split()))    # 여행다닐 도시를 리스트로 input 받고

tmp = find(travel[0])                       # 시작도시가 key인 value를 저장한다
for v in range(1, len(travel)):             # 여행다닐 도시 리스트를 1번 인덱스부터 반복해서
    if find(travel[v]) == tmp:              # 해당 도시의 value와 tmp가 같다면 연결되어있으므로
        pass                                # 패스
    else:                                   # 그렇지 않다면 연결되어있지 않으므로
        print('NO')                         # NO를 출력하고
        break                               # for문을 break 한다
else:                                       # 모든 도시가 연결되어 있다면
    print('YES')                            # YES를 출력한다