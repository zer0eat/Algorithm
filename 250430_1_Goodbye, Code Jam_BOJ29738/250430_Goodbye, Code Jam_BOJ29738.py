# Goodbye, Code Jam_BOJ29738

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                            # 테스트 케이스를 input 받고
for t in range(T):                          # 테스트 케이스를 반복해서
    case = int(input())                     # 등수를 input받고
    if case > 4500:                         # 4500등 안에 못 들었다면
        print(f'Case #{t+1}: Round 1')      # 1라운드 진출을 출력하고
    elif case > 1000:                       # 1000등 안에 못 들었다면
        print(f'Case #{t+1}: Round 2')      # 2라운드 진출을 출력하고
    elif case > 25:                         # 25등 안에 못 들었다면
        print(f'Case #{t+1}: Round 3')      # 3라운드 진출을 출력하고
    else:                                   # 25등 안에 들었다면
        print(f'Case #{t+1}: World Finals') # 최종 라운드 진출을 출력한다