# 문자열비교_13753

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())
for t in range(T):
    N = list(input())
    M = list(input())

    a = 0
    for i in range(len(M)):
        if M[i] == N[0]:
            for n in range(len(N)):
                if N[n] == M[i+n]:
                    a += i
                else:
                    pass
        else:
            pass
    print(a)
    # b = []
    # for n in range(len(N)):
    #     b.append(M[a])
    # print(b)