# Конвейер_BOJ28938

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 벨트의 길이를 input 받고
belt = sum(list(map(int, input().split()))) # 벨트의 이동의 합을 저장해서
if belt > 0:                                # 양수라면
    print('Right')                          # 오른쪽을 출력하고
elif belt < 0:                              # 음수라면
    print('Left')                           # 왼쪽을 출력하고
else:                                       # 0이라면
    print('Stay')                           # 머무르다를 출력한다