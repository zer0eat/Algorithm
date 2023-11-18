# 다음순열_BOJ10972

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 순열의 길이를 input 받고
permutation = list(map(int, input().split()))   # 현재 순열을 상태를 리스트로 input 받는다
end = [i for i in range(N, 0, -1)]              # 순열의 마지막을 생성하고
if permutation == end:                          # 입력받은 순열이 마지막이라면
    print(-1)                                   # -1을 출력하고
    quit()                                      # 종료한다
else:                                           # 마지막 순열이 아니라면
    for i in range(N-1, 0, -1):                 # 순열을 뒤에서부터 반복해서
        if permutation[i-1] < permutation[i]:   # 뒤에 있는 원소가 앞에 있는 원소보다 크다면
            for j in range(N-1, 0, -1):         # 순열을 뒤에서부터 반복해서
                if permutation[i-1] < permutation[j]:                                   # 처음으로 뒤에 원소보다 작아진 원소 i-1보다 j원소가 크다면
                    permutation[i-1], permutation[j] = permutation[j], permutation[i-1] # i-1번째 원소와 j번째 원소를 바꿔주고
                    permutation = permutation[:i] + sorted(permutation[i:])             # i-1번째 이후 원소를 오름차순 정렬한다
                    print(*permutation)         # 다음 순열을 출력하고
                    quit()                      # 종료한다