# Three Dots_BOJ13423

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                    # 테스트 케이스를 input 받고
for t in range(T):                                  # 테스트 케이스를 반복해서
    N = int(input())                                # 점의 개수를 input 받고
    lst = list(map(int, input().split()))           # 점의 위치를 리스트로 input 받는다
    lst.sort()                                      # 점의 위치를 오름차순으로 정렬하고
    dic = dict()                                    # 점의 위치를 저장할 딕셔너리를 생성한다
    for l in lst:                                   # 점의 위치를 반복해서
        dic[l] = 1                                  # 점의 위치를 key로 원소를 생성하고
    ans = 0                                         # 정답을 저장할 변수를 생성한다
    for a in range(N-2):                            # a점의 위치를 반복하고
        for b in range(a+1, N-1):                   # b점의 위치를 반복해서
            if dic.get(lst[b]+lst[b]-lst[a]):       # a와b 간격만큼 떨어진 곳에 c가 있다면
                ans += 1                            # 정답을 1 추가한다
    print(ans)                                      # 간격이 같은 세 점 a, b, c로 가능한 경우의 수를 출력한다