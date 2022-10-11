# 비밀번호찾기_BOJ17219

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())       # N 저장된 사이트의 수 / M 찾고자하는 사이트의 수
password = dict()                                   # 저장된 사이트와 비밀번호를 저장할 딕셔너리를 생성하고
for n in range(N):                                  # N만큼 반복해서
    key, value = sys.stdin.readline().split()       # 사이트를 key에 비밀번호를 value에 저장하고
    password[key] = value                           # password 딕셔너리에 key:value 형태로 저장한다

for m in range(M):                                  # M만큼 반복해서
    s = sys.stdin.readline().rstrip()               # 찾고자하는 사이트를 s에 저장하고
    print(password.get(s))                          # s의 비밀번호를 출력한다