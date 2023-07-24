# 떡먹는호랑이_BOJ2502

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
D, K = map(int, input().split())            # D 산을 넘어온 날 / K 호랑이에게 떡을 준 개수
lst = [1] * D                               # 피보나치 수를 저장할 리스트 생성
for i in range(2, D):                       # 3번째 피보나치 수부터 D까지 반복해서
    lst[i] = lst[i-1] + lst[i-2]            # i번째 인덱스에 피보나치 수를 저장한다
A = 1                                       # 첫째날 준 떡의 개수를 A로 생성하고 
B = K // lst[D-2]                           # 둘째날 준 떡의 개수를 B로 생성한다
while 1:                                    # break가 나올때 까지 반복해서
    if lst[D-3]*A + lst[D-2]*B == K:        # D일에 준 떡의 개수가 K개인 경우에
        print(A)                            # A의 개수를 출력하고
        print(B)                            # B의 개수를 출력한 후
        break                               # while문을 break한다
    elif lst[D-3]*A + lst[D-2]*B < K:       # D일에 준 떡의 개수가 K개보다 작은경우
        A += 1                              # A의 개수를 1 추가한다
    elif lst[D-3]*A + lst[D-2]*B > K:       # D일에 준 떡의 개수가 K개보다 큰 경우
        B -= 1                              # B의 개수를 1 제거한다