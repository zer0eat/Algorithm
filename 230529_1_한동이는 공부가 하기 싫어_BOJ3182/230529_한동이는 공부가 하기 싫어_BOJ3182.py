# 한동이는 공부가 하기 싫어_BOJ3182

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 선배의 수

friend = dict()                     # 선배의 답을 저장할 딕셔너리 생성
for i in range(N):                  # 선배의 수를 반복해서
    friend[i+1] = int(input())      # 선배를 key로 대답을 value로 원소를 생성

ans = 0                             # 최대 수를 저장할 변수 생성
num = 0                             # 최대 수를 말한 선배를 저장할 변수 생성
for j in range(N):                  # 선배의 수를 반복해서
    visited = [0] * (N+1)           # 방문표시를 할 리스트 생성
    cnt = 0                         # 연결된 선배의 수를 저장할 변수 생성
    A = j+1                         # 현재 선배를 A에 저장하고
    while 1:                        # break가 나올때까지 반복해서
        if visited[A] == 0:         # A 선배와 연락이 닿기 전 이라면
            visited[A] = 1          # 연락표시를 하고
            cnt += 1                # 연결된 선배의 수를 1 추가한다
            A = friend[A]           # A를 연결된 선배로 바꾼다
        else:                       # A 선배와 연락이 이미 닿아있다면
            break                   # break
    if ans < cnt:                   # ans보다 현재 연락이 닿은 선배의 수가 더 많다면
        num = j+1                   # num을 연락을 시작한 선배로 바꾸고
        ans = cnt                   # ans를 연락이 닿은 선배의 수로 바꾼다
print(num)                          # 모든 반복을 마쳤다면 가장 많이 연락이 닿게되는 시작 선배의 번호를 출력한다