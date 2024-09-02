# 비트 우정지수_BOJ12782

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())            # 테스트 케이스를 input 받고
for t in range(T):          # 테스트 케이스를 반복해서
    n, m = input().split()  # 두개의 비트를 input 받고
    o, z = 0, 0             # 비트의 차이를 저장할 변수를 생성한다
    for i in range(len(n)): # 비트의 길이를 반복해서
        if n[i] != m[i]:    # 두 비트가 다를 때
            if m[i] == '1': # m 비트가 1이라면
                o += 1      # o에 1을 더하고
            else:           # m 비트가 0이라면
                z += 1      # z에 1을 더한다
    print(max(o, z))        # o,z 중 큰 값을 출력한다