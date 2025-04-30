# Fill the Rowboats_BOJ5300

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 숫자를 input 받고
for n in range(1, N+1):             # 1부터 N까지 반복해서
    if n % 6:                       # 6의 배수가 아니라면
        print(n, end=' ')           # 숫자를 출력하고
    else:                           # 6의 배수가 나왔다면
        print(n, 'Go!', end=' ')    # 숫자를 출력하고 Go!를 출력한다
else:                               # 모든 수의 반복이 끝났다면
    if n % 6:                       # 6의 배수가 아니라면
        print('Go!')                # Go!를 출력한다