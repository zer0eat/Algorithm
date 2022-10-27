# 패션왕신해빈_BOJ9375

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())                       # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복해서
    N = int(sys.stdin.readline())                   # 옷 종류의 수
    fashion = []                                    # 옷의 이름
    cnt = []                                        # 옷의 개수
    for n in range(N):                              # 옷 종류만큼 반복해서
        a = list(sys.stdin.readline().split())      # 옷의 이름과 종류를 a에 input 받고
        for f in range(len(fashion)):               # fashion을 반복해서
            if a[1] == fashion[f]:                  # a에 들어있는 옷의 종류가 패션에 들어있다면
                cnt[f] += 1                         # 해당 인덱스의 숫자를 1 증가시키고
                break                               # 반복문을 종료한다
        else:                                       # 옷의 종류가 패션에 들어 있지 않다면
            fashion.append(a[1])                    # 패션에 옷의 종류를 저장하고
            cnt.append(1)                           # 해당 인덱스에 개수를 1로 저장한다

    king = 1                                        # 경우의 수를 저장할 변수를 생성하고
    for c in cnt:                                   # cnt 를 반복해서
        king *= (c+1)                               # 옷의 종류 + 1 을 king 에 곱해준 후

    print(king-1)                                   # 아무 것도 입지 않았을 경우 1을 빼준다





