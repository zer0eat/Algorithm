# 친구네트워크_BOJ4195

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def find(x):                            
    if friends[x] == x:                 # key와 value가 모두 x라면
        return x                        # x를 return
    friends[x] = find(friends[x])       # 다르다면 x의 value값으로 다시 find 함수를 통해 key, value가 같은 값이 되는 숫자를 찾아 value로 저장한다
    return friends[x]                   # 바뀐 value를 return

def union(x, y):
    x = find(x)                         # x가 key일 때 value 값을 x에 저장하고
    y = find(y)                         # y가 key일 때 value 값을 y에 저장한다
    if x != y:                          # x와 y가 다르면
        friends[y] = x                  # y를 key x를 value로 연결해주고
        num[x] += num[y]                # 친구의 수를 세는 딕셔너리에 x가 key일 때 value에 y가 key일 때 value를 더해준다
    print(num[x])                       # x가 key일 때 value를 출력한다

# input 받기
T = int(input())                        # T 테스트 케이스
for t in range(T):                      # 테스트 케이스를 반복해서
    F = int(input())                    # F 친구 관계의 수

    friends = dict()                    # 친구관계를 저장할 딕셔너리 생성
    num = dict()                        # 친구의 수를 저장할 딕셔너리 생성

    for f in range(F):                  # 친구 관계의 수를 반복해서
        A = list(input().split())       # 친구 관계가 된 두 사람을 input 받고
        if friends.get(A[0]) == None:   # 0 인덱스의 사람이 friends에 저장되어 있지 않다면
            friends[A[0]] = A[0]        # key, value를 0 인덱스의 사람 이름으로 friends에 생성하고
            num[A[0]] = 1               # num 딕셔너리에 해당 사람의 이름을 key로 현재는 친구관계가 없으므로 value를 1로 생성한다
        if friends.get(A[1]) == None:   # 1 인덱스의 사람이 friends에 저장되어 있지 않다면
            friends[A[1]] = A[1]        # key, value를 1 인덱스의 사람 이름으로 friends에 생성하고
            num[A[1]] = 1               # num 딕셔너리에 해당 사람의 이름을 key로 현재는 친구관계가 없으므로 value를 1로 생성한다
        union(A[0], A[1])               # 두 사람을 친구관계로 연결한 후 연결된 사람의 수를 계산한다