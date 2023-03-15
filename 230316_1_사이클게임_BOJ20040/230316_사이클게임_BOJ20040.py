# 사이클게임_BOJ20040

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
n, m = map(int, input().split())        # n 점의 개수 / m 선을 그을 횟수

def find(x):
    if line[x] == x:                    # key와 value가 모두 x라면
        return x                        # x를 return
    line[x] = find(line[x])             # 다르다면 x의 value값으로 다시 find 함수를 통해 key, value가 같은 값이 되는 숫자를 찾아 value로 저장한다
    return line[x]                      # 바뀐 value를 return

def union(x,y):
    global cnt                          # cnt를 global로 불러와서
    x = find(x)                         # x가 key일 때 value 값을 x에 저장하고
    y = find(y)                         # y가 key일 때 value 값을 y에 저장한다
    if x < y:                           # x가 y보다 크다면
        line[y] = x                     # x가 key y가 value로 저장한다
    elif x == y:                        # x와 y가 같다면
        print(cnt+1)                    # 이미 두 점은 이어져 있었기 때문에 사이클이 완성되므로 현재 선을 이은 횟수를 출력하고
        quit()                          # 종료한다
    else:                               # y가 x보다 크다면
        line[x] = y                     # y가 key x가 value로 저장한다

line = dict()                           # 선을 저장할 딕셔너리 생성
for cnt in range(m):                    # 선을 그을 횟수를 반복해서
    a, b = map(int, input().split())    # 선을 이을 두 점을 input 받고
    if line.get(a) == None:             # a 점이 아직 line 딕셔너리에 없다면
        line[a] = a                     # key value를 모두 a로 생성하고
    if line.get(b) == None:             # b 점이 아직 line 딕셔너리에 없다면
        line[b] = b                     # key value를 모두 b로 생성하고
    union(a, b)                         # a와 b를 잇는다
else:                                   # 선을 그을 횟수를 모두 반복했는데 사이클이 생기지 않았다면
    print(0)                            # 0을 출력한다

