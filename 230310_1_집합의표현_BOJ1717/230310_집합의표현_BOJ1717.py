# 집합의표현_BOJ1717

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# input 받기
n, m = map(int, input().split())            # n 집합의 개수 / m 연산의 개수
setNum = dict()                             # 집합을 저장할 딕셔너리를 생성하고
for i in range(n+1):                        # 0부터 n까지 반복해서
    setNum[i] = i                           # key와 value가 같은 값이 되도록 딕셔너리에 원소를 생성한다

def find(N):
    if setNum[N] == N:                      # key와 value가 같다면
        return N                            # N을 그대로 return
    setNum[N] = find(setNum[N])             # 다르다면 N의 value값으로 다시 find 함수를 통해 key, value가 같은 값이 되는 숫자를 찾아 value로 저장한다 
    return setNum[N]                        # 새로 저장된 value의 값을 return

def union(x,y):                             
    x = find(x)                             # x가 key일 때 value 값을 x에 저장하고
    y = find(y)                             # y가 key일 때 value 값을 y에 저장한다
    if x > y:                               # x가 y보다 크다면
        setNum[x] = y                       # x가 key y가 value가 되고
    elif x == y:                            # x와 y가 같다면
        pass                                # pass
    else:                                   # x가 y보다 작다면
        setNum[y] = x                       # x가 value y가 key가 되고

for _ in range(m):                          # 연산의 개수를 반복해서
    X, a, b = map(int, input().split())     # X 합칠 것인지 확인할 것인지 여부 / a 집합 번호 / b 집합 번호
    if X:                                   # X가 1이라면 두 집합이 묶여있는지 확인하는 것이므로
        if find(a) == find(b):              # a가 key일 때 value와 b가 key일 때 value가 같다면 두 집합이 묶여있으므로
            print('YES')                    # YES를 출력하고
        else:                               # 다르다면 두 집합이 묶여있지 않으므로
            print('NO')                     # NO를 출력한다
    else:                                   # X가 0이라면 집합을 만드는 것이므로
        if a == b:                          # a와 b가 같으면
            pass                            # pass
        else:                               # 다르다면
            union(a, b)                     # 두 집합을 union 함수를 통해 묶어준다