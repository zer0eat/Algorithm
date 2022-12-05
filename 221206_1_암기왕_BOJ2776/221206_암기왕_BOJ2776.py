# 암기왕_BOJ2776

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())                               # 테스트 케이스
for t in range(T):                                          # 테스트 케이스를 반복해서
    ans = dict()                                            # 수첩 1의 내용을 저장할 딕셔너리 생성

    N = int(sys.stdin.readline())                           # 수첩 1에 적힌 숫자의 개수를 input
    nlst = list(map(int, sys.stdin.readline().split()))     # 수첩 1에 적힌 숫자를 list로 input
    for n in nlst:                                          # 수첩 1에 적힌 숫자를 반복해서
        ans[n] = 1                                          # 적힌 숫자를 key로 value가 1인 딕셔너리를 만든다

    M = int(sys.stdin.readline())                           # 수첩 2에 적힌 숫자의 개수를 input
    mlst = list(map(int, sys.stdin.readline().split()))     # 수첩 2에 적힌 숫자를 list로 input
    for m in mlst:                                          # 수첩 2에 적힌 숫자를 반복해서
        if ans.get(m) == 1:                                 # 적힌 숫자가 ans 딕셔너리에 있다면
            print(1)                                        # 1을 출력하고
        else:                                               # 없다면
            print(0)                                        # 0을 출력한다
