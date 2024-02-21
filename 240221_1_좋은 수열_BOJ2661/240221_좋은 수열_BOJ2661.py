# 좋은 수열_BOJ2661

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 수열의 길이를 input 받고

def check(num):
    M = len(num)                                # num의 길이를 저장하고
    for i in range(1, M):                       # 비교할 길이를 반복하고
        for j in range(M):                      # 시작점의 위치를 반복해서
            if num[j:j+i] == num[j+i:j+i+i]:    # j번부터 i까지의 길이와 j+i번부터 j+i+i까지 길이가 같다면
                return True                     # 좋은 수열이 아니므로 True를 return한다
    else:                                       # 모든 for문을 통과했다면
        return False                            # 좋은 수열이므로 False를 return한다

def recur(dep, tmp):
    if check(tmp):                              # tmp를 check함수를 통해 탐색해서
        return                                  # 좋은 수열이 아니라면 return한다
    if dep == N:                                # 깊이가 N이 되었다면
        print(tmp)                              # 좋은 수열을 출력하고
        quit()                                  # 종료한다
    for i in ['1', '2', '3']:                   # 1, 2, 3 숫자를 반복해서
        recur(dep+1, tmp+i)                     # tmp에 i를 더한 후 깊이 dep+1부터 좋은 수열을 탐색한다

recur(0, '')                                    # 깊이 0부터 길이 N의 좋은 수열을 탐색한다