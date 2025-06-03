# #include <Google I/O.h>_BOJ12174

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                    # 테스트 케이스를 input받고
for t in range(T):                  # 테스트 케이스를 반복해서
    B = int(input())                # 바이트 수를 input받고
    aski = input().strip()          # 바이트를 문자로 inputqkerh
    print(f'Case #{t+1}: ', end='') # 케이스를 출력하고
    for b in range(B):              # 바이트를 반복해서
        tmp = aski[8*b:8*b+8]       # b번째 바이트를 잘라서 저장하고
        ans = ''                    # 정답을 저장할 변수를 생성한다
        for a in tmp:               # 바이트를 반복해서
            if a == 'I':            # I가 나오면
                ans += '1'          # 1을 추가하고
            else:                   # O가 나오면
                ans += '0'          # 0을 추가한다
        ans = int(ans,2)            # 변환한 바이트를 10진수로 변환하고
        print(chr(ans),end='')      # 해당 숫자의 아스키코드 문자를 출력한다
    else:                           # 케이스의 모든 바이트를 출력했다면
        print()                     # 줄을 바꿔준다